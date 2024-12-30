import os
from termcolor import colored

# API Configuration
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
PERPLEXITY_BASE_URL = "https://api.perplexity.ai"
MODEL_NAME = "llama-3.1-sonar-large-128k-online"

# System message for fact checking
SYSTEM_MESSAGE = """You are a professional fact checker. Your role is to:
1. Analyze the given text or image content
2. Verify the claims made
3. Provide accurate information with sources
4. Highlight any misinformation
5. Rate the overall accuracy on a scale of 1-10
Please be thorough and objective in your analysis."""

def print_status(message: str, status: str = "info"):
    """Print colored status messages"""
    colors = {
        "info": "cyan",
        "success": "green",
        "error": "red",
        "warning": "yellow"
    }
    print(colored(message, colors.get(status, "white"))) 