# Step 1a - Install gtts - Setup text to speech TTS model with gtts
import os
import subprocess  #Used in Autoplay of doctor's voice
import platform    #Used to find which OS platform the code is running on
from gtts import gTTS
from dotenv import load_dotenv

load_dotenv()


def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"

    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow = False
    )

    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == 'Darwin': # macos
            subprocess.run(['afplay', output_filepath])

        elif os_name == 'Windows': # Windows
            subprocess.run(['powershell','-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])

        elif os_name == 'Linux': #Linux
            subprocess.run(['aplay', output_filepath])  #Alternatives use 'mpg123' or 'ffplay'

        else:
            raise OSError("Unsupported Operating System...")
        
    except Exception as e:
        print(f"An Error occured while tryig to play the audio: {e}")






input_text = "Hi, This is your doctor speaking."
output_filepath = "gtts_testing.mp3"
text_to_speech_with_gtts(input_text,output_filepath=output_filepath )


# Step 1b - Setup Text to speech model with Elevenlabs(install elevenlabs)

import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_elevenlabs(input_text, output_filepath):

    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.text_to_speech.convert(
        text = input_text,
        voice_id='JBFqnCBsd6RMkjVDRZzb',
        output_format = "mp3_22050_32",
        model_id="eleven_turbo_v2"
    )

    elevenlabs.save(audio, output_filepath)
    os_name = platform.system()
    try:
        if os_name == 'Darwin': # macos
            subprocess.run(['afplay', output_filepath])

        elif os_name == 'Windows': # Windows
            # subprocess.run(['powershell','-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
            subprocess.run(['powershell','-c', f'(New-Object System.Windows.Media.MediaPlayer "{output_filepath}").PlaySync();'])


        elif os_name == 'Linux': #Linux
            subprocess.run(['aplay', output_filepath])  #Alternatives use 'mpg123' or 'ffplay'

        else:
            raise OSError("Unsupported Operating System...")
        
    except Exception as e:
        print("An Error occured while tryig to play the audio: {e}")



# input_text = "Hi, This is your doctor speaking."
# output_filepath = "elevenlabs_testing.mp3"
# text_to_speech_with_elevenlabs(input_text,output_filepath=output_filepath )


# Step 2 - Use Model to text output to voice



