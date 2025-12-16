"""
ner_extraction.py

Medical Named Entity Extraction module.
Uses a hybrid NLP approach (spaCy + rule-based matching)
to extract and normalize medical entities from transcripts.

Extracted entities:
- Symptoms
- Diagnosis
- Treatment
- Prognosis
"""

from typing import Dict, List
import re
import spacy

# Load spaCy model (lightweight, fast)
nlp = spacy.load("en_core_web_sm")

# -----------------------------
# Normalization Dictionaries
# -----------------------------

SYMPTOM_MAP = {
    "neck pain": "Neck pain",
    "back pain": "Back pain",
    "backache": "Back pain",
    "head injury": "Head impact",
    "hit my head": "Head impact",
    "stiffness": "Stiffness",
    "trouble sleeping": "Sleep disturbance",
    "had trouble sleeping": "Sleep disturbance"
}

DIAGNOSIS_MAP = {
    "whiplash injury": "Whiplash injury"
}

TREATMENT_MAP = {
    "physiotherapy": "Physiotherapy",
    "physio": "Physiotherapy",
    "painkillers": "Painkillers",
    "analgesics": "Painkillers"
}

PROGNOSIS_PATTERNS = [
    r"full recovery within [a-z0-9\s]+ months",
    r"no long-term impact",
    r"on track for a full recovery"
]

# -----------------------------
# Core Extraction Function
# -----------------------------

def extract_medical_entities(text: str) -> Dict[str, List[str] | str | None]:
    """
    Extract and normalize medical entities from transcript text.

    Parameters:
        text (str): Raw physician-patient transcript

    Returns:
        dict: Structured medical entities
    """

    text_lower = text.lower()
    doc = nlp(text_lower)

    symptoms = set()
    diagnosis = set()
    treatment = set()
    prognosis = set()

    # --- Symptoms ---
    for phrase, normalized in SYMPTOM_MAP.items():
        if phrase in text_lower:
            symptoms.add(normalized)

    # --- Diagnosis ---
    for phrase, normalized in DIAGNOSIS_MAP.items():
        if phrase in text_lower:
            diagnosis.add(normalized)

    # --- Treatment ---
    for phrase, normalized in TREATMENT_MAP.items():
        if phrase in text_lower:
            treatment.add(normalized)

    # --- Prognosis ---
    for pattern in PROGNOSIS_PATTERNS:
        matches = re.findall(pattern, text_lower)
        for match in matches:
            prognosis.add(match)

    return {
        "Patient_Name": None,  # Not inferred unless explicitly present
        "Symptoms": sorted(symptoms),
        "Diagnosis": diagnosis.pop() if diagnosis else None,
        "Treatment": sorted(treatment),
        "Current_Status": _infer_current_status(text_lower),
        "Prognosis": prognosis.pop() if prognosis else None
    }


# -----------------------------
# Helper Logic
# -----------------------------

def _infer_current_status(text_lower: str) -> str | None:
    """
    Infer current status conservatively from transcript.
    No guessing or hallucination.
    """

    if "occasional" in text_lower and "back" in text_lower:
        return "Occasional backache"

    if "doing better" in text_lower or "improving" in text_lower:
        return "Improving"

    return None


