import requests
import pandas as pd


def annotate_genes(genes):

    url = "https://mygene.info/v3/query"

    annotations = []

    for g in genes:

        r = requests.get(url, params={"q": g, "species": "human"})

        data = r.json()

        if "hits" in data and len(data["hits"]) > 0:

            hit = data["hits"][0]

            annotations.append({
                "gene": g,
                "name": hit.get("name"),
                "symbol": hit.get("symbol")
            })

    return pd.DataFrame(annotations)
