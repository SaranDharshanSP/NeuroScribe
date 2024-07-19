import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Neuroscribe: Aim",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 48px;
        font-weight: bold;
        margin-bottom: 20px;
        color: #343a40; /* Dark Gray */
    }

    .abstract {
        font-size: 18px;
        line-height: 1.6;
        text-align: justify;
        margin-bottom: 40px;
        color: #212529; /* Dark Gray */
    }

    .section-header {
        font-size: 32px;
        font-weight: bold;
        margin-top: 40px;
        margin-bottom: 20px;
        color: #007bff; /* Blue */ 
    }

    .image-container {
        display: flex;
        justify-content: center;
        margin-bottom: 40px;
    }

    .image {
        max-width: 80%;
        box-shadow: 5px 5px 10px #888888; /* Light Gray Shadow */
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="title">Neuroscribe: Aim 🧠</div>', unsafe_allow_html=True)

st.markdown('<div class="section-header">Abstract</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="abstract">
    This project presents the development of a handwriting assistance system designed for individuals with limited motor function, 
    leveraging Brain-Computer Interface (BCI) technology, advanced machine learning algorithms, and Internet of Things (IoT) devices. 
    The system utilizes the OpenBCI Ultracortex Mark IV EEG headset to capture brain signals corresponding to the user's intent to 
    write specific letters. Signal preprocessing involves bandpass filtering to confine signals within the 0-60 Hz range, followed by 
    Variational Mode Decomposition (VMD) to decompose signals, reduce noise, and eliminate irrelevant frequencies. <br><br>The preprocessed EEG data are fed into a deep learning model trained to classify EEG patterns associated with individual letters. 
    An IoT-enabled device with a Wi-Fi module facilitates real-time control of a CNC plotter, which physically reproduces the user's 
    intended letter. Additionally, an integrated voice speaker provides immediate auditory feedback by announcing the predicted letter, 
    enhancing user interaction and control. <br><br>This project advances assistive technologies by introducing a practical and intuitive BCI-controlled robotic handwriting system. 
    Future enhancements may include adaptive learning algorithms for improved prediction accuracy, personalized calibration for tailored 
    performance, and exploration of alternative input modalities to extend the system's applicability beyond handwriting. Further 
    improvements, such as sophisticated pattern recognition algorithms and dynamic time warping for signal alignment, are also proposed 
    to enhance the system's accuracy, speed, and user-friendliness.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="image-container">
        <img src="https://github.com/SaranDharshanSP/Leetcode-Solution-Python/assets/126688534/a3b5db85-000c-4d6a-80a5-105b009cb688" alt="Workflow of NeuroScribe" class="image">
    </div>
    """,
    unsafe_allow_html=True,
)


