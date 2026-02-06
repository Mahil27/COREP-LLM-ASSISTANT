import streamlit as st
from rag_pipeline import run_query
from validator import validate_output

st.set_page_config(page_title="COREP Assistant", layout="wide")

st.title("LLM-Powered COREP Reporting Assistant")

query = st.text_area("Enter reporting scenario")

if st.button("Generate Report") and query:

    result, docs = run_query(query)

    st.subheader("Structured Output")

    st.table({
        "Field": [
            "Capital Type",
            "Amount",
            "Risk Weight",
            "Template Section"
        ],
        "Value": [
            result.capital_type,
            result.amount,
            result.risk_weight,
            result.template_section
        ]
    })

    flags = validate_output(result)

    if flags:
        st.subheader("Validation Flags")
        for f in flags:
            st.warning(f)

    st.subheader("Audit Trail")

    for d in docs:
        st.info(d.page_content)
