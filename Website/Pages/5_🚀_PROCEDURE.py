import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 48px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .subtitle {
        text-align: center;
        font-size: 24px;
        margin-bottom: 40px;
    }
    .section-header {
        font-size: 32px;
        font-weight: bold;
        margin-top: 40px;
        margin-bottom: 20px;
        color: #007bff;  /* Blue for headers */
    }
    .description {
        font-size: 18px;
        line-height: 1.5;
        margin-bottom: 20px;
    }
    .image-container {
        display: flex;
        justify-content: center;
        margin-bottom: 40px;
    }
    .image {
        max-width: 80%;
    }
    .component-list {
        list-style-type: disc;
        margin-left: 40px;
    }
    .code {
        background-color: #f0f0f0;
        padding: 10px;
        margin-bottom: 20px;
        border-radius: 5px;
        font-family: monospace;
    }
    .procedure-step {
        margin-bottom: 20px;
    }
    .step-title {
        font-weight: bold;
        margin-bottom: 10px;
        color: #343a40; /* Dark gray for step titles */
    }
    .step-description {
        margin-left: 20px;
    }
    .gcode {
        background-color: #f8f9fa; /* Light gray for G-code */
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 5px;
        font-family: monospace;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-header">
        Procedure 🛠️
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="description">
        This section outlines the step-by-step process followed to build and operate the Neuroscribe plotter.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="procedure-step">
        <div class="step-title">
            1. Hardware Setup 🔌
        </div>
        <div class="step-description">
            <ul>
                <li>All the parts for the CNC plotter were readily available in our lab.</li>
                <li>We assembled these parts to construct the plotter.</li>
                <li>The plotter was built based on the schematic circuit diagram.</li>
                <li>Finally, a 12V DC supply was provided to the motors through the drivers.</li>
                <li>Our hardware setup was complete. 🎉</li>
            </ul>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="procedure-step">
        <div class="step-title">
            2. Software setup 💻
        </div>
        <div class="step-description">
            <ul>
                <li>open ugs </li>
                <li>open a gcode file</li>
                <li>enter the gcode for drawing the desired alphabet</li>
                <li>click the play button and the ugs software will do the gcode conversion and send it to the Arduino which then signals the stepper motor to move</li>
                <li>Gcode setup:</li>
                <li>Through numerous trials and understanding the workspace dimensions of the plotter, G-code was created for the desired alphabets "A" and "B".</li>
                <li>G-code for "A":</li>
                <div class="gcode">
                    G91 X15 F100<br>
                    G91 Y-15<br>
                    G91 Y4<br>
                    G91 X-6 Y6
                </div>
                <li>G-code for "B": </li>
                <div class="gcode">
                    G91 X10    Y10   F100<br>
                    G91 X10    Y-10<br>
                    G91 X-5    Y-5<br>
                    G91 X-10  Y10<br>
                    G91 X10    Y-10<br>
                    G91 X-5    Y-5<br>
                    G91 X-10  Y10
                </div>
            </ul>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="procedure-step">
        <div class="step-title">
            3. Final Output 🖼️
        </div>
        <div class="step-description">
            <ul>
                <li>The final output we obtained matched our intended goal.</li>
                <li>We successfully created the G-code for the letters "A" and "B".</li>
                <li>The plotter successfully drew these letters. ✍️</li>
                <li>Hence, the objective of the 2D CNC plotter was fulfilled. 🥳</li>
            </ul>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)