import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="SmartStock – Simple Inventory Dashboard", layout="wide")

st.title("📦 SmartStock – Simple Inventory Optimization")

st.write("Upload your dataset named **Inventory_Dataset.csv** or upload a CSV manually.")

# ---- FILE LOAD ----
uploaded = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
else:
    try:
        df = pd.read_csv("Inventory_Dataset.csv")
        st.info("Loaded local file: Inventory_Dataset.csv")
    except:
        st.warning("Please upload a dataset to proceed.")
        st.stop()

st.subheader("Preview of Data")
st.dataframe(df.head())

# ---- AUTO DETECT COLUMNS ----
possible_date = [c for c in df.columns if "date" in c.lower()]
possible_product = [c for c in df.columns if "product" in c.lower() or "item" in c.lower() or "sku" in c.lower()]
possible_qty = [c for c in df.columns if "qty" in c.lower() or "quantity" in c.lower()]
possible_stock = [c for c in df.columns if "stock" in c.lower()]

date_col = st.selectbox("Select Date Column", possible_date)
product_col = st.selectbox("Select Product/SKU Column", possible_product)
qty_col = st.selectbox("Select Quantity Sold Column", possible_qty)
stock_col = st.selectbox("Select Current Stock Column (optional)", ["None"] + possible_stock)

df[date_col] = pd.to_datetime(df[date_col])
df[qty_col] = pd.to_numeric(df[qty_col], errors="coerce").fillna(0)

if stock_col != "None":
    df[stock_col] = pd.to_numeric(df[stock_col], errors="coerce")

# ---- BASIC METRICS ----
st.header("📊 Key Metrics")

total_sales = df[qty_col].sum()
unique_items = df[product_col].nunique()
top_item = df.groupby(product_col)[qty_col].sum().idxmax()

col1, col2, col3 = st.columns(3)
col1.metric("Total Units Sold", int(total_sales))
col2.metric("Unique Products", unique_items)
col3.metric("Top Selling Item", top_item)

# ---- VISUAL 1: SALES TREND ----
st.header("📈 Sales Trend Over Time")

daily_sales = df.groupby(date_col)[qty_col].sum()

st.line_chart(daily_sales)

# ---- VISUAL 2: TOP SELLING PRODUCTS ----
st.header("🏆 Top 10 Selling Products")

top10 = df.groupby(product_col)[qty_col].sum().sort_values(ascending=False).head(10)

st.bar_chart(top10)

# ---- VISUAL 3: INVENTORY VS SALES ----
if stock_col != "None":
    st.header("📦 Inventory vs Sales (Per Product)")

    inventory_vs_sales = df.groupby(product_col).agg(
        total_sold=(qty_col, "sum"),
        stock=(stock_col, "last")
    )

    st.bar_chart(inventory_vs_sales)

# ---- SIMPLE REORDER SUGGESTIONS ----
st.header("🔔 Simple Reorder Suggestions")

if stock_col != "None":
    reorder_df = df.groupby(product_col).agg(
        sold_7_days=(qty_col, lambda x: x.tail(7).sum()),
        current_stock=(stock_col, "last")
    )

    reorder_df["needs_reorder"] = reorder_df["current_stock"] < reorder_df["sold_7_days"]

    st.write("Products needing reorder (stock < last 7 days sales):")
    st.dataframe(reorder_df[reorder_df["needs_reorder"] == True])

else:
    st.info("No stock column selected — reorder suggestions skipped.")

st.success("")
