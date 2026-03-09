import pandas as pd


def download_table(df, filename):

    return df.to_csv(index=False).encode("utf-8")
