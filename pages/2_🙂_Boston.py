# -*- coding: utf-8 -*-
"""
 @Author: Zeng Peng
 @Date: 2023-10-09 15:38:51
 @Email: zeng.peng@hotmail.com
"""
import streamlit as st
from streamlit_option_menu import option_menu
from utils.lang import en, cn

default_index = 0
if "locale" in st.session_state:
    default_index = 1 if st.session_state.locale == cn else 0

selected_lang = option_menu(
    menu_title=None,
    options=["EN", "中文", ],
    icons=["globe2", "translate"],
    menu_icon="cast",
    default_index=default_index,
    orientation="horizontal",
)

match selected_lang:
    case "EN":
        st.session_state.locale = en
    case "中文":
        st.session_state.locale = cn

with st.sidebar:
    openai_api_key = st.text_input(f"{st.session_state.locale.input_key_instruct}", key="openai_api_key", type="password")
    st.write(f"{st.session_state.locale.get_key_instruct} [link](https://platform.openai.com/account/api-keys)")

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