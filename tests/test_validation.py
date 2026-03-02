import pandas as pd

def test_sample_data_exists():
    df = pd.read_csv("data/payments_monthly_data_sample.csv")
    assert len(df) > 0
