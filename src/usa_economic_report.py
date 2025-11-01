"""
Automated Economic Report Generator
-----------------------------------
Generates a professional PDF summary of the U.S. Economic Trend Analysis (2020–2025),
including GDP growth, inflation, unemployment, and correlations between key indicators.

Author: [Your Name]
GitHub: [your_github_link]
"""

import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from datetime import datetime

# ==============================
#  PDF Report Generator
# ==============================
def generate_us_economic_report():
    # Ensure output directory exists
    os.makedirs("results", exist_ok=True)

    # PDF file path
    report_path = "results/us_economic_report_2025.pdf"

    # Initialize document
    doc = SimpleDocTemplate(report_path, pagesize=A4)
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        name="TitleStyle",
        parent=styles["Title"],
        fontSize=18,
        textColor="#003366",
        alignment=1,
        spaceAfter=20
    )

    subtitle_style = ParagraphStyle(
        name="Subtitle",
        parent=styles["Heading2"],
        textColor="#004c99",
        spaceAfter=10
    )

    normal = styles["Normal"]

    # PDF content
    content = []

    # Title
    content.append(Paragraph("📊 United States Economic Trends Report (2020–2025)", title_style))
    content.append(Paragraph(f"Generated on {datetime.now().strftime('%B %d, %Y')}", normal))
    content.append(Spacer(1, 12))

    # Overview
    overview_text = """
    This report provides a brief statistical overview of the United States economy 
    between 2020 and 2025, using dummy data designed to resemble realistic macroeconomic trends. 
    The analysis explores GDP growth, inflation, unemployment rates, and interest rates.
    """
    content.append(Paragraph(overview_text, normal))
    content.append(Spacer(1, 12))

    # Add chart image (from your analysis script)
    chart_path = "results/us_gdp_trend.png"
    if os.path.exists(chart_path):
        content.append(Paragraph("Figure 1. U.S. GDP Trend and Regression (2020–2025)", subtitle_style))
        content.append(Image(chart_path, width=6.0 * inch, height=3.5 * inch))
        content.append(Spacer(1, 12))
    else:
        content.append(Paragraph("⚠️ Chart image not found. Please run the analysis script first.", normal))
        content.append(Spacer(1, 12))

    # Key Insights
    insights = """
    <b>Key Observations:</b><br/>
    • Total GDP increased steadily over the period, reflecting a strong post-pandemic recovery.<br/>
    • Inflation peaked around 2022 and stabilized near 3% by 2025.<br/>
    • The unemployment rate decreased gradually, suggesting improving labor market conditions.<br/>
    • The correlation between inflation and interest rates was positive, 
      consistent with typical Federal Reserve monetary responses.<br/>
    <br/>
    <b>Regression Summary:</b><br/>
    The linear regression model indicates a clear upward GDP trend, 
    suggesting continuous economic expansion through 2025.
    """
    content.append(Paragraph(insights, normal))
    content.append(Spacer(1, 18))

    # Conclusion
    conclusion = """
    <b>Conclusion:</b><br/>
    The simulated U.S. economy shows sustainable growth, moderate inflation, 
    and decreasing unemployment, which together signal strong macroeconomic stability 
    for the 2025 outlook.
    """
    content.append(Paragraph(conclusion, normal))

    # Build the PDF
    doc.build(content)

    print(f"✅ PDF report generated successfully: {report_path}")


if __name__ == "__main__":
    generate_us_economic_report()
