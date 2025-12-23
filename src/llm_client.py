import json
import re
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage

load_dotenv()

MODEL = "mistralai/Mistral-7B-Instruct-v0.2"

endpoint = HuggingFaceEndpoint(
    repo_id=MODEL,
    temperature=0.2,
    max_new_tokens=800,
)

llm = ChatHuggingFace(llm=endpoint)

def call_llm(prompt: str):
    response = llm.invoke([HumanMessage(content=prompt)])
    raw = response.content.strip()

    
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass

   
    objects = re.findall(r"\{[\s\S]*?\}", raw)

    if not objects:
        raise ValueError(
            "No JSON objects found in LLM output.\n"
            "----- RAW OUTPUT -----\n"
            f"{raw}"
        )

   
    json_array_text = "[" + ",".join(objects) + "]"

    try:
        return json.loads(json_array_text)
    except json.JSONDecodeError as e:
        raise ValueError(
            "Failed to convert LLM output into valid JSON.\n"
            "----- RECONSTRUCTED JSON -----\n"
            f"{json_array_text}"
        ) from e
