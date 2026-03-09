"""
Global configuration file for Systems Biology Platform
"""

import os

# ----------------------------
# PROJECT PATHS
# ----------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "analysis_results")

PLOTS_DIR = os.path.join(OUTPUT_DIR, "plots")
TABLES_DIR = os.path.join(OUTPUT_DIR, "tables")
NETWORK_DIR = os.path.join(OUTPUT_DIR, "network")
ENRICHMENT_DIR = os.path.join(OUTPUT_DIR, "enrichment")

# Create directories if missing
for folder in [OUTPUT_DIR, PLOTS_DIR, TABLES_DIR, NETWORK_DIR, ENRICHMENT_DIR]:
    os.makedirs(folder, exist_ok=True)

# ----------------------------
# BIOLOGICAL DATABASE SETTINGS
# ----------------------------

# STRING database parameters
STRING_API_URL = "https://string-db.org/api"
STRING_SPECIES_ID = 9606
STRING_SCORE_THRESHOLD = 700

# Enrichr API
ENRICHR_ADDLIST_URL = "https://maayanlab.cloud/Enrichr/addList"
ENRICHR_ENRICH_URL = "https://maayanlab.cloud/Enrichr/enrich"

# gProfiler
GPROFILER_URL = "https://biit.cs.ut.ee/gprofiler/api/gost/profile/"

# miRNA library
MIRNA_LIBRARY = "miRTarBase_2017"

# TF library
TF_LIBRARY = "ChEA_2016"

# GO libraries
GO_BP = "GO_Biological_Process_2021"
GO_CC = "GO_Cellular_Component_2021"
GO_MF = "GO_Molecular_Function_2021"

# KEGG
KEGG_LIBRARY = "KEGG_2021_Human"

# ----------------------------
# DEG DEFAULT PARAMETERS
# ----------------------------

DEFAULT_LOGFC = 1.0
DEFAULT_PVALUE = 0.05

# Adaptive analysis parameters
MONTE_CARLO_ITERATIONS = 200
GENETIC_ALGO_GENERATIONS = 50

# ----------------------------
# PERFORMANCE SETTINGS
# ----------------------------

MAX_GENES = 25000
MAX_FILE_SIZE_MB = 100

# ----------------------------
# GOOGLE DRIVE DATA LINKS
# (Optional remote datasets)
# ----------------------------

GOOGLE_DRIVE_DATABASES = {
    "mirna_backup":
    "https://drive.google.com/uc?id=YOUR_FILE_ID",
}
