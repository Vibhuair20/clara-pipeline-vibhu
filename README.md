# Clara Answers Automation Pipeline

Hey! Welcome to my Clara Answers automation project. I built this pipeline to handle onboarding and updating AI voice agents completely automatically. My main goal was to make this 100% zero-cost while still writing production-grade code that scales.

## How it Works

1. **Audio Extraction**
   - I wrote a Python script that takes in raw demo calls or onboarding audio files.
   - To keep things free, it feeds the audio straight into the Google Gemini free tier.
   - Instead of letting the AI guess, my code forces it to spit out a strict Pydantic JSON schema so there's no hallucination.

2. **Building the Agent**
   - Once I have the clean JSON data, my `agent_builder.py` script injects it into a hardcoded template. 
   - This keeps the prompt super clean and stable before sending it to Retell AI.

3. **Versioning & Diffing**
   - When a client does a new Onboarding call, my code automatically checks the database for their old "version 1" profile.
   - It gracefully merges the new rules (like "new gas station added") and generates a clean Markdown changelog!

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

## n8n Setup
To execute the automation flow using n8n:

1. **Local Run Steps (Docker Compose)**:
   A `docker-compose.yml` file is included in the root directory. To spin up n8n instantly, simply ensure your Docker daemon is running and execute:
   ```bash
   docker compose up -d
   ```

2. **Environment Variables**:
   Your n8n environment needs access to:
   - `GEMINI_API_KEY`: Sourced automatically if you place it in a `.env` file in the root directory.
   - The current directory is automatically mounted to `/workspace` inside the container so the Execute Command nodes can call the python scripts.

3. **Workflow Import Steps**:
   - Open your local n8n instance at `http://localhost:5678`.
   - Click "Add Workflow" in the top right.
   - Click the "Options" menu (three dots) -> "Import from File".
   - Select the `workflows/n8n-clara-pipeline.json` file included in this repository.

4. **Run All Dataset (Batch Method)**:
   Instead of using n8n to process webhooks one by one, you can run the entire dataset instantly via the included batch script:
   ```bash
   python scripts/batch_run.py
   ```
   *This automatically parses every demo and onboarding recording, generates the v1 and v2 specs, writes the changelogs, and spits out a JSON summary metric.*

---

## Retell API Automation

1. **Create an Account:** Go to [retellai.com](https://retellai.com) and create an account.
2. **Setup your Key:** Grab your API key and throw it in your `.env` file under `RETELL_API_KEY`.
3. **Automatic Deployment:** 
   - When you run the batch script, I built a `RetellClient` that automatically hits their `create-retell-llm` and `create-agent` API endpoints. 
   - It will literally deploy the newly generated agents straight into your Retell dashboard without you having to click anything!
   - *(Note: If you don't provide an API key, my code gracefully falls back to a mocked "zero-cost" integration layer and just runs locally).*

4. **Testing it out:**
   - Go to your Retell dashboard online.
   - Click on the newly created agent from the list.
   - Hit **Test Chat** or **Web Call** to try out the logic it extracted from the audio!
