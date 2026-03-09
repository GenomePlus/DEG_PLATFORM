import streamlit as st
import pandas as pd

from core.data_loader import load_expression_data
from core.deg_analysis import perform_deg_analysis
from visualization.volcano_plot import generate_volcano_plot

from databases.database_connector import (
    fetch_string_ppi,
    fetch_enrichment,
    fetch_mirna_targets,
    fetch_tf_targets
)

from networks.ppi_network import build_ppi_network
from networks.mirna_network import build_mirna_network
from networks.tf_network import build_tf_network

st.set_page_config(page_title="Systems Bioinformatics Platform", layout="wide")

st.title("Integrated Bioinformatics Analysis Platform")

uploaded_file = st.file_uploader("Upload Gene Expression CSV", type=["csv"])

if uploaded_file:

    df = load_expression_data(uploaded_file)

    st.subheader("Raw Data")
    st.dataframe(df)

    if st.button("Run DEG Analysis"):

        results = perform_deg_analysis(df)

        all_genes = results["all"]
        up_genes = results["up"]
        down_genes = results["down"]

        st.subheader("All Genes")
        st.dataframe(all_genes)

        st.subheader("Upregulated Genes")
        st.dataframe(up_genes)

        st.subheader("Downregulated Genes")
        st.dataframe(down_genes)

        fig = generate_volcano_plot(all_genes)

        st.subheader("Volcano Plot")
        st.pyplot(fig)

        gene_list = all_genes["gene"].tolist()

        st.subheader("PPI Network")

        edges = fetch_string_ppi(gene_list)

        ppi_graph = build_ppi_network(edges)

        st.write(ppi_graph)

        st.subheader("GO / KEGG Enrichment")

        enrichment = fetch_enrichment(gene_list)

        st.dataframe(enrichment)

        st.subheader("miRNA Network")

        mirna_edges = fetch_mirna_targets(gene_list)

        mirna_net = build_mirna_network(mirna_edges)

        st.write(mirna_net)

        st.subheader("TF Network")

        tf_edges = fetch_tf_targets(gene_list)

        tf_net = build_tf_network(tf_edges)

        st.write(tf_net)
