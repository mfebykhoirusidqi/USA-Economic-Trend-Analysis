"""
US Economic Trend Analysis (2020–2025)
--------------------------------------
This project performs a statistical analysis and visualization
of dummy macroeconomic data for the United States, focusing on GDP trends,
inflation, unemployment rate, and interest rate relationships.

Author: [Your Name]
GitHub: [your_github_link]
"""

import os
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from statistic_manual import mean, correlation, linear_regression


# ============================================
# 1️⃣ Load Dummy Dataset
# ============================================
# The dataset should contain columns:
# Year, GDP (Trillion USD), Inflation (%), Unemployment (%), Interest Rate (%)

data = np.genfromtxt("data/dummy_data_usa.csv", delimiter=",", skip_header=1)

year = data[:, 0]
gdp = data[:, 1]
inflation = data[:, 2]
unemployment = data[:, 3]
interest_rate = data[:, 4]


# ============================================
# 2️⃣ Statistical Analysis
# ============================================
gdp_growth_rate = (gdp[-1] - gdp[0]) / gdp[0] * 100
corr_inflation_interest = correlation(inflation, interest_rate)
corr_gdp_unemployment = correlation(gdp, unemployment)
b0, b1 = linear_regression(year, gdp)

print("===== US Economic Trend Analysis (2020–2025) =====")
print(f"Total GDP Growth          : {gdp_growth_rate:.2f}%")
print(f"Correlation (Inflation vs Interest Rate): {corr_inflation_interest:.3f}")
print(f"Correlation (GDP vs Unemployment)      : {corr_gdp_unemployment:.3f}")
print(f"Linear Regression Equation (GDP)       : GDP = {b0:.2f} + {b1:.2f} × Year")


# ============================================
# 3️⃣ Visualization: GDP Trend & Linear Regression
# ============================================
predicted_gdp = b0 + b1 * year

plt.figure(figsize=(9, 6))
plt.plot(year, gdp, "o-", label="Actual GDP (Trillion USD)", color="#0077b6")
plt.plot(year, predicted_gdp, "r--", label="Linear Regression (Predicted GDP)")
plt.title("📈 United States GDP Trend (2020–2025)", fontsize=14)
plt.xlabel("Year")
plt.ylabel("GDP (Trillion USD)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# Ensure the results folder exists
os.makedirs("results", exist_ok=True)

plt.savefig("results/us_gdp_trend.png", dpi=300)
plt.show()

print("\n✅ Figure saved successfully: results/us_gdp_trend.png")
