# USA-Economic-Trend-Analysis
This project simulates an economic analysis of the **United States (2020–2025)** using dummy data that reflects realistic post-pandemic conditions — GDP growth, inflation spikes, unemployment trends, and interest rate policy shifts by the Federal Reserve.


# USA Economic Trend Analysis (2020–2025)
> **Live Analytics Dashboard and Automated Economic Report using Pure Python, NumPy, Matplotlib, and Streamlit**

📈 Output Samples
GDP Regression (2020–2025)
<img width="2700" height="1800" alt="us_gdp_trend" src="https://github.com/user-attachments/assets/46110df9-09ca-437c-b327-665c3b330663" />
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/mfebykhoirusidqi/USA-Economic-Trend-Analysis)](https://github.com/mfebykhoirusidqi/USA-Economic-Trend-Analysis/commits/main)

---
## 🎥 Live Demo
> Experience the interactive analytics dashboard directly without running the code.

🎬 **Dashboard Video Preview:**  
[![Watch the video](results/dashboard_preview.png)](https://github.com/mfebykhoirusidqi/USA-Economic-Trend-Analysis/assets/your-video-link.mp4)

🖥️ **Streamlit Dashboard Screenshot:**
<img width="1366" height="768" alt="Screenshot (264)" src="https://github.com/user-attachments/assets/ffff3da1-ec32-4170-9252-5abcaafab6d6" />
<img width="1366" height="768" alt="Screenshot (265)" src="https://github.com/user-attachments/assets/b24fb8fe-af43-4727-99d9-a0ff7410ced6" />
<img width="1366" height="768" alt="Screenshot (266)" src="https://github.com/user-attachments/assets/93ab1e3f-868f-47ce-bed8-503d6a1d06b8" />
<img width="1366" height="768" alt="Screenshot (267)" src="https://github.com/user-attachments/assets/5e1febba-4a7c-4627-bf04-f308e8ffd9d4" />
---

## 📊 Overview
This project presents a **data-driven analysis of U.S. economic trends (2020–2025)** using **pure Python and NumPy**.  
It demonstrates professional data workflow design — from raw data processing to visualization, report generation, and live dashboard deployment.

The analysis focuses on **four key macroeconomic indicators**:
- GDP Growth  
- Inflation Rate  
- Interest Rate  
- Unemployment Rate  

📘 Outputs include:
- **Analytical visualizations (Matplotlib)**
- **Statistical correlations & regression results**
- **Automated PDF report (`ReportLab`)**
- **Interactive Streamlit dashboard**

---

## 🧠 Theoretical Framework

Economic trend analysis explores how key financial variables evolve and interact.  
This project applies classical macroeconomic theories:

| Theory | Description |
|--------|--------------|
| **Phillips Curve** | Inflation tends to rise when unemployment falls. |
| **Okun’s Law** | GDP growth and unemployment have a negative correlation. |
| **Interest-Inflation Link** | Central banks raise interest rates to stabilize inflation. |

📈 **Findings (Dummy Dataset):**
- GDP increased steadily by ~18% between 2020–2025.  
- Inflation and interest rate show **moderate positive correlation**.  
- GDP and unemployment exhibit **strong negative correlation**, consistent with Okun’s Law.

---

## 📂 Project Structure
```bash
USA-Economic-Trend-Analysis/
│
├── data/
│   └── dummy_data_usa.csv              # Simulated U.S. economic dataset
│
├── results/
│   ├── grafik_tren_usa.png             # GDP trend regression chart
│   ├── us_gdp_trend.png                # Supporting visualization
│   ├── us_economic_report_2025.pdf     # Auto-generated PDF report
│   ├── streamlit_dashboard.png         # Dashboard screenshot
│   └── dashboard_preview.mp4           # Dashboard demo video
│
├── src/
│   ├── statistic_manual.py             # Custom statistical functions
│   ├── usa_economic_trend_analysis.py  # Main analysis pipeline
│   ├── usa_economic_report.py          # PDF generator
│   └── dashboard_economic_tren_usa.py  # Streamlit dashboard app
│
├── requirements.txt                    # Dependencies
└── README.md                           # Documentation


⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/mfebykhoirusidqi/USA-Economic-Trend-Analysis.git
cd USA-Economic-Trend-Analysis

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Analysis & Generate Outputs
python src/usa_economic_trend_analysis.py
python src/usa_economic_report.py

4️⃣ Launch Dashboard
streamlit run src/dashboard_economic_tren_usa.py


Access the dashboard at 👉 http://localhost:8501


🧰 Tools & Technologies
Category	Tools
Programming	Python 3.11+, NumPy
Visualization	Matplotlib, Streamlit
Reporting	ReportLab
Environment	Virtualenv
Version Control	Git + GitHub
🌍 Applications

Economic data modeling and visualization

Financial forecasting prototyping

Data science and statistical teaching tools

Portfolio project for Python/AI developers

👨‍💻 Author

Muhammad Feby Khoirul Sidqi

Data Enggineer · AI Research Enthusiast · Python Developer . Education Research

🌐 GitHub : https://github.com/mfebykhoirusidqi
📧 mfebykhoirus@gmail.com
