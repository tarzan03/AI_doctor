# Step 1 - Setup Audio recorder (ffmpeg and portaudio, pyaudio)
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    recogniser = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for Ambient noise...")
            recogniser.adjust_for_ambient_noise(source, duration=1) 
            logging.info("Start Speaking Now....")

            # Record the Audio
            audio_data = recogniser.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording Complete...")

            # Convert the recorded audio to an MP3 file
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format='mp3', bitrate='128k')

            logging.info(f"Audio saved to {file_path}...")

    except Exception as e:
        logging.error(f"an error occured: {e}")


audio_filepath = "patiets_voice.mp3"
# record_audio(file_path="patiets_voice.mp3")


# Step 2 - Setup Speech to text(STT) Model for Transcription
import os 
from groq import Groq
from dotenv import load_dotenv
load_dotenv()


GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

client = Groq()
stt_model="whisper-large-V3"
audio_file = open(audio_filepath, "rb")
transcription = client.audio.transcriptions.create(
    model = stt_model,
    file = audio_file,
    language="en"
)


print(transcription.text)
