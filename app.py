from PIL import Image
import streamlit as st

st.title("Mi wey y su novia")

imagen = Image.open("oscar.jpg")
st.image(imagen, caption="<3")