Deployed Link : https://corep-llm-assistant.streamlit.app/

COREP LLM Reporting Assistant (Prototype)

Overview

This project is a prototype LLM-powered regulatory reporting assistant designed to assist in COREP-style reporting using retrieval-augmented generation (RAG).

The system retrieves relevant regulatory rulebook sections and uses a large language model to extract structured reporting data. It demonstrates how LLMs can support structured regulatory reporting workflows with validation and audit traceability.

This is a functional prototype built using a small subset of regulatory text for demonstration purposes.

Features

Retrieval-Augmented Generation (RAG) pipeline

Local embeddings using sentence-transformers

FAISS vector search for regulatory context retrieval

Groq Llama 3.1 model for structured data extraction

Structured JSON output validated using Pydantic

Basic validation layer for reporting inconsistencies

Audit trail showing retrieved regulatory context

Streamlit-based interactive UI

Architecture

User Query
→ Vector Retrieval (FAISS)
→ Context Injection
→ LLM Structured Extraction
→ Schema Validation
→ Report Display + Audit Trail

Technology Stack

Python

Streamlit

LangChain (community components)

FAISS

Sentence Transformers

Groq API (Llama 3.1)

Pydantic

Prototype Scope

This implementation is a proof-of-concept prototype using a small sample of regulatory text (rulebook.txt) for demonstration.

It is not a production-grade regulatory system and does not cover full PRA/COREP documentation. The focus is on demonstrating:

LLM integration into structured workflows

Retrieval-based grounding

JSON extraction and validation

Explainability via audit trace

How to Run

Install dependencies:

pip install -r requirements.txt


Create .env file:

GROQ_API_KEY=your_api_key_here


Build vector index:

python ingest.py


Run application:

python -m streamlit run app.py

Example Use Case

User enters:

Bank has CET1 capital of €5,000,000 with 100% risk weight. Where should it be reported?

System outputs:

Capital Type

Amount

Risk Weight

Template Section

Retrieved regulatory context used for reasoning

Purpose

This project demonstrates how LLMs can assist in regulatory reporting workflows by converting unstructured regulatory text into structured reporting outputs with traceability and validation.
