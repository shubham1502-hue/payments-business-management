import pandas as pd
import unittest

from src.kpi_engine import build_kpis


class PaymentsBusinessValidationTests(unittest.TestCase):
    def test_sample_data_exists(self):
        df = pd.read_csv("data/payments_monthly_data_sample.csv")
        self.assertGreater(len(df), 0)

    def test_kpi_engine_builds_core_reports(self):
        df = pd.read_csv("data/payments_monthly_data_sample.csv")
        reports = build_kpis(df)
        self.assertIn("monthly_kpis", reports)
        self.assertIn("regional_summary", reports)
        self.assertGreater(len(reports["monthly_kpis"]), 0)


if __name__ == "__main__":
    unittest.main()
