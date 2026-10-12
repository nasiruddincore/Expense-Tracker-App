import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="FinTech Expense Tracker", page_icon="💰", layout="wide")

# --- DATA LOADING & CLEANING ---
@st.cache_data
def load_data():
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "expenses.csv")
    if not os.path.exists(file_path):
        return pd.DataFrame()
    
    df = pd.read_csv(file_path)
    
    # Cleaning & Feature Engineering
    df.dropna(inplace=True)
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.month_name()
    df["Month_Num"] = df["Date"].dt.month
    df["Category"] = df["Category"].str.title()
    
    return df.sort_values(by="Date")

df = load_data()

if df.empty:
    st.error("⚠️ Dataset not found. Please run `python data/generate_data.py` first.")
    st.stop()

# --- SIDEBAR FILTERS ---
st.sidebar.header("🔍 Filter Options")
selected_month = st.sidebar.multiselect("Select Month", df["Month"].unique(), default=df["Month"].unique())
selected_type = st.sidebar.selectbox("Transaction Type", ["All", "Expense", "Income"])

filtered_df = df[df["Month"].isin(selected_month)]
if selected_type != "All":
    filtered_df = filtered_df[filtered_df["Type"] == selected_type]

# --- KPI METRICS ---
st.title("💰 Personal Finance & Expense Tracker")
st.markdown("Analyze your spending habits, categorize expenses, and track monthly financial health.")

total_income = df[df["Type"] == "Income"]["Amount"].sum()
total_expense = df[df["Type"] == "Expense"]["Amount"].sum()
balance = total_income - total_expense

col1, col2, col3 = st.columns(3)
col1.metric("Total Income", f"${total_income:,.2f}")
col2.metric("Total Expenses", f"${total_expense:,.2f}", delta="- Outflow", delta_color="inverse")
col3.metric("Net Balance", f"${balance:,.2f}")

st.divider()

# --- VISUALIZATIONS ---
colA, colB = st.columns(2)

with colA:
    st.subheader("🍕 Spending by Category")
    expense_data = filtered_df[filtered_df["Type"] == "Expense"]
    if not expense_data.empty:
        fig_pie = px.pie(expense_data, values="Amount", names="Category", hole=0.4, 
                         color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig_pie, use_container_width=True)
    else:
        st.info("No expense data for this selection.")

with colB:
    st.subheader("📈 Monthly Trend")
    trend_data = filtered_df.groupby(["Month_Num", "Month", "Type"])["Amount"].sum().reset_index()
    trend_data = trend_data.sort_values("Month_Num")
    
    if not trend_data.empty:
        fig_line = px.line(trend_data, x="Month", y="Amount", color="Type", markers=True,
                           color_discrete_map={"Income": "green", "Expense": "red"})
        st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.info("No trend data for this selection.")

# --- DATA TABLE ---
st.subheader("📋 Raw Transaction Data")
st.dataframe(filtered_df.drop(columns=["Month_Num"]), use_container_width=True)