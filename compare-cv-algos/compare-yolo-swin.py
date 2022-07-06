import pydaisi as pyd
import streamlit as st
from PIL import Image

swin_transformer = pyd.Daisi("laurephilippe/Swin Transformer")
yolo_object_detection = pyd.Daisi("erichare/YOLO v6 Object Detection")

def st_ui():
    st.title("Compare interactively YOLOv6 and SWIN !")
    with st.sidebar:
        uploaded_file = st.file_uploader("Choose an Image", type=["png","jpg","jpeg"])

    if not uploaded_file:
        file_name = "cat.png"
    else:
        file_name = uploaded_file

    img = Image.open(file_name)
    st.image(img)
    with st.spinner("Processing image with SWIN"):
        from_swin = swin_transformer.compute(img).value
    st.subheader(f"Labels from Swin : {from_swin}")
    with st.spinner("Processing image with Yolo"):
        try:
            yolo_result, labels_df = yolo_object_detection.yolo(img, return_type=["Image", "Labels"]).value
        except:
            st.write("Not many great results from YoloV6 for this image")
    
    st.subheader("Label from Yolov6 :")
    st.table(labels_df)
    st.subheader(f"Boxes from Yolo:")
    st.image(yolo_result)

if __name__ == "__main__":
    st_ui()



   


