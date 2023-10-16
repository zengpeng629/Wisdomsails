import whisper
import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
from utils.utils import agent_take_notes
from streamlit_option_menu import option_menu
from utils.lang import en, cn

selected_lang = option_menu(
    menu_title=None,
    options=["EN", "中文", ],
    icons=["globe2", "translate"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

match selected_lang:
    case "EN":
        st.session_state.locale = en
    case "中文":
        st.session_state.locale = cn

with st.sidebar:
    openai_api_key = st.text_input(f"{st.session_state.locale.input_key_instruct}", key="openai_api_key", type="password")
    st.write(f"{st.session_state.locale.get_key_instruct} [link](https://platform.openai.com/account/api-keys)")

# Initialize speech recognition
r = sr.Recognizer()

# Display the image
image_path = "icons/albert.png"
st.image(image_path, caption=f"{st.session_state.locale.albert}", use_column_width=True)

# Streamlit app
st.markdown("""
    <style>
    .stTextArea [data-baseweb=base-input] {
        background-image: linear-gradient(140deg, rgb(54, 36, 31) 0%, rgb(121, 56, 100) 50%, rgb(106, 117, 25) 75%);
        -webkit-text-fill-color: white;
    }

    .stTextArea [data-baseweb=base-input] [disabled=""]{
        background-image: linear-gradient(45deg, red, purple, red);
        -webkit-text-fill-color: gray;
    }
    </style>
    """,unsafe_allow_html=True)

st.text_area(
    label="",
    value=st.session_state.locale.albert_intro,
    height=160)

# Custom Styling
st.markdown("""
    <style>
        .stFileUploader>div>div>button {
            background-color: #4CAF50;
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

uploaded_file = st.file_uploader(f"{st.session_state.locale.albert_upload_instruct}", type=["m4a", "wav", "mp3", "flac"])

if st.button(f"{st.session_state.locale.albert_button}", type="primary") and uploaded_file is not None:
    if not openai_api_key:
        st.info(f"{st.session_state.locale.key_not_found}")
        st.stop()
    # Check the file format and convert if necessary
    file_details = uploaded_file.name.split('.')
    file_format = file_details[-1]
    if file_format == 'm4a':
        audio = AudioSegment.from_file(uploaded_file, format="m4a")
        audio.export("temp.wav", format="wav")
        file_path = "temp.wav"
    else:
        file_path = uploaded_file

    with st.spinner(f"{st.session_state.locale.transcribing}"):
        audio_file = sr.AudioFile(file_path)
        with audio_file as source:
            audio_data = r.record(source)
            try:
                model = whisper.load_model("base")
                transcription = model.transcribe("temp.wav")["text"]

                st.success(f"{st.session_state.locale.transcribe_done}")
                notes = agent_take_notes(transcription, openai_api_key)
                st.markdown("#### {}".format(st.session_state.locale.note))
                st.write(notes)
                
            except sr.UnknownValueError:
                st.warning("Sorry, we couldn't understand the audio. Please try uploading a clearer audio file.")
            except sr.RequestError:
                st.error("Oops! It seems like the API is unavailable or unresponsive. Please try again later.")
