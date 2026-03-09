from gprofiler import GProfiler
import pandas as pd


def run_gprofiler(genes):

    gp = GProfiler(return_dataframe=True)

    res = gp.profile(
        organism="hsapiens",
        query=genes
    )

    return res
