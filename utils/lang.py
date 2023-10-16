# -*- coding: utf-8 -*-
"""
 @Author: Zeng Peng
 @Date: 2023-10-15 18:40:04
 @Email: zeng.peng@hotmail.com
"""

from  dataclasses import dataclass
from typing import List, Optional

@dataclass
class Locale:
    input_key_instruct: str
    get_key_instruct: str
    home_title: str
    home_privacy: str
    greetings: str
    welcome_words: str
    meet_agents: str
    privacy: str
    key_not_found: str
    # ----------------- Agents -----------------
    # Albert
    albert: str
    albert_desc: str
    albert_intro: str
    albert_upload_instruct: str
    albert_button: str
    transcribing: str
    transcribe_done: str
    note: str
    # Boston
    boston: str
    boston_desc: str
    # Carla
    carla: str
    carla_desc: str
    
en = Locale(
    input_key_instruct = "Please enter your OpenAI API key:",
    get_key_instruct = "Don't have an OpenAI key? Get one here: ",
    home_title = "WisdomSails",
    home_privacy = "At WisdomSails, your privacy is our top priority. To protect your personal information, our system only uses the hashed value of your OpenAI API Key, ensuring complete privacy and anonymity. Your API key is only used to access AI functionality during each visit, and is not stored beyond that time. This means you can use WisdomSails with peace of mind, knowing that your data is always safe and secure.",
    greetings = "Greetings!",
    welcome_words = "Welcome to Wisdomsails!\n\nI'm Zeng, your AI manager here to assist you throughout your journey in this wonderful place.\n\nWe have several AI agents here like Albert, Boston, and Carla, who are all ready to help you with your daily life.\n\nFeel free to reach out for any assistance!",
    meet_agents = "Meet Our Agents",
    privacy = "Privacy",
    key_not_found = "API key not found. Please enter your API key.",
    # ----------------- Agents -----------------
    # Albert
    albert = "Albert",
    albert_desc = "Your meeting notes taker.",
    albert_intro = "Hi! My name is Albert, your meeting notes taker. \n\nMeetings can be intense, engaging, or sometimes just long. Whether you've forgotten to jot down critical details, or simply didn't want the hassle of note-taking, I'm here to help. \n\nJust upload your meeting audio, and I will generate meeting notes as an email for you.",
    albert_upload_instruct = "Upload your meeting transcription here:",
    albert_button = "Click here, Let Albert work for you!",
    transcribing = "Albert is transcribing your audio, please wait...",
    transcribe_done = "Transcription completed! Albert is now generating meeting notes...",
    note = "Here are your meeting notes:",
    # Boston
    boston = "Boston",
    boston_desc = "Your personal assistant.",
    # Carla
    carla = "Carla",
    carla_desc = "Your personal stylist.",
)

cn = Locale(
    input_key_instruct = "请输入您的OpenAI API密钥:",
    get_key_instruct = "还没有OpenAI秘钥？在这里获取: ",
    home_title = "人类慧帆",
    home_privacy = "在人类慧帆，您的隐私是我们的首要任务。为了保护您的个人信息，我们的系统只使用您的OpenAI API密钥的哈希值，确保完全的隐私和匿名性。您的API密钥仅在每次访问时用于访问AI功能，并且不会存储超出该时间。这意味着您可以放心使用人类慧帆，因为您的数据始终是安全的。",
    greetings = "你好！",
    welcome_words = "欢迎来到人类慧帆！\n\n我是Zeng，您的AI管理员，我将在这个神奇的地方为您提供帮助。\n\n我们这里有几个AI代理，如Albert，Boston和Carla，他们都准备好帮助您处理日常生活中的问题。\n\n如有任何疑问，请随时与我们联系！",
    meet_agents = "见见我们的代理吧!",
    privacy = "隐私",
    key_not_found = "没有找到您的OpenAI Key。请输入！",
    # ----------------- Agents -----------------
    # Albert
    albert = "阿伯特",
    albert_desc = "您的会议记录员。",
    albert_intro = "嗨！我的名字是阿伯特，您的会议记录员。\n\n会议可能会很紧张，有趣，或者有时只是很长。无论您是忘记了记录重要细节，还是只是不想麻烦记录笔记，我都可以帮助您。\n\n只需上传会议音频，我就会为您生成会议记录。",
    albert_upload_instruct = "在这里上传您的会议录音:",
    albert_button = "点击这里，让阿伯特开始工作!",
    transcribing = "阿伯特正在处理您的音频，请稍候...",
    transcribe_done = "转录完成！阿伯特正在生成会议记录...",
    note = "这是您的会议记录:",
    # Boston
    boston = "波士顿",
    boston_desc = "您的私人助理。",
    # Carla
    carla = "卡拉",
    carla_desc = "您的私人造型师。",
)
