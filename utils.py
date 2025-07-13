import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# ── KPI helpers ───────────────────────────────────────────────────────
def run_kpis(csv_file):
    df = pd.read_csv(csv_file)
    df["date"] = pd.to_datetime(df["date"])
    return df

def kpi_traffic_lights(df):
    mrr = df[df.type == "subscription"].groupby("date").revenue.sum()
    churn = 100 * (
        mrr.diff().fillna(0).clip(lower=0) / mrr.shift(1).replace(0, np.nan)
    ).mean()
    hhi = (df.groupby("fan_id").revenue.sum() ** 2).sum() / df.revenue.sum() ** 2
    cve = df.shape[0] / df["fan_id"].nunique()
    return {"churn_pct": round(churn, 1), "hhi": round(hhi, 3), "cve": round(cve, 2)}

def segment_fans(df):
    spend = df.groupby("fan_id").revenue.sum().to_frame("spend")
    k = min(3, len(spend))
    labels = KMeans(n_clusters=k, n_init="auto", random_state=42).fit_predict(spend)
    spend["cluster"] = labels
    whales = spend.sort_values("spend", ascending=False).head(max(1, int(0.05 * len(spend))))
    return {
        "whales_share": round(100 * whales.spend.sum() / spend.spend.sum(), 1),
        "seg_counts": spend.cluster.value_counts().to_dict(),
    }

# ── PDF wrapper (lazy import) ─────────────────────────────────────────
def build_pdf_lazy(df, traffic, segs):
    from pdf_report import build_pdf  # imported only when user clicks
    return build_pdf(df, traffic, segs)
