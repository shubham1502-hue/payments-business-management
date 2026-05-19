# Payments Business Management Command Center

Payments business management workflow for merchant health, margin, SLA risk, budget variance, and regional performance.

<!-- FOUNDER_OS_STANDARD_README -->

## Portfolio role

This is a supporting fintech and business operations analytics repo. Use it to inspect merchant health, margin pressure, SLA risk, budget variance, and regional performance. It supports the portfolio as an analytics proof point, not as a flagship Founder OS module.

## The founder problem

Payments businesses lose visibility when revenue, cost, merchant health, chargebacks, SLA risk, and regional performance sit in disconnected reports. Founders need one monthly pack that identifies where the business is healthy and where follow-up is needed.

## What this repo does

- generates sample merchant portfolio data
- calculates payment business KPIs
- flags margin and SLA risk
- runs validation checks

## What a founder gets in 10 minutes

- merchant portfolio sample
- monthly KPI pack
- risk flags
- validation results
- business review inputs

## Before and after

Before:

- finance, merchant, and support data separated
- manual monthly reporting
- unclear merchant follow-up
- SLA and margin issues found late

After:

- monthly business pack
- merchant-level risk view
- validation checks
- clear follow-up list

## Who this is for

- fintech founders
- payments operators
- Founder's Office teams
- BizOps operators
- RevOps operators

## Quick start

- Run `python3 -m pip install -r requirements.txt`.
- Run `python3 src/generate_merchant_data.py`.
- Run `python3 src/kpi_engine.py`.
- Run `python3 -m unittest discover -s tests -v`.
- After running the KPI engine, open `reports/executive_summary.md` locally.

## How to fork and use this for your company

1. Click Fork.
2. Rename the repo if needed.
3. Replace `data/payments_monthly_data_sample.csv` with your private merchant portfolio export.
4. Update KPI thresholds in `src/kpi_engine.py`.
5. Run the KPI engine before the monthly business review.
6. Move outputs into Google Sheets, Notion, Tableau, Power BI, or an internal ops tracker.

### Non-technical path

- Replace one CSV: `data/payments_monthly_data_sample.csv`.
- Edit threshold values in `src/kpi_engine.py` only if needed.
- Run one KPI command.
- Read the locally generated `reports/executive_summary.md` first.

## Input format

- merchant ID
- region
- GMV
- net revenue
- cost
- margin
- chargebacks
- SLA performance
- budget or target fields

The default sample data and examples are synthetic, anonymized, or template-only unless the repo explicitly documents a public source. Keep private customer, prospect, employee, investor, borrower, merchant, payment, or company data out of public forks.

## Output files

- `data/payments_monthly_data_sample.csv`: generated merchant sample data
- `reports/monthly_kpis.csv`, `reports/regional_summary.csv`, `reports/top_underperforming_merchants.csv`, and `reports/sla_alerts.csv`: KPI engine outputs generated locally under `reports/`
- `reports/executive_summary.md`: founder-ready monthly summary generated locally after running the KPI engine
- validation output from `tests/test_validation.py`

## Example founder workflow

- Week 1: refresh merchant data.
- Week 2: run KPI engine.
- Week 3: review margin, SLA, and chargeback risks.
- Week 4: assign merchant follow-ups and update leadership narrative.

## Customization guide

Customize these before using the repo for a real company:

- merchant segments
- risk thresholds
- regions
- budget variance rules
- SLA definitions

## Where this fits in the Founder OS

This is a fintech operating module. Pair it with `fintech-transaction-analytics-monitoring-system` for transaction reliability and `startup-metrics-playbook` for metric definitions.

## Why this matters

This is not a generic finance dashboard. It is a payments business review workflow for deciding where to intervene.

## Roadmap

- Tableau or Power BI export
- Slack alerts
- merchant health scorecard
- weekly payments review
- processor data import

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) if present. Practical improvements are welcome when they make the workflow easier to fork, run, or adapt.

## License

MIT License. See [LICENSE](LICENSE).

## Built by

Built by Shubham Singh, a founder-facing operator focused on RevOps, GTM systems, startup metrics, AI workflows, and operating systems for early-stage teams.

## Use this in your company

Fork it, replace the sample inputs with your company context, and run the workflow. Start with the main output listed in the Quick Start section. Keep private data out of public forks.

## If you are a Founder's Office candidate

Use this repo to understand how a founder-facing operator turns messy inputs into decisions, cadence, and execution artifacts. Fork it, adapt it to a real company example, and write a short case note explaining what changed.

---

## Detailed implementation notes

The founder-facing guide above is the fastest path. The original repo-specific notes are preserved below for deeper implementation context.

A reusable payments business management operating system for fintech founders, payments leads, business operations teams, and Founder's Office operators.

Payments businesses lose visibility when revenue, cost, merchant health, chargebacks, SLA risk, budget variance, and regional performance sit in disconnected reports. This repo turns merchant portfolio data into a monthly management pack that helps operators see where the business is growing, where margin or SLA risk is building, and which merchants or regions need follow-up.

## Problem

Payments and fintech teams often have data spread across processors, merchant systems, support queues, finance sheets, and regional performance reports. That creates three operating problems:

- Revenue and cost trends are reviewed separately instead of as contribution health.
- Merchant-level underperformance is hidden until it becomes a portfolio issue.
- SLA breaches, chargebacks, and budget variance are not tied back to business ownership.

This project provides a compact reporting workflow for monthly payments business reviews: portfolio data in, KPI reports and executive summary out.

## What This Repo Includes

- `src/generate_merchant_data.py`: creates a synthetic merchant portfolio dataset across segments, regions, months, transaction volume, revenue, cost, chargebacks, SLA breaches, and budget revenue.
- `src/kpi_engine.py`: builds monthly KPIs, regional summaries, underperforming merchant views, SLA alert lists, and an executive summary.
- `data/payments_monthly_data_sample.csv`: tracked sample dataset used by the KPI engine and tests.
- `tests/test_validation.py`: basic validation checks for sample data and core report generation.
- `requirements.txt`: Python dependencies.
- `.gitignore`: excludes local reports, logs, caches, virtualenvs, DBs, and scratch outputs.
- `LICENSE`: MIT license for reuse.

Generated reporting outputs are written to `reports/`, which is ignored by Git so local report refreshes are not accidentally staged.

## System Workflow

1. Generate or replace the merchant portfolio dataset.
2. Load monthly merchant-level payments data.
3. Calculate revenue, cost, chargeback, SLA, budget variance, and regional contribution KPIs.
4. Identify underperforming merchants and high-SLA-risk merchants.
5. Export operator-ready CSV reports and an executive summary.
6. Use the outputs in a monthly business review, founder update, or payments ops cadence.

## KPI Logic

The repo models a payments portfolio at merchant-month grain:

```text
Merchant + Month -> Volume / Revenue / Cost / Chargebacks / SLA Breaches / Budget -> Reports
```

Core logic:

- Monthly revenue growth = month-over-month gross revenue change.
- Cost-to-income ratio = operating cost / gross revenue.
- Chargeback rate = chargebacks / transaction volume.
- Budget variance = gross revenue - budget revenue.
- Budget variance percentage = budget variance / budget revenue.
- Regional contribution = regional gross revenue share of total gross revenue.
- Underperforming merchants = merchants sorted by budget variance percentage and SLA breaches.
- SLA alerts = merchants at or above the 90th percentile of SLA breaches.

The sample data is synthetic and intended for portfolio demonstration and adaptation. It should be replaced before using the workflow inside a real company.

## Example Business Management Use Cases

- Founder monthly review: understand whether revenue growth is being offset by cost, chargebacks, or SLA risk.
- Payments business management: identify merchants that need pricing, support, or account-management intervention.
- Regional performance review: compare revenue contribution and operational risk by geography.
- Portfolio health monitoring: track budget variance and SLA breaches across merchant segments.
- Investor or board reporting: convert operating KPIs into an executive-ready monthly summary.
- Payments ops cadence: create a consistent reporting layer for follow-up, ownership, and escalation.

## Use This In Your Company

1. Replace the synthetic CSV with a real merchant portfolio export.
2. Map your source fields to merchant ID, segment, region, month, transaction volume, revenue, cost, chargebacks, SLA breaches, and budget revenue.
3. Tune KPI definitions so budget variance, chargeback rate, and SLA alerts match how your business is managed.
4. Run the KPI engine before the monthly business review.
5. Review the underperforming merchant and SLA alert files with named business owners.
6. Use the executive summary as the first draft for founder, leadership, investor, or board reporting.
7. Keep generated reports local unless you intentionally want to publish sanitized sample outputs.

## Minimum Edits Before First Use

| Edit | Where | Why |
| --- | --- | --- |
| Replace sample merchant data | `data/payments_monthly_data_sample.csv` | The KPI engine depends on this dataset for revenue, cost, chargeback, SLA, budget, and regional views. |
| Map real portfolio fields | `src/kpi_engine.py` | Align the current column names with your processor, warehouse, CRM, or finance export. |
| Tune SLA risk logic | `src/kpi_engine.py` | The current alert logic uses merchants at or above the 90th percentile of SLA breaches. |
| Tune underperformance logic | `src/kpi_engine.py` | The current ranking uses budget variance percentage and SLA breaches. |
| Adapt executive summary language | `src/kpi_engine.py` | Match your leadership, board, or investor reporting tone. |
| Update validation checks | `tests/test_validation.py` | Prevent future data changes from silently breaking the reporting workflow. |

## How To Run / Use

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Generate sample merchant data:

```bash
python3 src/generate_merchant_data.py
```

Run the KPI engine:

```bash
python3 src/kpi_engine.py
```

Run validation checks:

```bash
python3 -m unittest discover -s tests -v
```

The generator writes `data/payments_monthly_data_sample.csv`. The KPI engine writes reports into `reports/`. Because `reports/` is ignored, local report runs will not be staged unless the ignore rules are changed.

## Outputs

The KPI engine creates these local files under `reports/`:

- `monthly_kpis.csv`: monthly revenue, cost, volume, chargeback, SLA, and budget variance metrics.
- `regional_summary.csv`: gross revenue, transaction volume, SLA breaches, and revenue share by region.
- `top_underperforming_merchants.csv`: merchant-level follow-up list based on budget variance and SLA risk.
- `sla_alerts.csv`: merchants with high SLA breach counts relative to the portfolio.
- `executive_summary.md`: concise monthly business-management summary for leadership review.

## Folder Structure

```text
.
|-- data/
|  `-- payments_monthly_data_sample.csv
|-- src/
|  |-- generate_merchant_data.py
|  `-- kpi_engine.py
|-- tests/
|  `-- test_validation.py
|-- .gitignore
|-- LICENSE
|-- README.md
`-- requirements.txt
```

## Customization Guide

- For merchant acquiring: add approval rate, dispute rate, settlement lag, MDR, and merchant category.
- For fintech SaaS: add customer cohort, subscription revenue, payment failure reason, and plan tier.
- For regional management: add country, currency, FX assumptions, and regional owner.
- For Founder's Office reporting: add owner, intervention, status, next action, and review date to merchant outputs.
- For board reporting: add target metrics, forecast variance, risk commentary, and month-end narrative.

Keep the operating loop stable: refresh portfolio data, calculate KPIs, identify variance and risk, assign follow-up owners, and review the business monthly.

## Portfolio Note

This repo is part of a Founder's Office / startup operator portfolio focused on practical business operating systems. It demonstrates how a fintech operator can turn payments portfolio data into KPI visibility, merchant risk detection, regional contribution analysis, and executive-ready reporting.
