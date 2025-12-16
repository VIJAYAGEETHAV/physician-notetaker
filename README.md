# 🩺 Physician Notetaker – AI Engineer Intern Assignment (Emitrr)

## Overview

This project implements an **end‑to‑end AI‑driven Physician Notetaker system** that converts raw doctor–patient conversations into structured, clinically meaningful outputs. The solution focuses on **medical NLP, transformer‑based sentiment analysis, and healthcare documentation automation**, with an emphasis on **deterministic, production‑ready design** rather than ad‑hoc experimentation.

The pipeline mirrors how real-world healthcare AI systems are built: modular, explainable, reproducible, and robust to noisy conversational input.

---

## Key Capabilities

### 1. Medical NLP Summarization

* Extracts **Symptoms, Diagnosis, Treatment, Prognosis** from raw transcripts
* Converts unstructured dialogue into a **structured medical summary (JSON)** suitable for EHR systems
* Uses a **hybrid NLP approach** (spaCy + rule-based logic) for reliability and explainability

### 2. Sentiment & Intent Analysis

* Applies a **Transformer-based model (DistilBERT)** for patient sentiment classification
* Detects patient **intent** (e.g., reporting symptoms, seeking reassurance)
* Outputs confidence-scored, interpretable results

### 3. SOAP Note Generation (Bonus)

* Automatically generates a structured **SOAP note** (Subjective, Objective, Assessment, Plan)
* Designed for **clinical readability** and downstream medical workflows
* Demonstrates healthcare-domain understanding beyond basic NLP

---

## Project Structure

```
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
```

---

## Setup Instructions

### Python Version
- Python **3.9+** recommended

### Install Dependencies

pip install -r requirements.txt

###  Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```
---

## How to Run

Execute the complete pipeline:

```bash
python main.py
```

This will generate:

* `output/medical_summary.json`
* `output/sentiment.json`
* `output/soap_note.json`

---

## Design Decisions (Recruiter Perspective)

* **Hybrid NLP over pure LLMs**: Ensures deterministic behavior, critical for healthcare use cases
* **Transformer-based sentiment analysis**: Demonstrates modern NLP competence without unnecessary fine-tuning
* **Modular architecture**: Each component can be independently tested, replaced, or scaled
* **No hallucinated data**: All outputs are grounded in the provided transcript

This design reflects **production thinking**, not just assignment completion.

---

## Limitations & Future Improvements

* Speaker-aware entity filtering for finer symptom attribution
* Domain-specific medical NER models (e.g., BioBERT / ClinicalBERT)
* Confidence aggregation across multiple patient utterances
* REST API wrapper for integration into clinical systems

---

## Conclusion

This project demonstrates the ability to:

* Translate ambiguous requirements into a clear AI system
* Apply NLP and transformers pragmatically
* Build explainable, healthcare-ready AI pipelines

The solution is intentionally **simple, reliable, and extensible**, aligning with how real AI systems are evaluated and deployed in production environments.

---

