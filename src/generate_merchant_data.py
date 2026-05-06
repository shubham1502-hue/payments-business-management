from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)


def generate_payments_data(months: int = 6, merchants: int = 100, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    segments = ["SME", "Mid-Market", "Enterprise"]
    regions = ["India", "APAC", "EMEA", "Americas"]
    month_range = pd.date_range("2025-01-01", periods=months, freq="MS")
    rows = []

    for merchant_id in range(1, merchants + 1):
        segment = rng.choice(segments, p=[0.55, 0.30, 0.15])
        region = rng.choice(regions)
        base_volume = {
            "SME": rng.integers(8_000, 40_000),
            "Mid-Market": rng.integers(70_000, 160_000),
            "Enterprise": rng.integers(250_000, 450_000),
        }[segment]
        take_rate = {"SME": 0.016, "Mid-Market": 0.012, "Enterprise": 0.009}[segment]

        for month in month_range:
            volume = int(base_volume * rng.normal(1.0, 0.05))
            gross_revenue = round(volume * take_rate, 2)
            operating_cost = round(gross_revenue * rng.uniform(0.48, 0.72), 2)
            chargebacks = int(volume * rng.uniform(0.001, 0.004))
            sla_breaches = int(rng.poisson({"SME": 0.6, "Mid-Market": 2.4, "Enterprise": 6.5}[segment]))
            budget_revenue = round(gross_revenue * rng.normal(1.0, 0.03), 2)
            rows.append(
                {
                    "merchant_id": merchant_id,
                    "merchant_segment": segment,
                    "region": region,
                    "month": month.date().isoformat(),
                    "transaction_volume": volume,
                    "gross_revenue": gross_revenue,
                    "operating_cost": operating_cost,
                    "chargebacks": chargebacks,
                    "sla_breaches": sla_breaches,
                    "budget_revenue": budget_revenue,
                }
            )

    return pd.DataFrame(rows)


if __name__ == "__main__":
    output_path = DATA_DIR / "payments_monthly_data_sample.csv"
    df = generate_payments_data()
    df.to_csv(output_path, index=False)
    print(f"Generated {len(df)} rows: {output_path}")
