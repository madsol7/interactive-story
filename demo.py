import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
 
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
 
client = genai.Client(api_key=api_key) if api_key else None
 
MODEL_NAME = "gemini-3.5-flash-lite"

# Museum exhibits and their fixed outcomes
exhibits = {
    "Roman coin": "The visitor reads a label explaining that the coin is about 2,000 years old.",
    "Dinosaur fossil": "The visitor learns that the fossil belongs to a plant-eating dinosaur.",
    "Ancient pottery": "The visitor discovers that the pot was used for storing food."
}


def make_prompt(name, exhibit, outcome):
    """Create a prompt for the Gemini API."""

    return f"""
Role: You are a friendly museum exhibit narrator.

Context:
A visitor named {name} is looking at the {exhibit} exhibit.

Fixed outcome:
{outcome}

Constraints:
- Write in second person (you / your).
- Use a friendly, curious tone.
- Describe the discovery in 30-50 words.
- Do not change the fixed outcome.
- Do not let the visitor take objects or invent new discoveries.
- Do not introduce new decisions for the visitor.

Return only the short description.
"""


def generate_description(prompt, fallback):
    """Generate an exhibit description using Gemini."""

    if client is None:
        return fallback, "No API key found. Showing fallback description."

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        description = response.text

        if not description:
            return fallback, "Gemini returned no text. Showing fallback description."

        return description.strip(), None

    except Exception as error:
        return fallback, (
            f"The API request failed ({type(error).__name__}). "
            "Showing the fallback description."
        )


# Streamlit application
st.set_page_config(
    page_title="Museum",
    page_icon="🏛️"
)

st.title("🏛️ Museum")

# Visitor input
name = st.text_input("Visitor's name")

# Exhibit selection
exhibit = st.selectbox(
    "Choose an exhibit",
    list(exhibits.keys())
)

# Get the fixed outcome
outcome = exhibits[exhibit]

# Create the prompt
prompt = make_prompt(name, exhibit, outcome)

# Generate description
if st.button("✨ Generate a description"):

    if not name.strip():
        st.warning("Please enter your name first.")

    else:
        with st.spinner("Asking Gemini..."):

            description, message = generate_description(
                prompt,
                outcome
            )

        st.write(description)

        if message:
            st.warning(message)
