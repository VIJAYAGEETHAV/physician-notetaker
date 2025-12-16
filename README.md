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
''' 
physician-notetaker/
│
├── main.py
├── ner_extraction.py
├── sentiment_intent.py
├── soap_generator.py
│
├── outputs/
│ ├── medical_summary.json
│ ├── sentiment_intent.json
│ └── soap_note.json
│
├── sample_input_output.json
├── requirements.txt
├── .gitignore
└── README.md
'''


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

## Design Decisions

- **Hybrid NLP approach over pure LLMs** to ensure deterministic, reproducible behavior suitable for production environments  
- **Transformer-based sentiment analysis** used in inference-only mode, avoiding unnecessary fine-tuning to maintain stability and simplicity  
- **Modular system architecture** that enables easy extension, replacement, or independent testing of components  
- **Zero hallucination tolerance** — all outputs are strictly grounded in the provided input text  

These decisions reflect **production-oriented AI engineering practices**, not experimental prototyping.

---

## Limitations & Future Improvements

- **Speaker-aware attribution** to better handle multi-turn physician–patient conversations  
- **Domain-specific medical language models** such as BioBERT or ClinicalBERT for improved clinical accuracy  
- **Confidence scoring mechanisms** across aggregated patient utterances  
- **API-based deployment** to enable seamless integration with clinical systems  

---

## Conclusion

This project demonstrates the ability to:

- Translate ambiguous requirements into a **structured, end-to-end AI system**  
- Apply **NLP and transformer models pragmatically** rather than heuristically  
- Build **explainable, healthcare-ready pipelines** aligned with real-world constraints  

The solution prioritizes **clarity, reliability, and extensibility**, aligning closely with expectations for production-grade AI systems in healthcare.

---

**Author:** Vijayageetha V  
**Role Applied:** AI Engineer Intern – Emitrr
