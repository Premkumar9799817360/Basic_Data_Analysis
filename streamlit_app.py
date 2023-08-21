
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Data Analysis", page_icon=":bar_chart:", layout="wide")

st.title("Data Analysis :bar_chart:")
st.markdown("##")
upload = st.file_uploader("Upload Your Dataset (In CSV Format)")

if upload is not None:
    data = pd.read_csv(upload)


if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
if upload is not None:
     if st.checkbox("DataType of Each Column"):
        st.text("DataTypes")
        st.write(data.dtypes)

if upload is not None:
    data_shape = st.radio("what Dimension Do You Want To Check?",('Rows','Columns'))

    if data_shape=="Rows":
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape=="Columns":
        st.text("Number of Columns")
        st.write(data.shape[1])

if upload is not None:
    selected_columns = st.selectbox("Select columns for count of the total number of values in Specific Columns  ", data.columns)
    if selected_columns:
        selected_df = data[selected_columns]
        value_counts = selected_df.value_counts()
        st.write(value_counts)


if upload is not None:
    test = data.isnull().values.any()
    st.write("Total Null value of Particular columns ")
    st.write(data.isnull().sum())
    st.text("Total Null Values in Dataset")
    st.write(data.isnull().sum().sum())
    if test == True:
        if st.checkbox("Null Values in the dataset"):
            fig, ax = plt.subplots()
            sns.heatmap(data.isnull())
            st.pyplot(fig)
    else:
        st.success("No Null OR Missing Values")

if upload is not None:
    test = data.duplicated().any()
    if test== True:
        st.warning("This Dataset Contains Some Duplicate Values")
        dup = st.selectbox("Do You Want to Remove Duplicate Values?",("Select One","Yes","No"))
        if dup=="Yes":
            data = data.drop_duplicates()
            st.text("Duplicate Values are Removed")
        if dup=="No":
                st.text("Ok No Problem")
if upload is not None:
    if st.checkbox("Summary of The Dataset"):
        st.write(data.describe(include="all"))


    selected_column = st.selectbox("Select columns for data visualization(show Top)", data.columns)

    category_mean = data[selected_column].value_counts().head(10)
    fig, ax = plt.subplots()
    category_mean.plot(kind='bar')
    st.pyplot(fig)

#
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
