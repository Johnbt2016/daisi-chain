import streamlit as st
import pydaisi as pyd

zero_shot = pyd.Daisi("Zero Shot Text Classification")

def md_text():
    markdown_text = '''
    Call it in Python:

    ```python
    import pydaisi as pyd

    zero_shot = pyd.Daisi("Zero Shot Text Classification")
    result = zero_shot.compute(text="Let's go to the moon", 
                                candidate_labels='travel, astronomy', 
                                is_multi_labels=False).value
    ```
    

    '''

    return markdown_text

def compute(text, candidate_labels, is_multi_labels="false"):
    result = zero_shot.compute(text=text, candidate_labels=candidate_labels, is_multi_labels=is_multi_labels).value

    return result

def st_ui():
    st.title("Zero Shot Text Classification")
    text = st.sidebar.text_input("Your text here", "Let's go to the moon")
    candidate_labels = st.sidebar.text_input("Candidate labels (comma separated)", "travel, astronomy")
    multi_labels = st.sidebar.checkbox('Allow multi labels classification')
    if multi_labels:
        is_multi_labels = "true"
    else:
        is_multi_labels = "false"
    result = compute(text, candidate_labels, is_multi_labels)

    st.write(result)

    st.markdown(md_text())

if __name__ == "__main__":
    st_ui()
