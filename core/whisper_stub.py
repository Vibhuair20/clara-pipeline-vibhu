# Fallback free transcription stub
import os
from dotenv import load_dotenv
load_dotenv()
import subprocess
import json

def transcribe_audio_free(audio_path: str) -> str:
    """Uses a free API to generate transcripts from audio input."""
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
