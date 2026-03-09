def interpret_hub_genes(hub_df):

    top_genes = hub_df.head(10)

    report = []

    for _, row in top_genes.iterrows():

        report.append(
            f"{row['gene']} is a high degree hub gene."
        )

    return report
