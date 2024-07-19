import streamlit as st

st.title("POST - TEST")

# Questions and answers
questions = [
    {
        "question": "What is the primary function of the A4988 stepper driver in a CNC plotter?",
        "options": ["A. To control the speed of the motor", "B. To control the direction of the motor", "C. To control the step resolution of the motor", "D. To control the current output of the motor"],
        "answer": "D. To control the current output of the motor"
    },
    {
        "question": "What is the purpose of the timing belt in a CNC plotter?",
        "options": ["A. To transmit power", "B. To transmit rotation", "C. To provide precise displacement", "D. To provide precise positioning"],
        "answer": "C. To provide precise displacement"
    },
    {
        "question": "What is the primary language used to control CNC machines?",
        "options": ["A. G-code", "B. Python", "C. C++", "D. Java"],
        "answer": "A. G-code"
    },
    {
        "question": "What is the primary purpose of the Universal G Code Sender (UGS)?",
        "options": ["A. To create G-code from designs", "B. To connect and control 2D plotters", "C. To provide power to the CNC machine", "D. To design 3D models"],
        "answer": "B. To connect and control 2D plotters"
    },
    {
        "question": "What is the primary advantage of using a CNC 2D Plotter over manual plotting methods?",
        "options": ["a) Increased speed", "b) Increased accuracy", "c) Increased cost", "d) Increased complexity"],
        "answer": "b) Increased accuracy"
    }
]

# Initialize session state for answers
if "answers" not in st.session_state:
    st.session_state["answers"] = [None] * len(questions)

# Quiz form
with st.form("quiz_form"):
    for i, q in enumerate(questions):
        st.write(f"Q{i+1}: {q['question']}")
        st.session_state["answers"][i] = st.radio("", q["options"], key=f"q{i}", index=None)  # Prevent default selection
    
    submitted = st.form_submit_button("SUBMIT") 

# Calculate score and display results
if submitted:
    correct_count = 0
    for i, q in enumerate(questions):
        st.write(f"Q{i+1}: {q['question']}")
        
        # Display user's answer with feedback
        user_answer = st.session_state["answers"][i]
        if user_answer == q["answer"]:
            correct_count += 1
            st.markdown(f"✅ {user_answer} <span style='background-color:lightgreen; padding: 5px;'>   </span>", unsafe_allow_html=True)
        else:
            st.markdown(f"❌ {user_answer} <span style='background-color:lightcoral; padding: 5px;'>   </span>", unsafe_allow_html=True)
        st.write(f"Correct answer: {q['answer']}")
        st.write("")

    st.write(f"Your score: {correct_count} out of {len(questions)}")

# Add some styling to the app
st.markdown("""
<style>
body {
  background-color: #f2f2f2;
}

.stForm {
  background-color: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

.stRadio {
  margin-bottom: 10px;
}

.stButton {
  background-color: #007bff;
  color: black;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-align: center; 
}

.stButton:hover {
  background-color: #0069d9;
}
</style>
""", unsafe_allow_html=True)