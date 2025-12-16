# 🩺 Physician Notetaker – Medical NLP Pipeline (Emitrr Assignment)

## Overview

This project implements an **end-to-end Medical NLP pipeline** that converts raw physician–patient conversations into **structured clinical outputs**.  
The solution focuses on **robust information extraction, sentiment & intent analysis, and automated SOAP note generation**, designed with **deterministic, production-ready engineering principles**.

The pipeline mirrors real-world healthcare AI systems by being **modular, explainable, reproducible, and resilient to noisy conversational input**.

---

## Key Capabilities

### 1. Medical Information Extraction
- Extracts **Symptoms, Diagnosis, Treatment, Current Status, Prognosis**
- Converts unstructured text into a **structured medical summary (JSON)**
- Uses a **hybrid NLP approach (spaCy + rule-based normalization)** for reliability and transparency

### 2. Sentiment & Intent Analysis
- Uses a **Transformer-based model (DistilBERT)** for sentiment detection
- Identifies patient **intent** such as reporting symptoms or expressing concern
- Inference-only design for fast, stable execution

### 3. SOAP Note Generation
- Automatically generates a structured **SOAP note**
- Output designed for **clinical readability**
- Demonstrates healthcare workflow awareness beyond basic NLP

---

## Project Structure

physician-notetaker/
│
├── main.py # Entry point for the full pipeline
├── ner_extraction.py # Medical entity extraction & normalization
├── sentiment_intent.py # Transformer-based sentiment & intent analysis
├── soap_generator.py # SOAP note generator
│
├── outputs/
│ ├── medical_summary.json # Structured medical summary
│ ├── sentiment_intent.json # Sentiment & intent output
│ └── soap_note.json # Generated SOAP note
│
├── sample_input_output.json # Example input & expected output
├── requirements.txt # Python dependencies
├── .gitignore
└── README.md

yaml
Copy code

---

## Setup Instructions

### Python Version
- Python **3.9+** recommended

### Install Dependencies
```bash
pip install -r requirements.txt
Download spaCy Model
bash
Copy code
python -m spacy download en_core_web_sm
How to Run
Run the complete pipeline:

bash
Copy code
python main.py
You will be prompted to paste a physician–patient transcript.
The pipeline generates structured outputs in the outputs/ directory.

Sample Output (Excerpt)
json
Copy code
{
  "Symptoms": ["Back pain", "Head impact"],
  "Diagnosis": null,
  "Treatment": ["Physiotherapy", "Painkillers"],
  "Current_Status": "Occasional backache",
  "Prognosis": "Full recovery expected within six months"
}
Design Decisions
Hybrid NLP instead of pure LLMs for deterministic behavior

Transformer-based sentiment analysis without unnecessary fine-tuning

Modular architecture enabling easy extension or replacement

No hallucinated data — outputs are strictly grounded in input text

These choices reflect production-oriented AI engineering, not experimental prototyping.

Limitations & Future Improvements
Speaker-aware attribution for multi-turn conversations

Domain-specific medical models (BioBERT / ClinicalBERT)

Confidence scoring across multiple patient utterances

API-based deployment for clinical integration

Conclusion
This project demonstrates the ability to:

Translate ambiguous requirements into a structured AI system

Apply NLP and transformers pragmatically

Build explainable, healthcare-ready pipelines

The solution prioritizes clarity, reliability, and extensibility, aligning with real-world AI product expectations.

Author: Vijayageetha V
Role Applied: AI Engineer Intern – Emitrr

markdown
Copy code
