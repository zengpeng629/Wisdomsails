import whisper
import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
from utils.utils import take_notes

# Initialize speech recognition
r = sr.Recognizer()

# Display the image
image_path = "icons/albert.png"
st.image(image_path, caption='Albert - Meeting Notes Taker', use_column_width=True)

# Streamlit app
st.markdown("Upload an audio file and let Albert transcribe and take notes for you!")

# Custom Styling
st.markdown("""
    <style>
        .stFileUploader>div>div>button {
            background-color: #4CAF50;
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose an audio file to get started...", type=["m4a", "wav", "mp3", "flac"])

if st.button('Click here, let Albert work!', type="primary") and uploaded_file is not None:
    # Check the file format and convert if necessary
    file_details = uploaded_file.name.split('.')
    file_format = file_details[-1]
    if file_format == 'm4a':
        with st.spinner('Converting audio to a compatible format...'):
            audio = AudioSegment.from_file(uploaded_file, format="m4a")
            audio.export("temp.wav", format="wav")
            file_path = "temp.wav"
    else:
        file_path = uploaded_file

    with st.spinner('Transcribing the audio...'):
        audio_file = sr.AudioFile(file_path)
        with audio_file as source:
            audio_data = r.record(source)
            try:
                # transcription = r.recognize_whisper(
                #     audio_data,
                #     model="medium.en",
                #     show_dict=True,
                # )["text"]
                # transcription = r.recognize_google(audio_data, language= 'en-in')
                model = whisper.load_model("base")
                transcription = model.transcribe("temp.wav")["text"]

                st.success('Transcription completed! Albert is now generating meeting notes...')
                notes = take_notes(transcription)
                st.markdown("**Notes:**")
                st.write(notes)
                
            except sr.UnknownValueError:
                st.warning("Sorry, we couldn't understand the audio. Please try uploading a clearer audio file.")
            except sr.RequestError:
                st.error("Oops! It seems like the API is unavailable or unresponsive. Please try again later.")
