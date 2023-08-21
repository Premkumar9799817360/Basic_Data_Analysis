import numpy as np
import pandas as pd
import streamlit as st
#from pandas_profiling import ProfileReport
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


st.set_page_config(page_title="EDA APP", page_icon=":bar_chart:", layout="wide")

# Web App Title
st.title("Exploratory Data Analysis :bar_chart:")
st.subheader(''':link: [Prem Kumar](https://prembhargav.netlify.app/)      :bow_and_arrow: [GitHub](https://github.com/Premkumar9799817360)''')

# Upload CSV data

with st.sidebar.header('1. Upload your CSV data :file_folder:'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.subheader("About :technologist:")
    st.sidebar.text("This project aims to automatically\nperform advanced exploratory data\nanalysis (EDA) of any dataset using\nthe Pandas profiling library.\nThis app provides insights from an\nExploratory Data Analysis project.\nThe goal of the project was to\nanalyze a dataset, uncover patterns,\nrelationships, anomalies, present\nthe findings in an easy-to-understand\nmanner.")


# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache_data
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)