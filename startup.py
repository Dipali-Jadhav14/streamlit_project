import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- Page Config ----------------
st.set_page_config(page_title="Startup Funding Analysis", layout="wide")

# ---------------- Load Data ----------------
@st.cache_data
def load_data():
    df = pd.read_csv("startup_cleaned.csv")

    # convert date to datetime and extract year
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['year'] = df['date'].dt.year

    return df

df = load_data()

# ---------------- Sidebar ----------------
st.sidebar.title(" Analysis Panel")

analysis_type = st.sidebar.selectbox(
    "Select One",
    [
        "Overall Analysis",
        "Year-wise Analysis",
        "City-wise Analysis",
        "Startup-wise Analysis"
    ]
)

startup_selected = None
if analysis_type == "Startup-wise Analysis":
    startup_selected = st.sidebar.selectbox(
        "Select Startup",
        sorted(df['startup'].dropna().unique())
    )

# ---------------- Overall Analysis ----------------
if analysis_type == "Overall Analysis":

    st.title(" Overall Startup Funding Analysis")

    col1, col2, col3 = st.columns(3)

    col1.metric(" Total Startups", df['startup'].nunique())
    col2.metric(" Total Funding", f"{df['amount'].sum():,.0f}")
    col3.metric("Average Funding", f"{df['amount'].mean():,.0f}")

    st.subheader("Year-wise Funding Trend")

    year_funding = df.groupby("year")["amount"].sum()

    fig, ax = plt.subplots()
    ax.plot(year_funding.index, year_funding.values, marker='o')
    ax.set_xlabel("Year")
    ax.set_ylabel("Funding Amount")
    ax.set_title("Funding Trend Over Years")

    st.pyplot(fig)

# ---------------- Year-wise Analysis ----------------
elif analysis_type == "Year-wise Analysis":

    st.title(" Year-wise Analysis")

    year = st.selectbox(
        "Select Year",
        sorted(df['year'].dropna().unique())
    )

    year_df = df[df['year'] == year]

    st.metric(
        "Total Funding",
        f"{year_df['amount'].sum():,.0f}"
    )

    st.subheader(" Top 10 Startups")

    top_startups = (
        year_df.groupby("startup")["amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.bar_chart(top_startups)

# ---------------- City-wise Analysis ----------------
elif analysis_type == "City-wise Analysis":

    st.title("🏙️ City-wise Funding Analysis")

    city_funding = (
        df.groupby("city")["amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.subheader("Top 10 Cities by Funding")
    st.bar_chart(city_funding)

# ---------------- Startup-wise Analysis ----------------
elif analysis_type == "Startup-wise Analysis":

    st.title(f" Startup Analysis: {startup_selected}")

    startup_df = df[df['startup'] == startup_selected]

    col1, col2 = st.columns(2)

    col1.metric(
        "Total Funding",
        f"{startup_df['amount'].sum():,.0f}"
    )
    col2.metric(
        "Funding Rounds",
        startup_df.shape[0]
    )

    st.subheader("Funding Over Years")
    st.bar_chart(
        startup_df.groupby("year")["amount"].sum()
    )

    st.subheader("Funding Details")
    st.dataframe(startup_df)
