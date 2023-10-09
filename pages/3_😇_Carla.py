# -*- coding: utf-8 -*-
"""
 @Author: Zeng Peng
 @Date: 2023-10-09 15:39:09
 @Email: zeng.peng@hotmail.com
"""
import streamlit as st

# Display the image
image_path = "icons/carla.png"
st.image(image_path, caption='Carla - Your life coach', use_column_width=True)

st.write("This is Carla page")