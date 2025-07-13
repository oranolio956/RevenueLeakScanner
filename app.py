import streamlit as st
from utils import run_kpis, kpi_traffic_lights, segment_fans, build_pdf_lazy

# ── Page config ───────────────────────────────────────────────────────
st.set_page_config(page_title="Revenue-Leak Scanner", layout="centered")
st.title("🩺  Revenue-Leak Scanner (≤60 s)")

# ── File uploader ─────────────────────────────────────────────────────
uploaded = st.file_uploader(
    "Drop your OnlyFans CSV (subscriptions, PPV, tips). Required columns: "
    "`fan_id, date, revenue, type`.",
    type=["csv"],
)

# ── Processing ────────────────────────────────────────────────────────
if uploaded:
    df = run_kpis(uploaded)
    traffic = kpi_traffic_lights(df)
    segs = segment_fans(df)

    st.subheader("Key Insights")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Churn %", traffic["churn_pct"])
    col2.metric("HHI", traffic["hhi"])
    col3.metric("CVE", traffic["cve"])
    col4.metric("Whales Share %", segs["whales_share"])

    st.divider()

    if st.button("📄 Download 2-page PDF"):
        pdf_bytes = build_pdf_lazy(df, traffic, segs)
        st.download_button(
            "Save Report",
            data=pdf_bytes,
            file_name="RevenueLeakSnapshot.pdf",
            mime="application/pdf",
        )
