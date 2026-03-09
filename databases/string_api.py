import requests
import pandas as pd


def get_string_interactions(genes):

    gene_str = "%0d".join(genes)

    url = f"https://string-db.org/api/tsv/network?identifiers={gene_str}&species=9606"

    response = requests.get(url)

    lines = response.text.strip().split("\n")

    edges = []

    for line in lines[1:]:

        parts = line.split("\t")

        edges.append({
            "protein1": parts[2],
            "protein2": parts[3],
            "score": parts[5]
        })

    return pd.DataFrame(edges)
