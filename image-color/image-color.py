import pydaisi as pyd
import streamlit as st
from PIL import Image

colorizer = pyd.Daisi("laiglejm/Image Colorization")

def md_text():
    markdown_text = '''
    Call it in Python:

    ```python
    import pydaisi as pyd
    from PIL import Image

    image = Image.open(<path to image file>)

    colorizer = pyd.Daisi("laiglejm/Image Colorization")
    result = colorizer.run(image).value
    ```
    

    '''

    return markdown_text

def give_colors(image):
    result = colorizer.run(image).value

    return result

def st_ui():
    st.title("Image Colorization")
    image_upload = st.sidebar.file_uploader("Load your image here")
    if image_upload is not None:
        image = Image.open(image_upload)
    else:
        image = Image.open("example.jpeg")
    st.header("Gray Image")
    st.image(image)
    with st.spinner("Colorizing your image"):
        result = give_colors(image)
    st.header("Colored Image")
    st.image(result)

    st.markdown(md_text())

if __name__ == "__main__":
    st_ui()


