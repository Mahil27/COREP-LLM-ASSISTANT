import os
import json
from dotenv import load_dotenv
from groq import Groq
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from schema import CorepOutput

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

retriever = db.as_retriever(search_kwargs={"k": 3})

def run_query(question):

    docs = retriever.invoke(question)
    context = "\n\n".join(d.page_content for d in docs)

    prompt = f"""
You are a regulatory reporting assistant.

Using the provided context, extract structured COREP data.

Return ONLY valid JSON with keys:
capital_type
amount
risk_weight
template_section

Context:
{context}

Question:
{question}
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",

        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    raw = completion.choices[0].message.content.strip()
    import re

    match = re.search(r"\{.*?\}", raw, re.DOTALL)

    if not match:   
        raise ValueError("No JSON found in model response")

    cleaned = match.group()

    parsed = json.loads(cleaned)

    parsed["amount"] = str(parsed.get("amount", ""))
    parsed["risk_weight"] = str(parsed.get("risk_weight", ""))
    parsed["capital_type"] = str(parsed.get("capital_type", ""))
    parsed["template_section"] = str(parsed.get("template_section", ""))

    result = CorepOutput(**parsed)


    return result, docs
