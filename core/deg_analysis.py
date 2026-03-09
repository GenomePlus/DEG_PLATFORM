"""
Differential Gene Expression Analysis
"""

import pandas as pd
from .statistics import log2_fold_change, ttest, benjamini_hochberg


def compute_deg(df,
                gene_col,
                group1_cols,
                group2_cols):
    """
    Compute DEG statistics
    """

    results = []

    for _, row in df.iterrows():

        gene = row[gene_col]

        group1 = row[group1_cols].astype(float)
        group2 = row[group2_cols].astype(float)

        g1_mean = group1.mean()
        g2_mean = group2.mean()

        logfc = log2_fold_change(g1_mean, g2_mean)

        pvalue = ttest(group1, group2)

        results.append({
            "gene": gene,
            "logFC": logfc,
            "pvalue": pvalue
        })

    res_df = pd.DataFrame(results)

    res_df["adj_pvalue"] = benjamini_hochberg(res_df["pvalue"])

    return res_df
