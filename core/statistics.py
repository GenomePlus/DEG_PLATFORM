"""
Statistical functions for DEG analysis
"""

import numpy as np
from scipy import stats


def ttest(group1, group2):
    """
    Perform t-test
    """

    stat, pvalue = stats.ttest_ind(group1, group2)

    return pvalue


def benjamini_hochberg(pvalues):
    """
    FDR correction
    """

    pvalues = np.array(pvalues)
    n = len(pvalues)

    order = np.argsort(pvalues)
    ranked = np.empty(n)

    for i, idx in enumerate(order):
        ranked[idx] = pvalues[idx] * n / (i + 1)

    return np.minimum(ranked, 1.0)


def log2_fold_change(group1_mean, group2_mean):
    """
    Compute log2 fold change
    """

    if group2_mean == 0:
        return 0

    return np.log2(group1_mean / group2_mean)
