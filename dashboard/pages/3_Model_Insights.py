import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv(
    "data/processed/train.csv"
)
fig = px.histogram(
    df,
    x="Churn Value"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
fig = px.bar(
    df,
    x="Contract",
    color="Churn Value"
)

st.plotly_chart(
    fig
)
fig = px.box(
    df,
    x="Churn Value",
    y="CLTV"
)

st.plotly_chart(
    fig
)
