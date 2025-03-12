import streamlit as st

# Define the questions and choices
questions = [
    "You find it easy to stay relaxed and optimistic even under stressful situations.",
    "You prefer to be around others rather than being alone.",
    "You tend to focus more on the present than the future.",
    "You are more inclined to follow your heart than your head.",
    "You prefer to have a planned schedule rather than being spontaneous.",
    "You are more comfortable with abstract ideas than concrete details.",
    "You often prioritize others' feelings over logical analysis.",
    "You enjoy being the center of attention in social gatherings.",
    "You prefer to make decisions based on objective criteria rather than personal values.",
    "You are more comfortable with routines and familiar environments."
]

choices = [
    ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
    ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
    ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
    ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
    ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
    ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
    ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
    ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
    ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
    ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"]
]

# Define the MBTI dimensions
dimensions = {
    "E-I": 0,  # Extraversion - Introversion
    "S-N": 0,  # Sensing - Intuition
    "T-F": 0,  # Thinking - Feeling
    "J-P": 0   # Judging - Perceiving
}

# Define the scoring for each question
scoring = [
    {"Strongly Agree": "E", "Agree": "E", "Disagree": "I", "Strongly Disagree": "I"},
    {"Strongly Agree": "E", "Agree": "E", "Disagree": "I", "Strongly Disagree": "I"},
    {"Strongly Agree": "S", "Agree": "S", "Disagree": "N", "Strongly Disagree": "N"},
    {"Strongly Agree": "F", "Agree": "F", "Disagree": "T", "Strongly Disagree": "T"},
    {"Strongly Agree": "J", "Agree": "J", "Disagree": "P", "Strongly Disagree": "P"},
    {"Strongly Agree": "N", "Agree": "N", "Disagree": "S", "Strongly Disagree": "S"},
    {"Strongly Agree": "F", "Agree": "F", "Disagree": "T", "Strongly Disagree": "T"},
    {"Strongly Agree": "E", "Agree": "E", "Disagree": "I", "Strongly Disagree": "I"},
    {"Strongly Agree": "T", "Agree": "T", "Disagree": "F", "Strongly Disagree": "F"},
    {"Strongly Agree": "J", "Agree": "J", "Disagree": "P", "Strongly Disagree": "P"}
]

# Streamlit app
st.title("Personality Analysis Questionnaire")
st.markdown("**Answer the following questions to determine your MBTI personality type.**")

# Collect user responses
responses = []
for i, question in enumerate(questions):
    st.markdown(f"**{i+1}. {question}**")
    response = st.radio("", choices[i], key=f"q{i}", index=0)
    responses.append(response)
    st.write("")  # Add some space between questions

# Calculate the MBTI type
if st.button("Submit", key="submit-button", help="Click to submit your responses"):
    for i, response in enumerate(responses):
        dimension = scoring[i][response]
        if dimension in ["E", "S", "T", "J"]:
            if dimension == "E":
                dimensions["E-I"] += 1
            elif dimension == "S":
                dimensions["S-N"] += 1
            elif dimension == "T":
                dimensions["T-F"] += 1
            elif dimension == "J":
                dimensions["J-P"] += 1
        else:
            if dimension == "I":
                dimensions["E-I"] -= 1
            elif dimension == "N":
                dimensions["S-N"] -= 1
            elif dimension == "F":
                dimensions["T-F"] -= 1
            elif dimension == "P":
                dimensions["J-P"] -= 1

    # Determine the MBTI type
    mbti_type = ""
    mbti_type += "E" if dimensions["E-I"] >= 0 else "I"
    mbti_type += "S" if dimensions["S-N"] >= 0 else "N"
    mbti_type += "T" if dimensions["T-F"] >= 0 else "F"
    mbti_type += "J" if dimensions["J-P"] >= 0 else "P"

    st.markdown(f"**Your MBTI personality type is: {mbti_type}**")
