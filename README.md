# AI-Powered Cloud Cost Optimization Tool

An AI-driven system that analyzes cloud usage and billing data to provide actionable cost optimization recommendations .

---

## Features

- Convert free-text project description into structured JSON
- Generate realistic mock cloud billing data using LLMs
- Analyze monthly cloud costs against a defined budget
- Provide AI-powered cost optimization recommendations
- CLI-based workflow for easy testing and extension

---

##  Tech Stack

**Backend:** Python  
**LLM:** Hugging Face (Mistral-7B-Instruct)  
---

### Tools used:- ChatGPT.

### Required Accounts
- **Hugging Face Account**
  - Create an account at https://huggingface.co
  - Generate an **Access Token** 

---

### Python Dependencies
The project relies on the following core Python libraries:

- `langchain`
- `langchain-huggingface`
- `huggingface-hub`
- `python-dotenv`
- `requests`

All dependencies are installed automatically using:

```bash
pip install -r requirements.txt

### The access token should be placed in .env file with the same variable name as provided below
HUGGINGFACEHUB_API_TOKEN=YOUR_TOKEN

