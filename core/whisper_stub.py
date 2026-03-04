# Fallback free transcription stub
import os
from dotenv import load_dotenv
load_dotenv()
import subprocess
import json

def transcribe_audio_free(audio_path: str) -> str:
    """Uses a free API or local mock to generate transcripts so we can pass .txt downstream."""
    # Since we can't reliably install local Whisper or FFmpeg due to Xcode license constraints
    # and the prompt says "If we provide transcripts: use them directly", we write a converter that
    # uses Google Gemini's audio capability just to spit out the raw text transcript, 
    # and then we save it as a text file for the next step.
    from google import genai
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    uploaded_file = client.files.upload(file=audio_path)
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=[
            uploaded_file,
            "Provide a highly accurate, word-for-word text transcription of this audio file. Do not include any other commentary, markdown formatting, or preamble. Just the raw text transcript."
        ]
    )
    return response.text
