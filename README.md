## Setup Instructions

**Python Version:** 3.9+

Install project dependencies:
```bash
pip install -r requirements.txt

Download required spaCy model:

python -m spacy download en_core_web_sm


Run the pipeline:

python main.py

## Task Details

This project implements an AI pipeline to process physician–patient conversations and produce:

- **Medical NLP Summarization**
  - Extraction of Symptoms, Diagnosis, Treatment, and Prognosis
- **Sentiment Analysis**
  - Classifies patient sentiment as Anxious, Neutral, or Reassured
- **Intent Detection**
  - Identifies patient intent such as reporting symptoms or seeking reassurance
- **SOAP Note Generation (Bonus)**
  - Structures the conversation into Subjective, Objective, Assessment, and Plan

All outputs are generated in structured JSON format and are designed to avoid hallucination by extracting only explicitly stated medical information.
