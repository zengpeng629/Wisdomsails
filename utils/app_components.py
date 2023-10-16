# -*- coding: utf-8 -*-
"""
 @Author: Zeng Peng
 @Date: 2023-10-09 15:27:45
 @Email: zeng.peng@hotmail.com
"""
import streamlit as st

def render_agent_gallery(agents_info):
    # Create rows of 3 agents until all agents have been displayed
    for i in range(0, len(agents_info), 3):
        cols = st.columns(3)  # Create a new row with 3 columns
        for j in range(3):  # Fill in each column
            agent = agents_info[i+j] if i+j < len(agents_info) else None  # Get the agent info if exists, else None
            if agent:
                with cols[j]:
                    st.image(agent["image"], use_column_width=True)  # Display agent image
                    st.markdown(f"<a href='{agent['link']}' target=\"_self\" style='text-decoration: none; background-color: #204876; color: white; padding: 2px 6px; border-radius: 5px; display: inline-block; text-align: center;'>{agent['name']}</a>", unsafe_allow_html=True)
                    st.write(agent["description"])