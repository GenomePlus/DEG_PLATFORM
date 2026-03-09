"""
Data Loader for gene expression datasets
Supports CSV, TSV, XLSX and GEO series matrix
"""

import pandas as pd


def load_expression_data(uploaded_file):
    """
    Load uploaded dataset
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


def preview_data(df, n=5):
    """
    Preview dataset
    """
    return df.head(n)


def dataset_summary(df):
    """
    Basic dataset summary
    """
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns)
    }
