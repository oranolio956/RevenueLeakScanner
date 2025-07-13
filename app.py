import streamlit as st
from utils import run_kpis, segment_fans, kpi_traffic_lights
from pdf_report import build_pdf

st.set_page_config(page_title="Revenue-Leak Scanner", layout="centered")

st.title("🩺 5-Minute Revenue-Leak Scanner")

uploaded = st.file_uploader(
    "Drag & drop your OnlyFans CSV export (Subscriptions + PPV + Tips)", 
    type=["csv"]
)

if uploaded:
    df = run_kpis(uploaded)
    traffic = kpi_traffic_lights(df)
    segs   = segment_fans(df)

    st.subheader("Key Results")
    st.metric("Churn %",          f"{traffic['churn_pct']}%")
    st.metric("Rev. Diversification", traffic['hhi'])
    st.metric("Content Velocity", traffic['cve'])
    st.metric("Whales Share",     f"{segs['whales_share']}%")

    st.write("---")
    if st.button("Download 2-page PDF Snapshot"):
        pdf_bytes = build_pdf(df, traffic, segs)
        st.download_button(
            label="📄  Download Report",
            data=pdf_bytes,
            file_name="RevenueLeakSnapshot.pdf",
            mime="application/pdf"
        )
