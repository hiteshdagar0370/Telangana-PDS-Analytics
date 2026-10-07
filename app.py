import streamlit as st
 
st.title("Telangana PDS Analytics Dashboard")
 
st.write("Shop Performance Clustering Dashboard")
 
uploaded_file = st.file_uploader("Upload Clustered CSV", type="csv")
 
if uploaded_file:
import pandas as pd
 
df = pd.read_csv(uploaded_file)
 
st.dataframe(df.head())
 
if "Cluster" in df.columns:
st.bar_chart(df["Cluster"].value_counts())
