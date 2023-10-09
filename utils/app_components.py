# -*- coding: utf-8 -*-
"""
 @Author: Zeng Peng
 @Date: 2023-10-09 15:27:45
 @Email: zeng.peng@hotmail.com
"""
import streamlit as st

def st_button(url, label, font_awesome_icon):
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">', unsafe_allow_html=True)
    button_code = f'''<a href="{url}" target=_blank><i class="fa {font_awesome_icon}"></i>   {label}</a>'''
    return st.markdown(button_code, unsafe_allow_html=True)

def render_socialmedia():
  with st.sidebar:
      st.write("Let's connect!")
      st_button(url="https://twitter.com/viapeng", label="Twitter", font_awesome_icon="fa-twitter")
      st_button(url="www.linkedin.com/in/zengpeng", label="LinkedIn", font_awesome_icon="fa-linkedin")
