import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

st.title("Dashboard")
df = sns.load_dataset("Titanic")
st.dataframe(df)

fig = px.histogram(df, x='age',color='sex', facet_col='survived',
              title='age distribution by gender and survived',
              
              template='plotly_dark',width=800)
 

st.plotly_chart(fig)