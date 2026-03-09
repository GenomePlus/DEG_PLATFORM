import requests
import pandas as pd


def run_enrichr(genes):

    ENRICHR_ADD = "https://maayanlab.cloud/Enrichr/addList"
    ENRICHR_RESULTS = "https://maayanlab.cloud/Enrichr/enrich"

    payload = {
        "list": "\n".join(genes),
        "description": "gene_list"
    }

    r = requests.post(ENRICHR_ADD, files=payload)

    user_list_id = r.json()["userListId"]

    params = {
        "userListId": user_list_id,
        "backgroundType": "KEGG_2021_Human"
    }

    r = requests.get(ENRICHR_RESULTS, params=params)

    data = r.json()

    records = []

    for item in data["KEGG_2021_Human"]:

        records.append({
            "pathway": item[1],
            "pvalue": item[2],
            "combined_score": item[4]
        })

    return pd.DataFrame(records)
