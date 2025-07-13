from io import BytesIO
from reportlab.lib.pagesizes import LETTER
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from branding import COLOR_PRIMARY

def build_pdf(df, traffic, segs):
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=LETTER)
    # Page 1
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(COLOR_PRIMARY)
    c.drawString(40, 750, "Revenue-Leak Scanner  –  Snapshot")
    c.setFont("Helvetica", 12)
    y = 700
    for label, val in [
        ("Churn %",          f"{traffic['churn_pct']} %"),
        ("Diversification",  traffic["hhi"]),
        ("Content Velocity", traffic["cve"]),
        ("Whales Share %",   f"{segs['whales_share']} %"),
    ]:
        c.drawString(40, y, f"{label}: {val}")
        y -= 25

    # Segment bar
    y -= 20
    c.drawString(40, y, "Fan Segments:")
    y -= 15
    total = sum(segs["seg_counts"].values())
    x = 40
    for cl, ct in segs["seg_counts"].items():
        width = 400 * (ct / total)
        c.setFillColor(
            colors.green if cl == 0 else colors.orange if cl == 1 else colors.red
        )
        c.rect(x, y, width, 14, stroke=0, fill=1)
        x += width

    # Page 2
    c.showPage()
    c.setFillColor(COLOR_PRIMARY)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(40, 750, "Next Steps")
    c.setFont("Helvetica", 11)
    c.setFillColor(colors.black)
    c.drawString(40, 720, "• Book a FREE strategy call to unlock the 300-point audit.")
    c.drawString(40, 700, "• Receive custom revenue-growth blueprints and chat scripts.")
    c.save()
    pdf_bytes = buf.getvalue()
    buf.close()
    return pdf_bytes
