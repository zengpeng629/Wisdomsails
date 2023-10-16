# -*- coding: utf-8 -*-
"""
 @Author: Zeng Peng
 @Date: 2023-10-09 15:38:51
 @Email: zeng.peng@hotmail.com
"""
import streamlit as st
import utils.app_components as app_components

app_components.render_socialmedia()
image_path = "icons/boston.png"
st.image(image_path, caption='Boston - Your buddy', use_column_width=True)

st.markdown("""
    <style>
    .stTextArea [data-baseweb=base-input] {
        background-image: linear-gradient(140deg, rgb(54, 36, 31) 0%, rgb(121, 56, 100) 50%, rgb(106, 117, 25) 75%);
        -webkit-text-fill-color: white;
    }

    .stTextArea [data-baseweb=base-input] [disabled=""]{
        background-image: linear-gradient(45deg, red, purple, red);
        -webkit-text-fill-color: gray;
    }
    </style>
    """,unsafe_allow_html=True)
msg_from_boston = "Hello, I am Boston, your document helper. \n\n\
You just need to upload your document, \
and I will help you by answering your questions based on those documents."

st.text_area(
    label="Something Boston wants to say:",
    value=msg_from_boston,
    height=130)