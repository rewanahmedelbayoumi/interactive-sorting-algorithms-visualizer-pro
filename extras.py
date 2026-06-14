import winsound
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def play_sound(action):
    try:
        if action == "swap":
            winsound.Beep(800, 50)
        elif action == "compare":
            winsound.Beep(400, 20)
    except:
        pass

def export_report(comps, swaps, elapsed):
    doc = SimpleDocTemplate("sorting_report.pdf")
    styles = getSampleStyleSheet()

    content = []
    content.append(Paragraph("Sorting Visualizer Report", styles["Title"]))
    content.append(Paragraph(f"Comparisons: {comps}", styles["Normal"]))
    content.append(Paragraph(f"Swaps: {swaps}", styles["Normal"]))
    content.append(Paragraph(f"Time: {elapsed}s", styles["Normal"]))

    doc.build(content)