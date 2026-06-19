# 📈 Mutual Fund Analytics & Performance Dashboard

An end-to-end Mutual Fund Analytics platform built using **Python, SQL, SQLite, and Power BI** to analyze mutual fund performance, calculate financial metrics, and generate business insights through interactive dashboards.

---

## 🚀 Project Overview

The objective of this project is to ingest and process mutual fund NAV data from AMFI, perform financial analysis, and create an interactive dashboard that helps investors and analysts understand fund performance, risk, and returns.

The project demonstrates:

* Data ingestion and ETL pipelines
* Database design and SQL analytics
* Financial metric calculations
* Interactive Power BI dashboard development
* Business insight generation

---

## 🏗️ Project Architecture

```text
AMFI NAV Data
      ↓
Python ETL Pipeline
      ↓
SQLite Database
      ↓
Financial Metrics Engine
      ↓
Dashboard Dataset
      ↓
Power BI Dashboard
      ↓
Business Insights
```

---

## 🛠️ Tech Stack

### Programming & Analytics

* Python
* Pandas
* NumPy

### Database

* SQLite
* SQL

### Visualization

* Power BI
* Matplotlib
* Plotly

### Tools

* Jupyter Notebook
* Git
* GitHub

---

## 📂 Project Structure

```text
Mutual_Fund_Analytics/
│
├── data/
│   ├── raw/
│   │   └── NAVAll.csv
│   │
│   └── processed/
│       ├── nav_history.csv
│       ├── schemes.csv
│       ├── top_funds.csv
│       └── dashboard_data.csv
│
├── database/
│   └── nifty100.db
│
├── src/
│   ├── ingestion.py
│   ├── create_schemes.py
│   ├── create_database.py
│   ├── select_funds.py
│   ├── generate_historical_nav.py
│   ├── metrics.py
│   └── dashboard_dataset.py
│
├── dashboard/
│   └── Mutual_Fund_Analytics.pbix
│
├── reports/
│   └── images/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📊 Dataset

### Source

Association of Mutual Funds in India (AMFI)

### Files Used

* NAVAll.csv
* nav_history.csv
* schemes.csv
* top_funds.csv
* dashboard_data.csv

### Data Size

* 14,000+ Mutual Fund Schemes
* 90,000+ Historical NAV Records

---

## ⚙️ ETL Workflow

### Step 1

Download NAV data from AMFI.

### Step 2

Clean and transform raw text data.

### Step 3

Generate structured datasets.

### Step 4

Load data into SQLite database.

### Step 5

Generate historical NAV dataset.

### Step 6

Compute financial metrics.

### Step 7

Build Power BI dashboards.

---

## 📈 Financial Metrics Implemented

### Daily Return

Measures day-to-day change in NAV.

### CAGR (Compound Annual Growth Rate)

Measures annualized investment growth.

### Volatility

Measures risk using the standard deviation of returns.

### Sharpe Ratio

Measures risk-adjusted return.

### Maximum Drawdown

Measures the maximum decline from peak NAV.

---

## 📊 Dashboard Pages

### Page 1 – Executive Summary

* KPI Cards
* Top 10 Funds by CAGR
* Fund Category Distribution
* Risk Distribution
* Top Funds Table
* Business Insights

### Page 2 – NAV Trend & Fund Performance

* Date Slicer
* Fund Selector
* Average NAV
* Highest NAV
* Lowest NAV
* NAV Trend Analysis
* Category Performance
* Top Performing Funds

### Page 3 – Risk & Return Analysis

* Risk vs Return Scatter Plot
* Average Return
* Average Volatility
* Average Sharpe Ratio
* Top Funds by Sharpe Ratio
* Lowest Drawdown Funds
* Fund Metrics Table

---

## 💡 Key Business Insights

* Index funds exhibited strong long-term growth trends.
* Medium-risk funds dominated the portfolio.
* Funds with higher Sharpe ratios provided superior risk-adjusted returns.
* Debt funds generally demonstrated lower volatility.
* Top-performing funds significantly outperformed category averages.

---

## ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/prasadsunkara11/Mutual_Fund_Analytics.git
cd Mutual_Fund_Analytics
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run ETL Pipeline

```bash
python src/ingestion.py
python src/create_schemes.py
python src/create_database.py
python src/select_funds.py
python src/generate_historical_nav.py
python src/metrics.py
python src/dashboard_dataset.py
```

---

## 🎯 Skills Demonstrated

* Python Programming
* Data Cleaning and Transformation
* ETL Pipeline Development
* SQL and Database Design
* Financial Analytics
* Time Series Analysis
* Data Visualization
* Power BI Dashboard Development
* Business Intelligence Reporting
* Git and GitHub

---

## 🔮 Future Improvements

* Integration with live AMFI APIs
* Benchmark comparison with NIFTY indices
* Automated data refresh pipeline
* Portfolio optimization module
* Predictive analytics and fund recommendation engine

---

## 👨‍💻 Author

**Sunkara Prasad**

B.Tech Computer Science Engineering Student

GitHub: https://github.com/prasadsunkara11

LinkedIn: Add your LinkedIn profile link here.
