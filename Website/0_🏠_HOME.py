import streamlit as st

st.set_page_config(
    page_title="Neuroscribe: Home",
    page_icon="🧠", 
    layout="wide",
)

st.markdown(
    """
    <style>
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        padding: 50px;
        background-color: #f8f9fa; /* Light Gray Background */
        border-radius: 10px;
        box-shadow: 5px 5px 15px #888888; /* Light Gray Shadow */
    }

    .title {
        font-size: 64px;
        font-weight: bold;
        color: #343a40; /* Dark Gray */
        margin-bottom: 20px;
    }

    .pitch {
        font-size: 30px;
        font-style: italic;
        color: #007bff; /* Blue */
        margin-bottom: 40px;
    }

    .info-title {
        font-size: 30px;
        font-weight: bold;
        color: #28a745; /* Green */
        margin-bottom: 10px;
    }

    .names-list {
        list-style-type: none;
        padding: 0;
        margin: 0;
    }

    .names-list li {
        margin-bottom: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-container"> <h1 class="title">Neuroscribe 🧠</h1>''<p class="pitch">Translating Thoughts into Written Words with Robotic Finesse and Vocal Feedback</p>'
'<h2 class="info-title">22AIE214: Introduction to AI Robotics 🤖</h2>''<h2 class="info-title">Faculty Incharge:</h2>'"Dr. Navaneeth Haridasan"'<h2 class="info-title">Team Members:</h2>'"Kathir A" '<br>'"Arivananthan M"'<br>' "Saran Dharshan S.P" '<br>'"Shreyas Sivakumar"'</div>', unsafe_allow_html=True) # Close the main container