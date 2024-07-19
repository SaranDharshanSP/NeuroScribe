import streamlit as st

st.title("FREQUENTLY ASKED QUESTIONS")
# Define questions and answers as dictionaries
questions = {
    "q1": "What is a CNC plotter?",
    "q2": "How many degrees of freedom does a typical CNC plotter have?",
    "q3": "What is G-code, and how is it used in a CNC plotter?",
    "q4": "What are the limitations of a CNC plotter?",
    "q5": "What are the advantages of using a CNC plotter?",
}

answers = {
    "q1": "A CNC plotter is a computer-controlled machine that uses stepper motors to move a pen or other tool along a predetermined path to create a design or image on a surface.",
    "q2": "A typical CNC plotter has 2 degrees of freedom (2 DOF), controlling movement along the X and Y axes. Some advanced models may have 3 DOF, adding Z-axis control for more complex designs.",
    "q3": "G-code is a programming language used to control CNC machines. It provides instructions for the machine to follow, including the movement of the motor and the actions to perform. In a CNC plotter, G-code is used to generate the design or image that the machine will create.",
    "q4": "The limitations of a CNC plotter include the need for precise calibration and setup, the potential for errors if the G-code is not properly written, and the cost of the machine and its components.",
    "q5": "CNC plotters offer:\nPrecision and accuracy\nSpeed and efficiency\nRepeatability\nReduced labor costs\nAbility to handle complex designs"
}

# Display questions as buttons with plus symbol
for question_id in questions:
    if st.button(f"➕ {questions[question_id]}"):
        st.markdown(f"**{answers[question_id]}**")