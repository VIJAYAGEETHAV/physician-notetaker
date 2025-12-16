"""
main.py

Entry point for the Physician Notetaker pipeline.
Runs medical NER, sentiment & intent analysis, and SOAP note generation.
"""

import json
import os

from ner_extraction import extract_medical_entities
from sentiment_intent import analyze_sentiment_and_intent
from soap_generator import generate_soap_note


def run_pipeline(transcript: str) -> None:
    """
    Run the full Physician Notetaker pipeline on a transcript.
    """

    # Ensure output directory exists
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    # -----------------------------
    # Step 1: Medical NER
    # -----------------------------
    medical_summary = extract_medical_entities(transcript)

    # -----------------------------
    # Step 2: Sentiment & Intent
    # -----------------------------
    sentiment_intent = analyze_sentiment_and_intent(transcript)

    # -----------------------------
    # Step 3: SOAP Note
    # -----------------------------
    soap_note = generate_soap_note(transcript, medical_summary)

    # -----------------------------
    # Print Outputs (Reviewer-Friendly)
    # -----------------------------
    print("\n=== MEDICAL SUMMARY ===")
    print(json.dumps(medical_summary, indent=2))

    print("\n=== SENTIMENT & INTENT ===")
    print(json.dumps(sentiment_intent, indent=2))

    print("\n=== SOAP NOTE ===")
    print(json.dumps(soap_note, indent=2))

    # -----------------------------
    # Save Outputs (Production-Ready)
    # -----------------------------
    _save_json(os.path.join(output_dir, "medical_summary.json"), medical_summary)
    _save_json(os.path.join(output_dir, "sentiment_intent.json"), sentiment_intent)
    _save_json(os.path.join(output_dir, "soap_note.json"), soap_note)


def _save_json(path: str, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    # Example usage: replace with ANY transcript
    transcript_input = input("Paste physician-patient transcript:\n\n")
    run_pipeline(transcript_input)
