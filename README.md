# 💰 FinTech Expense Tracker App (Data Science Project)

An industry-oriented data science web application that allows users to track, categorize, and visualize their financial expenses. Built to simulate the core analytics engine behind platforms like Mint, CRED, and Splitwise.

## 📌 Problem Statement
Raw financial data—such as bank statements and digital receipts—is difficult to read and analyze manually. Users and businesses often lose track of categorical spending, leading to budget deficits, unnoticed subscription leaks, and poor financial forecasting. 

## 💡 Solution
This project ingests time-series transaction data, applies automated data cleaning using Pandas, and renders a real-time interactive dashboard. It provides instant visibility into cash flow, monthly trends, and spending categories, empowering users to make data-driven financial decisions.

## 🚀 Features
- **Automated Data Generation:** Includes a synthetic dataset generator simulating realistic human financial behavior (e.g., rent spikes, salary days, everyday expenses).
- **KPI Metrics:** Real-time calculation of Total Income, Total Expenses, and Net Balance.
- **Interactive Visualizations:** Plotly-powered pie charts for category breakdowns and line charts for temporal cash flow trends.
- **Dynamic Filtering:** Slice and dice financial data by month and transaction type dynamically.
- **Data Wrangling:** Automated handling of missing values, date-time casting, and string standardization.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Data Manipulation:** Pandas, NumPy
- **Data Visualization:** Plotly Express
- **Frontend Dashboard:** Streamlit

## 📂 Folder Structure
```text
Expense-Tracker-App/
│
├── data/
│   └── generate_data.py       # Script to create synthetic transaction data
│
├── src/
│   └── app.py                 # Main Streamlit dashboard application
│
├── assets/                    # Directory for portfolio screenshots
├── requirements.txt           # Python dependencies list
├── .gitignore                 # Files for Git to ignore
└── README.md                  # Project documentation

🏁 How to Run Locally

1. Clone the repository and navigate to the project directory:
Bash

git clone [https://github.com/YOUR_USERNAME/FinTech-Expense-Tracker-Data-Science.git](https://github.com/YOUR_USERNAME/FinTech-Expense-Tracker-Data-Science.git)
cd FinTech-Expense-Tracker-Data-Science

2. Create a virtual environment and install dependencies:
Bash

python -m venv venv
# On Windows: venv\Scripts\activate
# On Mac/Linux: source venv/bin/activate
pip install -r requirements.txt

3. Generate the synthetic dataset:
Bash

python data/generate_data.py

4. Launch the Streamlit dashboard:
Bash

streamlit run src/app.py

📸 Screenshots

(Add your screenshots to the assets/ folder and link them here)

    ![Dashboard Overview](assets/dashboard_top_kpis.png)

    ![Category Spending](assets/category_pie_chart.png)

    ![Monthly Trends](assets/monthly_trend_chart.png)

🔮 Future Improvements

    Database Integration: Swap the static CSV file for PostgreSQL for persistent, multi-session storage.

    Bank API Integration: Use the Plaid API to pull real, authenticated bank transactions.

    AI Categorization: Implement an NLP model to read raw transaction descriptions and automatically assign categories.

    Budgeting Alerts: Add threshold limits per category with visual warnings when exceeding 90% of the allocated budget.
