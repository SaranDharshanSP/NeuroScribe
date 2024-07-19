import streamlit as st
from PIL import Image
import streamlit.components.v1 as components


st.set_page_config(layout="wide")

st.title("Neuroscribe: CNC Plotter")



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
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-header">
        Mechanism ⚙️
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="description">
        The plotter machine is assembled based on a serial mechanism where the two stepper motors are mounted on the main chassis, connected to a single continuous belt. 
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="video-container">
        <video width="800" controls autoplay>
            <source src="https://github.com/SaranDharshanSP/Leetcode-Solution-Python/assets/126688534/c7efbef4-d810-4d16-a862-41174977d8dd" type="video/mp4">
        </video>
    </div>
    """,
    unsafe_allow_html=True,
)



st.markdown(
    """
    <div class="section-header">
        Components 🧰
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="description">
        Here are the key components used in the Neuroscribe plotter:
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <ul class="component-list">
        <li>Arduino UNO 💻</li>
        <li>CNC Shield V3 🛡️</li>
        <li>A4988 Stepper Motor Driver 🏎️</li>
        <li>Stepper Motor (Nema 17) ⚙️</li>
        <li>Power Supply (12V)</li>
        <li>Timer Pulley and Idler Pulley 🔄</li>
        <li>Timing Belt 🧵</li>
    </ul>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-header">
        Detailed Component Descriptions 🔍
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="description">
        Let's take a closer look at some of the key components:
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-header">
        Arduino UNO 💻
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="description">
        The Arduino UNO is a microcontroller board based on the ATmega328P. It serves as the brain of the plotter, receiving commands from your computer and controlling the stepper motors to move the pen.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="description">
        It has 14 digital input/output pins (of which 6 can be used as PWM outputs), 6 analog inputs, a 16 MHz ceramic resonator, a USB connection, a power jack, an ICSP header and a reset button. 
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-header">
        CNC Shield V3 🛡️
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="description">
        The CNC Shield is a specialized board that extends the capabilities of the Arduino UNO to control CNC machines. In the Neuroscribe plotter, it acts as an intermediary, connecting the Arduino to the stepper motor drivers and other components.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="description">
        It's compatible with various stepper motor drivers, including the A4988.  It provides a convenient interface for connecting stepper motors, limit switches, and other components to the Arduino board.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-header">
        A4988 Stepper Motor Driver 🏎️
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="description">
        The A4988 is a microstepping driver that translates the signals from the CNC shield into precise commands for the stepper motors. This allows for smooth and controlled movements of the pen, ensuring accurate drawing.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="description">
        It provides different step resolutions, allowing you to fine-tune the motor's movement for optimal drawing quality. 
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-header">
        Stepper Motor (Nema 17) ⚙️
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="description">
        Stepper motors are essential for the movement of the pen.  They are brushless DC motors that rotate in precise steps, making them perfect for precise positioning in drawing applications. 
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="description">
        They are known for their high torque and speed, making them capable of handling the weight of the pen and moving it smoothly across the drawing surface.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-header">
        Timer Pulley and Idler Pulley 🔄
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="description">
        Timing pulleys are specialized pulleys with teeth or pockets that engage with the timing belt, ensuring that the belt does not slip. They are crucial for maintaining the precise movement of the pen arm.  The idler pulley provides tension to the timing belt, keeping it taut and ensuring smooth operation.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-header">
        Timing Belt 🧵
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="description">
        The timing belt connects the stepper motors to the pen arm, transmitting motion from the motors to the pen. It's a non-slipping belt that ensures smooth and consistent movement of the pen arm, vital for accurate drawing.
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div class="section-header">
        Software 💻
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="description">
        Here are the software components used in the Neuroscribe plotter:
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-header">
        Grbl 🧰
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="description">
        Grbl is a free and open-source firmware that runs on the Arduino UNO and controls the movement of the stepper motors. It's responsible for interpreting G-code commands sent from your computer and translating them into precise movements of the pen.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-header">
        Universal G-code Sender (UGS) 📡
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="description">
        Universal G-code Sender (UGS) is a software tool commonly used for controlling 2D plotters. 
        It allows users to connect to their plotter, load G-code files, and send instructions for precise 
        movements and operations. UGS provides essential features like connection management, real-time 
        monitoring, job scheduling, error handling, and recovery options. With its user-friendly interface, 
        UGS simplifies the process of controlling a 2D plotter and ensures accurate results. <br><br>By combining UGS with GRBL firmware, the following benefits can be realized: <br>
        - Compatibility: GRBL firmware is well-suited for 2D plotters and provides seamless compatibility with UGS. 
          This allows users to leverage the advanced features of GRBL, such as acceleration, motion planning, and homing, for precise and efficient plotting. <br>
        - Real-time Feedback: GRBL communicates with UGS to provide real-time feedback on the plotter's status, position, and progress. 
          This enables users to monitor the plotting process closely and make any necessary adjustments or interventions as needed. 
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-header">
        G-code ✍️
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="description">
        G-code is a programming language that's used to control CNC machines, including our plotter. 
        It's a series of commands that tell the plotter where to move the pen, how fast to move, and 
        what path to follow. <br><br>G-Code Generation: Once the design is created, it needs to be converted into machine-readable 
        instructions called G-code. G-code is a programming language that specifies the movements, speeds, 
        and other parameters for the plotter. This step involves software tools or plugins that generate 
        G-code based on the design.
    </div>
    """,
    unsafe_allow_html=True,
)