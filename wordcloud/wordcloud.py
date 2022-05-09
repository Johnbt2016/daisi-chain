import pydaisi as pyd
import pandas as pd
import streamlit as st
import numpy as np
from PIL import Image
import io
import base64


wc = pyd.Daisi("WordCloud")

def wordcloud(df):
    df = df.rename(columns={'review': 'title'})

    bytestring_image = wc.generate_wordcloud_byte(texts_path=df).value

    imgdata = base64.b64decode(bytestring_image)
    image = np.array(Image.open(io.BytesIO(imgdata)).convert('RGBA'))

    return image


def st_ui():
    st.title("Compute a beautiful Wordcloud")

    st.markdown('''
    This daisi comutes and render a wordcloud.   
    Simply upload an Excel file with a column containing the sentences that will be used to compute the wordcloud.   
    The column needs to be labelled "title"   
    
    Call it in your code now (see the [Daisi "WordCloud" doc](https://app.daisi.io/daisies/237587e0-7c47-4a4f-afad-80370c8e98a4/how-to-use)):   
    `import pydaisi as pyd`   
    `import pandas as pd`   

    `classify =  pyd.Daisi("WordCloud")`   
    `df = pd.read_excel(<filename>)`
    `df = df.rename(columns={'your column name': 'title'})`
    `bytestring_image = wc.generate_wordcloud_byte(texts_path=df).value`   

    
    ''')

    fileupload = st.sidebar.file_uploader("Load an Excel file with the text to classify in a column")
    if fileupload is not None:
        df = pd.read_excel(fileupload)
        headers = df.columns.values.tolist()
        column_choice = st.sidebar.selectbox("Column to use to compute a wordcloud", headers,index=len(headers) - 1)
        df = df.rename(columns={column_choice: 'title'})

        st.header("View of your Data")
        st.dataframe(df)
        image = wordcloud(df)
        
        st.header("WordCloud !")
        st.image(image)
    
st_ui()