from databases.enrichr_api import run_enrichr
from databases.gprofiler_api import run_gprofiler


def perform_enrichment(genes):

    enrichr_results = run_enrichr(genes)

    gprofiler_results = run_gprofiler(genes)

    return {
        "enrichr": enrichr_results,
        "gprofiler": gprofiler_results
    }
