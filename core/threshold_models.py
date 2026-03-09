"""
Threshold models for DEG classification
"""

def classify_deg(df, logfc_col="logFC", p_col="pvalue",
                 logfc_threshold=1.0,
                 p_threshold=0.05):

    up = df[
        (df[logfc_col] >= logfc_threshold) &
        (df[p_col] < p_threshold)
    ]

    down = df[
        (df[logfc_col] <= -logfc_threshold) &
        (df[p_col] < p_threshold)
    ]

    neutral = df.drop(up.index.union(down.index))

    return up, down, neutral
