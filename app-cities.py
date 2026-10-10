from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

plt.style.use("seaborn-v0_8")
st.set_page_config(page_title="World Cities", layout="wide")
st.title("World Cities")


@st.cache_data
def load_data():
    data = pd.read_csv(Path(__file__).with_name("worldcities.csv"))
    data["capital"] = data["capital"].fillna("Not a capital")
    return data


df = load_data()
population_filter = st.slider("Minimal Population (Millions):", 0.0, 40.0, 3.6)
capital_options = df["capital"].unique().tolist()
capital_filter = st.sidebar.multiselect(
    "Capital Selector", capital_options, default=capital_options
)

if "applied_country" not in st.session_state:
    st.session_state.applied_country = "ALL"
with st.sidebar.form("country_form"):
    country_input = st.text_input("Country Name (enter ALL to reset)", "ALL")
    if st.form_submit_button("Apply"):
        st.session_state.applied_country = country_input.strip()

df = df[
    (df["population"] >= population_filter)
    & df["capital"].isin(capital_filter)
].copy()
country_filter = st.session_state.applied_country
if country_filter.casefold() != "all":
    df = df[df["country"].str.casefold() == country_filter.casefold()]

st.caption(f"{len(df):,} cities • Population in millions")
if df.empty:
    st.info("No cities match these filters. Lower the population, select a capital category, or enter ALL.")
else:
    st.map(df, latitude="lat", longitude="lon")

st.subheader("City Details:")
st.dataframe(df[["city", "country", "population"]], hide_index=True)
st.subheader("Total Population By Country")
if not df.empty:
    fig, ax = plt.subplots(figsize=(20, 5))
    pop_sum = df.groupby("country")["population"].sum()
    pop_sum.plot.bar(ax=ax)
    ax.set_ylabel("Population (millions)")
    ax.set_xlabel("Country")
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
