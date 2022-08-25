import streamlit as st
import pydaisi as pyd
from summary import *

ask_bert = pyd.Daisi("erichare/Ask BERT")

def get_answer(context, query):
    answer = ask_bert.compute(query, context).value
    staight_answer = answer[0]['answer']
    answer_proba = int(100*float(answer[0]['score']))
    highlighted_answer = answer[1]

    return staight_answer, highlighted_answer, answer_proba

def st_ui():
    st.set_page_config(layout = "wide")
    st.title("Awesome Bert")

    context = st.sidebar.text_area("Enter a context", 
                                        value ="The potato is a starchy vegetable.", 
                                        height = 400)

    col1, col2 = st.columns(2)

    with col1:

        query = st.text_input("Enter your question", 
                               value = "What is a potato?")

        staight_answer,\
        highlighted_answer,\
        answer_proba = get_answer(context, query)

        st.header("Answer : " + staight_answer)
        st.subheader("Answer confidence : " + str(answer_proba) + "%")
        st.write("And this is the answer in context :")
        st.write(highlighted_answer, unsafe_allow_html=True)

        with open("DAISI.md", "r") as f:
            summary = f.read()

        with st.expander("Summary", expanded = True):
            st.markdown(summary)
    
    with col2:
        st.image('Bert_smile.png', width = 300)

if __name__ == "__main__":
    st_ui()