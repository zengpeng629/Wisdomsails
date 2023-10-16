# -*- coding: utf-8 -*-
"""
 @Author: Zeng Peng
 @Date: 2023-10-09 15:31:55
 @Email: zeng.peng@hotmail.com
"""
import streamlit as st 
import utils.utils as utils
from utils.lang import en, cn
from utils.app_components import render_agent_gallery
from streamlit_option_menu import option_menu

# Storing The Context
if "locale" not in st.session_state:
    st.session_state.locale = en

if st.session_state.locale is not None:
        default_index = 0 if st.session_state.locale == en else 1

with st.sidebar:
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

    openai_api_key = st.text_input(f"{st.session_state.locale.input_key_instruct}", key="openai_api_key", type="password")
    st.write(f"{st.session_state.locale.get_key_instruct} [link](https://platform.openai.com/account/api-keys)")

# Storing The Context
if "openai_api_key" not in st.session_state:
    st.session_state.openai_api_key = openai_api_key

st.markdown(
    "<style>#MainMenu{visibility:hidden;}</style>",
    unsafe_allow_html=True
)

st.markdown(f"""# {st.session_state.locale.home_title} <span style=color:#2E9BF5><font size=5>Beta</font></span>""",unsafe_allow_html=True)

image_path = "icons/Zeng.png"
st.image(image_path, use_column_width=True)

st.markdown("#### {}".format(st.session_state.locale.greetings))
st.write(st.session_state.locale.welcome_words)

# Gallery of AI Agents
st.markdown("#### {}".format(st.session_state.locale.meet_agents))

# Assume agents_info is a list of dictionaries where each dictionary contains the info of one agent
agents_info = utils.get_agents_info(st.session_state.locale)
render_agent_gallery(agents_info)

st.markdown("#### {}".format(st.session_state.locale.privacy))
st.write(st.session_state.locale.home_privacy)