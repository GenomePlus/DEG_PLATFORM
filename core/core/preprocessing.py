"""
Data preprocessing module
"""

import pandas as pd
import numpy as np


def clean_numeric_columns(df):
    """
    Convert numeric columns safely
    """

    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")

    return df


def drop_missing(df):
    """
    Remove missing rows
    """
    return df.dropna()


def log_transform(series):
    """
    Log2 transform expression
    """
    return np.log2(series + 1)


def normalize_expression(series):
    """
    Normalize gene expression
    """
    return (series - series.mean()) / series.std()
