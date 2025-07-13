from io import BytesIO
from reportlab.lib.pagesizes import LETTER
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from branding import COLOR_PRIMARY

def build_pdf(df, traffic, segs):
    buf = BytesIO()
    c   = canvas.Canvas(buf, pagesize=LETTER)
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(COLOR_PRIMARY)
    c.drawString(40, 750, "Revenue-Leak Scanner – Snapshot")

    c.setFont("Helvetica", 12)
    y = 700
    for label, val in [
        ("Churn %",         f"{traffic['churn_pct']} %"),
        ("Diversification", traffic['hhi']),
        ("Content Velocity",traffic['cve']),
        ("Whales Share",    f"{segs['whales_share']} %")
    ]:
        c.drawString(40, y, f"{label}: {val}")
        y -= 25

    y -= 20
    c.drawString(40, y, "Fan Segments:")
    y -= 15
    total = sum(segs['seg_counts'].values())
    x0    = 40
    for cl, ct in segs['seg_counts'].items():
        width = 400*(ct/total)
        c.setFillColor(colors.green if cl==0 else colors.orange if cl==1 else colors.red)
        c.rect(x0, y, width, 14, stroke=0, fill=1)
        x0 += width
    c.showPage()
    c.setFillColor(COLOR_PRIMARY)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(40, 750, "Next Steps")
    c.setFont("Helvetica", 11)
    c.setFillColor(colors.black)
    c.drawString(40, 720, "• Schedule a FREE strategy call to unlock the full 300-point audit")
    c.drawString(40, 700, "• Get personalized revenue-growth blueprints and chat scripts")
    c.save()
    pdf = buf.getvalue()
    buf.close()
    return pdf
