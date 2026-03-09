import requests
import pandas as pd


def fetch_mirtarbase_interactions(gene_list):

    """
    Fetch miRNA-target interactions from miRTarBase
    """

    interactions = []

    base_url = "https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2022/php/search.php"

    for gene in gene_list:

        try:

            params = {
                "opt": "search",
                "gene": gene
            }

            response = requests.get(base_url, params=params, timeout=10)

            if response.status_code != 200:
                continue

            data = response.json()

            for record in data.get("data", []):

                interactions.append({
                    "miRNA": record.get("mirna"),
                    "target_gene": gene,
                    "support_type": record.get("_
