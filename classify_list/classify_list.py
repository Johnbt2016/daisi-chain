from doctest import DocFileSuite
import pydaisi as pyd
import pandas as pd
import streamlit as st


classify = pyd.Daisi("Zero Shot Text Classification")

def get_labels(df, column, candidate_labels):
    print(df)
    data_list = df[column].to_list()
    labels = [classify.compute(text = n, candidate_labels = candidate_labels).value for n in data_list]
    return labels


def st_ui():
    st.title("Zero Shot Text Classification")

    st.markdown('''
    This daisi uses the Bart langugage model developed by Facebook for Zero Shot classification.   
    Simply upload an Excel file with a column containing the sentences to classify and define possible labels.   
    
    Call it in your code now (see the [Daisi Zero Shot Text Classification" doc](https://app.daisi.io/daisies/237587e0-7c47-4a4f-afad-80370c8e98a4/how-to-use)):   
    `import pydaisi as pyd`   
    `classify =  pyd.Daisi("Zero Shot Text Classification")`   
    `result = classify.compute(text="Let's go the moon", candidate_labels="astronomy, travel").value`   

    
    Check also the [model doc](https://huggingface.co/docs/transformers/main/en/model_doc/bart#transformers.BartForSequenceClassification) on Transformers
    ''')

    fileupload = st.sidebar.file_uploader("Load an Excel file with the text to classify in a column")
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
    
st_ui()