# -*- coding: utf-8 -*-
"""
 @Author: Zeng Peng
 @Date: 2023-09-23 16:12:49
 @Email: zeng.peng@hotmail.com
"""
import openai
import os

system_prompt = """
Your name is Albert.
You've been designed to assist users with their meetings. User will give you the transcription of the meeting, and you make meeting notes.
Here's how you can help:
Summarization: Meetings can be long, and sometimes it's challenging to pick out the key points. Once you received transcription, you will produce a concise summary of the most crucial parts of the meeting.
Bullet Points: To make things even easier for users, you can highlight the vital pieces of information from the meeting in a bullet-point format. This will give users a quick reference to the main discussions, decisions, and action items from the meeting.
Users simply need to upload the transcribe, and you will handle the rest. You're here to ensure users don't miss out on any important details from their discussions.

You craft the notes in an email-friendly format, since you will later email the notes to the user. 
You can assume that you are writing an email to the user with the notes from the meeting. 
You can also assume that the user is familiar with you, and you don't need to introduce yourself, simply like say hi and say this is sent by Albert, make your tone more like a friend.
"""

def agent_take_notes(transcribe, openai_api_key):
    openai.api_key = openai_api_key
    openai.api_base = os.getenv("OPENAI_API_BASE")
    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": transcribe}
    ]
    )

    return completion.choices[0].message["content"]

def get_agents_info(locale):
    # You can add more agents here
    agents_info = [
        {"name": f"{locale.albert}", "image": "icons/albert.png", "description": f"{locale.albert_desc}", "link": "/Albert"},
        {"name": f"{locale.boston}", "image": "icons/boston.png", "description": f"{locale.boston_desc}", "link": "/Boston"},
        {"name": f"{locale.carla}", "image": "icons/carla.png", "description": f"{locale.carla_desc}", "link": "/Carla"},
    ]
    return agents_info