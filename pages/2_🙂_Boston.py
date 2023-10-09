# -*- coding: utf-8 -*-
"""
 @Author: Zeng Peng
 @Date: 2023-10-09 15:38:51
 @Email: zeng.peng@hotmail.com
"""
import streamlit as st

# Display the image
image_path = "icons/boston.png"
st.image(image_path, caption='Boston - Your documents buddy', use_column_width=True)

st.write("This is Boston page")