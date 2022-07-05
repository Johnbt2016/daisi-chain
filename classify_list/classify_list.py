import pydaisi as pyd
import pandas as pd
import streamlit as st
from summary import *

zero_shot = pyd.Daisi("exampledaisies/Zero Shot Text Classification")

def get_labels(df, column, candidate_labels):
    '''
    Returns the classification of sentences stored in a column of a dataframe.

    Parameters:
    - df (Pandas Dataframe) :  the input Dataframe 
    - column (str) : the title of the column containing the sentences
    - candidate_labels (str) : the possible labels to classify the sentences (labels need to be separated by commas)

    Returns:
    - a list of labels corresponding to each sentence
    '''

    data_list = df[column].to_list()
    labels = [zero_shot.compute(text = n, candidate_labels = candidate_labels).value for n in data_list]
    return labels


def st_ui():
    '''This function renders the Streamlit UI'''
    st.set_page_config(layout = "wide")
    st.title("Zero Shot Text Classification")

    with st.expander("Summary"):
        st.markdown(get_summary())

    fileupload = st.sidebar.file_uploader("Load an Excel file with the sentences to classify in a column")
    if fileupload is not None:
        df = pd.read_excel(fileupload)
        headers = df.columns.values.tolist()
        column_choice = st.sidebar.selectbox("Column to classify", headers,index=len(headers) - 1)
        labels = st.sidebar.text_input("Labels list (comma separated)", value = "positive, negative")
        st.header("View of your Data")
        st.dataframe(df)
        labels = get_labels(df, column_choice, labels)
        s = [el['result']['labels'][0] for el in labels]
        proba = [el['result']['scores'][0] for el in labels]
        df["Classification Result"] = s
        df["Proba"] = proba
        st.header("Classification results")
        st.dataframe(df)
    
if __name__ == "__main__":
    st_ui()
