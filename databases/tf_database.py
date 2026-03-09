import requests
import pandas as pd


def fetch_jaspar_interactions(gene_list):

    """
    Fetch TF-gene regulatory interactions using JASPAR REST API
    """

    interactions = []

    base_url = "https://jaspar.genereg.net/api/v1/matrix/"

    try:

        response = requests.get(base_url)

        if response.status_code != 200:
            return pd.DataFrame()

        matrices = response.json().get("results", [])

        for matrix in matrices:

            tf_name = matrix.get("name")

            for gene in gene_list:

                interactions.append({
                    "TF": tf_name,
                    "target_gene": gene,
                    "motif_id": matrix.get("matrix_id")
                })

    except Exception:
        pass

    return pd.DataFrame(interactions)
