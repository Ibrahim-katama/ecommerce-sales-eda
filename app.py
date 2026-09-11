import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config ( page_title="E-Commerce EDA Dashboard", layout="wide" )


# Cache data loading so it doesn't reload on every click
@st.cache_data
def load_data():
    return pd.read_csv ( "data/cleaned_sales.csv" )
df = load_data ()

st.title ( "_E-Commerce Sales Performance Dashboard_" )
st.sidebar.header ( "Filter Data" )
categories = st.sidebar.multiselect (
    "Select Categories:",
    options=df["category"].unique (),
    default=df["category"].unique ()
)

filtered_df = df[df["category"].isin ( categories )]

col1, col2, col3 = st.columns ( 3 )
col1.metric ( "Total Revenue", f"${filtered_df['sales'].sum ():,.2f}" )
col2.metric ( "Total Orders", f"{len ( filtered_df ):,}" )
col3.metric ( "Avg Order Value", f"${filtered_df['sales'].mean ():,.2f}" )

st.markdown ( "---" )

row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader ( "1. Category Revenue Breakdown" )
    fig1, ax1 = plt.subplots ( figsize=(6, 4) )
    sns.barplot (
        data=filtered_df,
        x="category",
        y="sales",
        hue="category",
        legend=False,
        estimator=sum,
        errorbar=None,
        ax=ax1,
        palette="Blues_d"
    )
    ax1.set_xlabel ("Category")
    ax1.set_ylabel ("Total Sales ($)")
    plt.xticks (rotation=30)
    plt.grid (axis="y", linestyle="--", alpha=0.5)
    st.pyplot (fig1)

with row1_col2:
    st.subheader ( "2. Price vs. Rating Dynamics" )
    fig2, ax2 = plt.subplots ( figsize=(6, 4) )
    sns.regplot (
        data=filtered_df,
        x="price",
        y="customer_rating",
        scatter_kws={"alpha": 0.5, "color": "#1f77b4"},
        line_kws={"color": "crimson", "linewidth": 2},
        ax=ax2
    )
    ax2.set_xlabel ( "Product Price ($)" )
    ax2.set_ylabel ( "Customer Rating (0-10)" )
    plt.grid ( True, linestyle="--", alpha=0.5 )
    st.pyplot ( fig2 )

row2_col1, row2_col2 = st.columns ( 2 )

with row2_col1:
    st.subheader ( "3. Rating Spread per Category" )
    fig3, ax3 = plt.subplots ( figsize=(6, 4) )
    sns.boxplot (
        data=filtered_df,
        x="category",
        y="customer_rating",
        hue="category",
        legend=False,
        palette="Set2",
        ax=ax3
    )
    ax3.set_xlabel ( "Category" )
    ax3.set_ylabel ( "Customer Rating (0-10)" )
    plt.xticks ( rotation=30 )
    plt.grid ( axis="y", linestyle="--", alpha=0.5 )
    st.pyplot ( fig3 )

with row2_col2:
    st.subheader ("4. Monthly Revenue Performance by Category")
    fig4, ax4 = plt.subplots (figsize=(6, 4))

    if "month" in filtered_df.columns:
        monthly_cat_sales = (
            filtered_df.groupby ( ["month", "category"] )["sales"]
            .sum ()
            .reset_index ()
        )
        sns.barplot (
            data=monthly_cat_sales,
            x="month",
            y="sales",
            hue="category",
            palette="Set2",
            ax=ax4
        )
        ax4.set_xlabel ( "Month" )
        ax4.set_ylabel ( "Total Revenue ($)" )
        plt.xticks ( rotation=30 )
        plt.grid ( axis="y", linestyle="--", alpha=0.5 )
        ax4.legend ( title="Category", bbox_to_anchor=(1.05, 1), loc="upper left" )

    st.pyplot ( fig4 )