import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

st.title("Dashboard")
df = sns.load_dataset("Titanic")
#to display dataset
st.dataframe(df)


#gender filter
gender_filter=st.sidebar.multiselect("Gender",options = df["sex"].unique(),default=df["sex"].unique())
filtered_df=df[
    (df["sex"].isin(gender_filter))
]

#pclass filter
pclass_filter= st.sidebar.multiselect("Passenger Class",options=df["pclass"].unique(),default = df["pclass"].unique())



fig = px.histogram(filtered_df, x='age',color='sex', facet_col='survived',
              title='age distribution by gender and survived',
              
              template='plotly_dark',width=800)
 

st.plotly_chart(fig)
st.markdown("This graph shows age distribution by gender and survived ")


fig = px.scatter(filtered_df,x='age',y='fare', color='survived', title='Age vs Fare by Survival',
           template='plotly_dark', width=809)

st.plotly_chart(fig)
st.markdown("This graph shows age vs fare by survival ")



fig = px.sunburst(filtered_df, path=['pclass','sex','survived'],
            title='Survived by class and gender', template='plotly_dark',
            width=800)

st.plotly_chart(fig)
st.markdown("This graph shows survived by class and gender ")

