import os
from dotenv import load_dotenv
load_dotenv()
import mimetypes
from google import genai
from google.genai import types
from .models import AccountMemo

# Make sure GEMINI_API_KEY is natively set in the environment or passed when creating the client
# If not present, throw a clear error

def extract_account_memo(file_path: str, previous_memo: AccountMemo = None) -> AccountMemo:
    """
    Extracts an AccountMemo from a transcript or audio file.
    If previous_memo is provided, this acts as an 'onboarding update' treating previous_memo as v1.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set. A free key from Google AI Studio is required for zero-cost operation.")

    client = genai.Client(api_key=api_key)

    # Determine file type
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        if file_path.endswith('.m4a'):
            mime_type = 'audio/mp4'
            from .whisper_stub import transcribe_audio_free
            transcript = transcribe_audio_free(file_path)
            # We swap the file pointing to a generated transcript
            tmp_txt = file_path + ".txt"
            with open(tmp_txt, "w") as f:
                f.write(transcript)
            file_path = tmp_txt
            mime_type = "text/plain"
        elif file_path.endswith('.txt'):
            mime_type = 'text/plain'
        else:
            mime_type = 'application/octet-stream'

    uploaded_file = client.files.upload(file=file_path, config={'mime_type': mime_type})

    system_instructions = """
    You are an AI assistant processing customer call recordings or transcripts to configure an AI voice agent (Clara Answers). 
    Extract the required information strictly based on what is stated in the call.
    DO NOT hallucinate or assume details not mentioned for missing fields. Instead, list missing but essential details under 'questions_or_unknowns'.
    You are outputting a strict JSON format complying with the AccountMemo schema.
    """
    
    prompt = "Extract the AccountMemo details from this customer discussion."
    if previous_memo:
        prompt += f"""
        This is an ONBOARDING update. You are given the previous v1 memo details below. 
        Update the structured memo based on the new onboarding information in the provided file, maintaining unchanged data and adding/modifying constrained rules.
        Previous Memo (v1):
        {previous_memo.model_dump_json()}
        """
    else:
        prompt += "\nThis is a Demo Call. Assume incomplete information and rely solely on explicit statements."

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=[
            uploaded_file,
            prompt
        ],
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=AccountMemo,
            system_instruction=system_instructions,
        ),
    )
    
    return AccountMemo.model_validate_json(response.text)
