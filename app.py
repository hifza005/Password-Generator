import streamlit as st
import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Checking password criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password)
    lowercase_criteria = re.search(r'[a-z]', password)
    digit_criteria = re.search(r'\d', password)
    special_char_criteria = re.search(r'[@$!%*?&]', password)

    # Evaluating password strength
    if length_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if digit_criteria:
        strength += 1
    if special_char_criteria:
        strength += 1

    # Assigning strength levels
    if strength == 5:
        remarks = "💪 Very Strong"
    elif strength == 4:
        remarks = "🟡 Strong"
    elif strength == 3:
        remarks = "🌘 Moderate"
    elif strength == 2:
        remarks = "❄️ Weak"
    else:
        remarks = "💮 Very Weak"

    return remarks, strength


st.markdown(
    """
    <style>
        .stApp {
            background-color: lightgreen; /* Change this to any color you want */
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Streamlit App UI
st.markdown(
    """
  <h1 style="text-align: center; color: red; font-family: Times new roman, sans-serif; font-size: 40px; background-color: black; padding: 10px;">
    🔏 Password Strength Meter
</h1>


    """,
    unsafe_allow_html=True
)

password = st.text_input("Enter your password", type="password")

# Define strength_score before using it
strength_score = 0
strength_label = ""

if password:
    strength_label, strength_score = check_password_strength(password)

    # Displaying strength level
    st.subheader(f"Password Strength: {strength_label}")

    # Progress bar (fixing error)
    progress_colors = ["red", "orange", "purple", "lightgreen", "green"]
    progress_percentage = (strength_score / 5) * 100

    st.markdown(f"""
        <div style="width: 100%; background-color: #ddd; border-radius: 5px;">
            <div style="width: {progress_percentage}%; 
                        background-color: {progress_colors[strength_score - 1] if strength_score > 0 else 'red'}; 
                        height: 20px; border-radius: 5px;">
            </div>
        </div>
    """, unsafe_allow_html=True)