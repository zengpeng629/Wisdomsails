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

# Gallery of AI Agents
st.markdown("#### Meet Our AI Agents")

# Assume agents_info is a list of dictionaries where each dictionary contains the info of one agent
agents_info = [
    {"name": "Albert", "image": "icons/albert.png", "description": "Your meeting notes buddy.", "link": "/Albert"},
    {"name": "Boston", "image": "icons/boston.png", "description": "Your document helper.", "link": "/Boston"},
    {"name": "Carla", "image": "icons/carla.png", "description": "Your daily life assistant.", "link": "/Carla"},
]

# Create rows of 3 agents until all agents have been displayed
for i in range(0, len(agents_info), 3):
    cols = st.columns(3)  # Create a new row with 3 columns
    for j in range(3):  # Fill in each column
        agent = agents_info[i+j] if i+j < len(agents_info) else None  # Get the agent info if exists, else None
        if agent:
            with cols[j]:
                st.image(agent["image"], use_column_width=True)  # Display agent image
                st.markdown(f"<a href='{agent['link']}' style='text-decoration: none; background-color: #204876; color: white; padding: 2px 6px; border-radius: 5px; display: inline-block; text-align: center;'>{agent['name']}</a>", unsafe_allow_html=True)
                st.write(agent["description"])

st.markdown("#### Privacy")
st.write(home_privacy)



