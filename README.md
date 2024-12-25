# NeuroScribe
Translating Thoughts into Written Words with Robotic Finesse and Vocal Feedback

This project presents the development of a handwriting assistance system designed for individuals with limited motor function, leveraging Brain-Computer Interface (BCI) technology, advanced machine learning algorithms, and Internet of Things (IoT) devices. The system utilizes the OpenBCI Ultracortex Mark IV EEG headset to capture brain signals corresponding to the user's intent to write specific letters. Signal preprocessing involves bandpass filtering to confine signals within the 0-60 Hz range, followed by Variational Mode Decomposition (VMD) to decompose signals, reduce noise, and eliminate irrelevant frequencies.

The preprocessed EEG data are fed into a deep learning model trained to classify EEG patterns associated with individual letters. An IoT-enabled device with a Wi-Fi module facilitates real-time control of a CNC plotter, which physically reproduces the user's intended letter. Additionally, an integrated voice speaker provides immediate auditory feedback by announcing the predicted letter, enhancing user interaction and control.

This project advances assistive technologies by introducing a practical and intuitive BCI-controlled robotic handwriting system. Future enhancements may include adaptive learning algorithms for improved prediction accuracy, personalized calibration for tailored performance, and exploration of alternative input modalities to extend the system's applicability beyond handwriting. Further improvements, such as sophisticated pattern recognition algorithms and dynamic time warping for signal alignment, are also proposed to enhance the system's accuracy, speed, efficiency and user-friendliness.


## FLOW CHART
![Work Flow](https://github.com/user-attachments/assets/14804a49-4fb9-4a75-b373-08e8467633c7)


## EEG Streamlit Application

We’ve introduced a **Streamlit-based EEG application** to make the NeuroScribe system more interactive and accessible.
This app simplifies interaction with the model, offering user-friendly interface for EEG data visualization, preprocessing, and classification of alphabets.

### Demo 

Watch the demo of the EEG Streamlit app here:
[EEG App Demo](https://www.dropbox.com/scl/fi/imfs9211l7yj7fph7riaf/Appdemo.mp4?rlkey=ctvnrjt7e55r0x5s5fgukr50i&st=lm0ukn5o&dl=0)

### Steps to Run the App Locally
```bash
  git clone https://github.com/SaranDharshanSP/NeuroScribe.git
  cd NeuroScribe
  cd AlphabetClassification
  pip install streamlit
  pip install numpy
  pip install pandas
  pip install scikit-learn
  pip install matplotlib
  streamlit run app.py
