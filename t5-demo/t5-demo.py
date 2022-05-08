import pydaisi as pyd
import streamlit as st

translator = pyd.Daisi("LanguageTranslator")

def translate(sentence, source_language, target_language):
    return translator.translate(text=sentence, dest=target_language).value

def st_ui():
    st.title("T5 language translator")

    st.markdown('''
    This is an application of the T5 language model developed by Google for translation.   

    Call it in your code (see the [Daisi "LanguageTranslator" doc](https://app.daisi.io/daisies/63ed4819-2134-4cfc-87d1-eba65bdaeed2/how-to-use)):   
    `import pydaisi as pyd`   
    `tranlator =  pyd.Daisi("LanguageTranslator")`   
    `result = translator.translate(text="Testing the translation", dest='french').value`   

    
    Check also the [model doc](https://huggingface.co/docs/transformers/main/en/model_doc/t5#transformers.T5WithLMHeadModel) on Transformers
    ''')

    sentence = st.text_area(label="Type in the sentence to translate", value = "Testing the translation")
    languages = ['french', 'german']
    source_language = st.sidebar.selectbox("Input language", ['english'],index=0)
    target_language = st.sidebar.selectbox("Output language", languages)

    output = translate(sentence, source_language, target_language)

    st.header("Translation result :")
    st.write(output)

st_ui()