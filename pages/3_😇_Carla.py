# -*- coding: utf-8 -*-
"""
 @Author: Zeng Peng
 @Date: 2023-10-09 15:39:09
 @Email: zeng.peng@hotmail.com
"""
import streamlit as st
import utils.app_components as app_components

app_components.render_socialmedia()

# Display the image
image_path = "icons/carla.png"
st.image(image_path, caption='Carla - Your life coach', use_column_width=True)

st.write("This is Carla page")

from streamlit_extras.let_it_rain import rain
rain(
    emoji="🎈",
    font_size=44,
    falling_speed=5,
    animation_length="infinite",
)