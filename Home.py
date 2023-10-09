# -*- coding: utf-8 -*-
"""
 @Author: Zeng Peng
 @Date: 2023-10-09 15:31:55
 @Email: zeng.peng@hotmail.com
"""
import streamlit as st 
import utils.app_components as app_components

app_components.render_socialmedia()

# copies 
home_title = "WisdomSails"
home_privacy = "At WisdomSails, your privacy is our top priority. To protect your personal information, our system only uses the hashed value of your OpenAI API Key, ensuring complete privacy and anonymity. Your API key is only used to access AI functionality during each visit, and is not stored beyond that time. This means you can use WisdomSails with peace of mind, knowing that your data is always safe and secure."

st.markdown(
    "<style>#MainMenu{visibility:hidden;}</style>",
    unsafe_allow_html=True
)

st.markdown(f"""# {home_title} <span style=color:#2E9BF5><font size=5>Beta</font></span>""",unsafe_allow_html=True)

image_path = "icons/Zeng.png"
st.image(image_path, use_column_width=True)

st.markdown("#### Greetings!")
st.write("Welcome to Wisdomsails!\n\nI'm Zeng, your AI manager here to assist you throughout your journey in this wonderful place.\n\nWe have several AI agents here like Albert, Boston, and Carla, who are all ready to help you with your daily life.\n\nFeel free to reach out for any assistance!")


st.markdown("#### Privacy")
st.write(home_privacy)

st.markdown("#### Who are we?")


