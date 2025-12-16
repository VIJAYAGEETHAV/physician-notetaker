"""
sentiment_intent.py

Patient Sentiment and Intent Analysis.
Uses DistilBERT for sentiment inference and
rule-based logic for intent detection.
"""

from typing import Dict
from transformers import pipeline

# Load sentiment analysis pipeline (inference only)
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# -----------------------------
# Keyword Rules for Intent
# -----------------------------

INTENT_RULES = {
    "Seeking reassurance": [
        "will i be okay",
        "should i worry",
        "do i need to worry",
        "is this serious",
        "affect me in the future"
    ],
    "Expressing concern": [
        "worried",
        "concerned",
        "anxious",
        "nervous",
        "scared"
    ],
    "Reporting symptoms": [
        "pain",
        "hurt",
        "ache",
        "stiff",
        "discomfort"
    ]
}

ANXIETY_KEYWORDS = [
    "worried",
    "anxious",
    "nervous",
    "concerned"
]

# -----------------------------
# Core Analysis Function
# -----------------------------

def analyze_sentiment_and_intent(text: str) -> Dict[str, str]:
    """
    Analyze patient sentiment and intent from text.
    """

    text_lower = text.lower()

    # --- Sentiment Analysis ---
    model_output = sentiment_model(text)[0]
    label = model_output["label"]

    sentiment = _map_sentiment(label, text_lower)

    # --- Intent Detection ---
    intent = _detect_intent(text_lower)

    return {
        "Sentiment": sentiment,
        "Intent": intent
    }

# -----------------------------
# Helper Functions
# -----------------------------

def _map_sentiment(model_label: str, text_lower: str) -> str:
    """
    Map model sentiment to medical sentiment categories.
    """

    # Safety override: anxiety words dominate
    if any(word in text_lower for word in ANXIETY_KEYWORDS):
        return "Anxious"

    if model_label == "NEGATIVE":
        return "Anxious"
    elif model_label == "POSITIVE":
        return "Reassured"
    else:
        return "Neutral"


def _detect_intent(text_lower: str) -> str:
    """
    Detect patient intent using rule-based priority logic.
    """

    for intent, phrases in INTENT_RULES.items():
        for phrase in phrases:
            if phrase in text_lower:
                return intent

    return "Other"


