"""
Mathematical utilities for biomathematical algorithms
"""

import numpy as np


def normalize_series(series):
    """
    Normalize values between 0 and 1
    """
    min_val = np.min(series)
    max_val = np.max(series)

    if max_val == min_val:
        return np.zeros(len(series))

    return (series - min_val) / (max_val - min_val)


def z_score(series):
    """
    Z-score normalization
    """
    mean = np.mean(series)
    std = np.std(series)

    if std == 0:
        return np.zeros(len(series))

    return (series - mean) / std


def safe_log10(x):
    """
    Prevent log errors
    """
    return np.log10(np.clip(x, 1e-10, None))


def gene_ratio(hit_genes, total_genes):
    """
    Compute gene ratio for pathway scoring
    """
    if total_genes == 0:
        return 0
    return hit_genes / total_genes
