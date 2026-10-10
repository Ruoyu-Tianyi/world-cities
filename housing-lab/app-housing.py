from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_page_config(page_title="California Housing Data (1990)", layout="wide")
plt.style.use("seaborn-v0_8")
st.title("California Housing Data (1990) by Tianyi Zhou")


@st.cache_data
def load_data():
    return pd.read_csv(Path(__file__).with_name("housing.csv"))


def filter_districts(data, minimum_value, location_types, income_level):
    filtered = data[
        (data["median_house_value"] >= minimum_value)
        & data["ocean_proximity"].isin(location_types)
    ]
    if income_level == "Low":
        filtered = filtered[filtered["median_income"] <= 2.5]
    elif income_level == "Medium":
        filtered = filtered[
            (filtered["median_income"] > 2.5)
            & (filtered["median_income"] < 4.5)
        ]
    else:
        filtered = filtered[filtered["median_income"] >= 4.5]
    return filtered


data = load_data()
minimum_value = st.slider(
    "Minimal Median House Value", min_value=0, max_value=500001,
    value=200000, step=1, format="$%d",
)
st.subheader("See more filters in the sidebar:")
location_options = data["ocean_proximity"].unique().tolist()
location_types = st.sidebar.multiselect(
    "Choose the location type", location_options, default=location_options,
)
income_level = st.sidebar.radio("Choose income level", ["Low", "Medium", "High"])
st.sidebar.caption(
    "Income in $10,000 units: Low ≤ 2.5; Medium > 2.5 and < 4.5; High ≥ 4.5."
)
districts = filter_districts(data, minimum_value, location_types, income_level)
st.caption(f"{len(districts):,} matching districts")
if districts.empty:
    st.info("No districts match these filters. Lower the minimum house value or choose more location types.")
else:
    st.map(districts[["latitude", "longitude"]])

st.subheader("Median House Value Distribution")
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(districts["median_house_value"], bins=30, color="#2878a8", edgecolor="white")
ax.set_xlabel("Median house value (US dollars)")
ax.set_ylabel("Number of districts")
ax.ticklabel_format(axis="x", style="plain")
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)
