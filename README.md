# Clara Answers Zero-Cost Automation Pipeline

This represents a complete, zero-cost, serverless AI automation pipeline for ingesting Demo and Onboarding recordings/transcripts, generating structured metadata schemas, mapping them to Retell AI prompt constraints, and automatically diffing changes over time.

## Architecture and Data Flow

1. **Ingestion & Extraction (Zero-Cost LLM)**
   - The CLI batch process ingests audio (`.m4a`, `.mp3`) or text transcriptions (`.txt`).
   - Using the **Google Gemini 2.5 Flash Free Tier** (15 RPM limit, 1 million token context), it directly processes multi-modal inputs.
   - Outputs a typed Pydantic `AccountMemo`.

2. **Agent Prompt Generation (v1 and v2)**
   - The `AccountMemo` is injected into `agent_builder.py` which guarantees prompt hygiene.
   - It outputs a Retell AI ready `RetellAgentSpec` dictating call rules, fallbacks, and transfers.
   - Variables are mapped without showing internal 'function calling' logic to the agent.

3. **Diffing and Versioning (Onboarding Support)**
   - Onboarding runs pull the existing `v1` memo.
   - It prompts the model to perform a differential update combining old structural logic and new constraints.
   - Finally, `differ.py` generates a `changelog.md` file reflecting exact feature differences (e.g. business hour updates).

## Setup Instructions

### 1. Requirements

Install python requirements and make sure you're using python 3.10+.
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Zero-Cost LLM Configuration
Go to [Google AI Studio](https://aistudio.google.com/app/apikey) and create a free API key.
```bash
export GEMINI_API_KEY="your-free-key-here"
```

### 3. File Structure Setup
In the root directory, create the `inputs/` folder if it doesn't exist:
```
inputs/
  demo/
    customer1_recording_demo.m4a
  onboarding/
    customer1_recording_onboard.m4a
```

## How to Run Locally

You can run individual files:
```bash
# Generate the v1 demo output
python scripts/process_file.py inputs/demo/customer1.m4a --type demo

# Generate the updated v2 onboarding output
python scripts/process_file.py inputs/onboarding/customer1_onboarding.m4a --type onboarding
```

Or you can run the entire dataset through batch processing:
```bash
python scripts/batch_run.py
```

### Where are the outputs stored?
Everything is stored in structured directories under `outputs/`:
```
outputs/
  accounts/
    [account_id]/
      v1/
        memo.json
        agent_spec.json
      v2/
        memo.json
        agent_spec.json
      changelog.md
```

## n8n Orchestration (Alternative Execution)
An n8n workflow export is included at `workflows/n8n-clara-pipeline.json` (mock placeholder).
To execute using n8n:
1. Run n8n locally via Docker: `docker run -it --rm --name n8n -p 5678:5678 -v ~/.n8n:/home/node/.n8n n8nio/n8n`
2. Import the workflow JSON.
3. The workflow watches a designated Google Drive or Local folder, and executes the CLI `scripts/process_file.py` node locally.
4. It then pushes a task creation update to an Asana webhook.


## Limitations and Future Improvements
- **Production Scale**: In production, I would utilize Supabase (Posternetes/PostgREST) to actually house the JSON structured output `AccountMemo` representations instead of Local folders.
- **Transcriptions**: Since Gemini handles both Audio & Text beautifully, the pipeline accepts both. However, Whisper-large-v3 mapped to Groq API could yield even faster pre-processing times if solely dealing with text inputs.

## Retell API Setup Instructions
As required by the zero-cost assignment constraint:
- Create a Free Tier Retell AI account at [retellai.com](https://retellai.com)
- **Important**: Retell does not allow free programmatic Agent Creation via their API on zero-cost tiers. Consequently, this pipeline generates a strict `"Retell Agent Draft Spec JSON"` locally.
- **Manual Import Steps**:
  1. Login to your Retell Dashboard.
  2. Click "Create Agent" -> "Custom Prompt".
  3. Navigate to your generated output folder (`outputs/accounts/<account_id>/v1/agent_spec.json`).
  4. Copy the value of `"system_prompt"` and paste it into the Retell "Agent Prompt" text area.
  5. Scroll down to "Tools" and add a "Transfer Call" tool using the logic provided in `"call_transfer_protocol"`.
  6. Choose the `"voice_style"` referenced in the JSON to match the persona.
  7. Your agent is now ready!
