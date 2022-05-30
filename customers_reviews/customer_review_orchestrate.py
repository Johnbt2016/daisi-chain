import pydaisi as pyd
import pandas as pd
from PIL import Image
import io
import base64
import streamlit as st

classify = pyd.Daisi("Classify Labels")
translator = pyd.Daisi("LanguageTranslator")
wc = pyd.Daisi("laiglejm/WordCloud")
yelp = pyd.Daisi("Get Yelp Reviews")

def sentiment(df):
    #Daisi call
    sentiments = classify.get_labels(df=df, column="review", candidate_labels="positive, negative").value

    s = [el['result']['labels'][0] for el in sentiments]
    df['sentiment'] = s

    return df

def translate(df, language = 'French'):
    french_revs = []
    for index, row in df.iterrows():

        #Daisi call
        result = translator.translate(text=row['review'], dest=language).value
        french_revs.append(result)
    df[f'reviews in {language}'] = french_revs

    return df

def wordcloud(df):
    df = df.rename(columns={'review': 'title'})

    bytestring_image = wc.generate_wordcloud_byte(texts_path=df).value

    imgdata = base64.b64decode(bytestring_image)
    image = Image.open(io.BytesIO(imgdata)).convert('RGBA')

    return image

def orchestrate(term="korean", location="Houston", language="French"):
    '''
    Orchestrate 4 Daisies to pull restaurant reviews from Yelp, analyze sentiment
    of each review, translate in a different language and compute a Wordcloud

    Parameters:
    - term (str) : the restaurant type (default = "korean")
    - location (str) : the city (default = "Houston")
    - language (str) : the language for translation

    Returns:
    - a Pandas Dataframe with the results
    - an image of the Wordcloud
    '''

    df = yelp.get_reviews(term=term, location=location).value

    df = sentiment(df)

    df = translate(df=df, language=language)

    image = wordcloud(df)

    return df, image

def st_ui():
    st.title("Daisi ETL example")

    term = st.sidebar.text_input("Style", "korean")
    location = st.sidebar.text_input("Location", "Houston")
    language = st.sidebar.text_input("Language for translation", "French")

    with st.spinner("Collecting reviews"):
        df = yelp.get_reviews(term=term, location=location).value
    st.header("Collected data")
    st.dataframe(df)

    with st.spinner("Computing sentiments"):
        df = sentiment(df)
    st.header("Sentiments computation results")
    st.dataframe(df)
    with st.spinner("Translating reviews"):
        df = translate(df=df, language=language)
    st.header(f"Translation in {language}")
    st.dataframe(df)
    with st.spinner("Computing a wordcloud"):

        image = wordcloud(df)
    st.header("Wordcloud")
    st.image(image)

if __name__ == "__main__":
    st_ui()

