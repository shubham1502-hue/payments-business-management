from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "payments_monthly_data_sample.csv"
REPORTS_DIR = ROOT / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["month"] = pd.to_datetime(df["month"])
    df["region"] = df["region"].fillna("Unknown")
    return df


def build_kpis(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    monthly = (
        df.groupby("month")
        .agg(
            gross_revenue=("gross_revenue", "sum"),
            operating_cost=("operating_cost", "sum"),
            budget_revenue=("budget_revenue", "sum"),
            transaction_volume=("transaction_volume", "sum"),
            chargebacks=("chargebacks", "sum"),
            sla_breaches=("sla_breaches", "sum"),
        )
        .reset_index()
        .sort_values("month")
    )
    monthly["revenue_growth_mom"] = monthly["gross_revenue"].pct_change().fillna(0)
    monthly["cost_to_income_ratio"] = monthly["operating_cost"] / monthly["gross_revenue"]
    monthly["chargeback_rate"] = monthly["chargebacks"] / monthly["transaction_volume"]
    monthly["budget_variance"] = monthly["gross_revenue"] - monthly["budget_revenue"]
    monthly["budget_variance_pct"] = monthly["budget_variance"] / monthly["budget_revenue"]

    regional = (
        df.groupby("region")
        .agg(
            gross_revenue=("gross_revenue", "sum"),
            transaction_volume=("transaction_volume", "sum"),
            sla_breaches=("sla_breaches", "sum"),
        )
        .reset_index()
        .sort_values("gross_revenue", ascending=False)
    )
    regional["revenue_share"] = regional["gross_revenue"] / regional["gross_revenue"].sum()

    merchant = (
        df.groupby(["merchant_id", "merchant_segment", "region"])
        .agg(
            gross_revenue=("gross_revenue", "sum"),
            budget_revenue=("budget_revenue", "sum"),
            sla_breaches=("sla_breaches", "sum"),
            chargebacks=("chargebacks", "sum"),
            transaction_volume=("transaction_volume", "sum"),
        )
        .reset_index()
    )
    merchant["budget_variance_pct"] = (
        (merchant["gross_revenue"] - merchant["budget_revenue"]) / merchant["budget_revenue"]
    )
    merchant["chargeback_rate"] = merchant["chargebacks"] / merchant["transaction_volume"]
    underperformers = merchant.sort_values(["budget_variance_pct", "sla_breaches"]).head(10)
    sla_alerts = merchant[merchant["sla_breaches"] >= merchant["sla_breaches"].quantile(0.90)]

    return {
        "monthly_kpis": monthly,
        "regional_summary": regional,
        "top_underperforming_merchants": underperformers,
        "sla_alerts": sla_alerts,
    }


def write_reports(reports: dict[str, pd.DataFrame]) -> None:
    for name, report in reports.items():
        report.to_csv(REPORTS_DIR / f"{name}.csv", index=False)

    latest = reports["monthly_kpis"].iloc[-1]
    summary = [
        "# Payments Business KPI Executive Summary",
        "",
        f"Latest month: {latest['month'].date()}",
        f"Gross revenue: {latest['gross_revenue']:.2f}",
        f"MoM revenue growth: {latest['revenue_growth_mom']:.2%}",
        f"Cost-to-income ratio: {latest['cost_to_income_ratio']:.2%}",
        f"Chargeback rate: {latest['chargeback_rate']:.2%}",
        f"Budget variance: {latest['budget_variance']:.2f} ({latest['budget_variance_pct']:.2%})",
        f"SLA breaches: {int(latest['sla_breaches'])}",
        "",
        "Use the CSV reports for monthly business review, regional diagnosis, and merchant-level follow-up.",
    ]
    (REPORTS_DIR / "executive_summary.md").write_text("\n".join(summary), encoding="utf-8")


if __name__ == "__main__":
    data = load_data()
    reports = build_kpis(data)
    write_reports(reports)
    print(f"Reports generated in {REPORTS_DIR}")
