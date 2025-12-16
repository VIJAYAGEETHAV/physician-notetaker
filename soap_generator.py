"""
soap_generator.py

Generates a structured SOAP note from extracted medical entities
and transcript text using deterministic, rule-based logic.
"""

from typing import Dict, Any


def generate_soap_note(
    transcript: str,
    medical_summary: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Generate SOAP note from transcript and structured medical summary.
    """

    text_lower = transcript.lower()

    # -----------------------------
    # Subjective
    # -----------------------------

    subjective = {
        "Chief_Complaint": _chief_complaint(medical_summary),
        "History_of_Present_Illness": _history_of_present_illness(transcript)
    }

    # -----------------------------
    # Objective
    # -----------------------------

    objective = {
        "Physical_Exam": _physical_exam(text_lower),
        "Observations": _observations(text_lower)
    }

    # -----------------------------
    # Assessment
    # -----------------------------

    assessment = {
        "Diagnosis": medical_summary.get("Diagnosis"),
        "Severity": _severity_assessment(text_lower)
    }

    # -----------------------------
    # Plan
    # -----------------------------

    plan = {
        "Treatment": _treatment_plan(medical_summary),
        "Follow-Up": _follow_up(text_lower)
    }

    return {
        "Subjective": subjective,
        "Objective": objective,
        "Assessment": assessment,
        "Plan": plan
    }


# -----------------------------
# Helper Functions
# -----------------------------

def _chief_complaint(summary: Dict[str, Any]) -> str | None:
    symptoms = summary.get("Symptoms", [])
    if symptoms:
        return ", ".join(symptoms)
    return None


def _history_of_present_illness(transcript: str) -> str:
    """
    Conservative summarization of patient-reported history.
    No abstraction beyond original wording.
    """
    return transcript.strip()


def _physical_exam(text_lower: str) -> str | None:
    if "full range of movement" in text_lower or "full range of motion" in text_lower:
        return "Full range of motion in affected areas, no tenderness noted."
    return None


def _observations(text_lower: str) -> str | None:
    if "everything looks good" in text_lower:
        return "Patient appears in normal health."
    return None


def _severity_assessment(text_lower: str) -> str:
    if "improving" in text_lower or "doing better" in text_lower:
        return "Mild, improving"
    return "Stable"


def _treatment_plan(summary: Dict[str, Any]) -> str | None:
    treatments = summary.get("Treatment", [])
    if treatments:
        return ", ".join(treatments)
    return None


def _follow_up(text_lower: str) -> str | None:
    if "come back" in text_lower or "follow-up" in text_lower:
        return "Patient advised to return if symptoms worsen."
    return None


