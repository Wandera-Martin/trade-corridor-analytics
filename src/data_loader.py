import pandas as pd

def load_data(path):
    return pd.read_csv(
        path,
        parse_dates=[
            "depart_time",
            "arrive_time",
            "border_arrive_time",
            "border_exit_time",
        ])