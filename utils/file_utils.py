"""
File utilities for loading gene datasets
"""

import pandas as pd
import os


def load_gene_file(uploaded_file):
    """
    Load gene expression dataset
    Supports CSV, TSV, XLSX
    """

    filename = uploaded_file.name.lower()

    if filename.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    elif filename.endswith(".tsv"):
        df = pd.read_csv(uploaded_file, sep="\t")

    elif filename.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

    else:
        raise ValueError("Unsupported file format")

    return df


def save_table(df, path):
    """
    Save dataframe to CSV
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)


def ensure_columns(df, required_cols):
    """
    Validate required columns
    """

    missing = [c for c in required_cols if c not in df.columns]

    if missing:
        raise ValueError(f"Missing columns: {missing}")

    return True
