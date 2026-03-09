from databases.string_api import get_string_interactions
from databases.enrichr_api import run_enrichr
from databases.mirTarBase_api import get_mirtarbase_targets
from databases.jaspar_api import get_jaspar_targets


def fetch_string_ppi(genes):

    edges = get_string_interactions(genes)

    return edges


def fetch_enrichment(genes):

    enrichment = run_enrichr(genes)

    return enrichment


def fetch_mirna_targets(genes):

    targets = get_mirtarbase_targets(genes)

    return targets


def fetch_tf_targets(genes):

    targets = get_jaspar_targets(genes)

    return targets
