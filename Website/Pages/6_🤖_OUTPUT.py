import streamlit as st
from streamlit.components.v1 import html
import time

st.title("OUTPUT")

# Set custom CSS for styling
st.markdown(
    """
    <style>
        .video-container {
            display: flex;
            justify-content: space-around;
            align-items: center;
            padding: 20px;
        }

        .video-card {
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            width: 45%;
            text-align: center;
        }

        .video-card h2 {
            color: #333;
            margin-bottom: 10px;
        }

        .video-card p {
            font-size: 14px;
            color: #555;
            margin-bottom: 20px;
        }

        .stVideo {
            width: 100%; /* Make video fill the container width */
            height: auto; /* Maintain aspect ratio */
        }

        .video-container {
            display: flex;
            justify-content: center;
            margin-bottom: 40px;
        }
        .video-player {
            width: 80%;
            height: auto;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Video 1
with st.container():
    st.markdown(
        "<h1 style='text-align:center; color: #333; font-size: 3em; margin-bottom: 20px;'>Video 1</h1>",
        unsafe_allow_html=True,
    )

    col1, col2, COL3 = st.columns(3)
    with col2:
        video_file1 = r'https://github.com/SaranDharshanSP/NueroScribe/assets/126688534/936cd7e1-e431-4982-aea2-8ef8d9bc9271'  # Replace with your video file path
        st.video(video_file1, format="video/mp4", start_time=0)

# Video 2
with st.container():
    st.markdown(
        "<h1 style='text-align:center; color: #333; font-size: 3em; margin-bottom: 20px;'>Video 2</h1>",
        unsafe_allow_html=True,
    )

    col1, col2,col3 = st.columns(3)
    with col2:
        video_file2 = r'https://github.com/SaranDharshanSP/NueroScribe/assets/126688534/94e680ed-fdaf-42f7-b8e6-33c5c94f5b79'  # Replace with your video file path
        st.video(video_file2, format="video/mp4", start_time=0)


# Add some visual elements for a more polished look
st.markdown("---")

#  Video in the desired layout
st.markdown(
    """
    <div class="video-container">
        <video class="video-player" controls autoplay>
            <source src="https://github.com/SaranDharshanSP/Leetcode-Solution-Python/assets/126688534/c7efbef4-d810-4d16-a862-41174977d8dd" type="video/mp4">
        </video>
    </div>
    """,
    unsafe_allow_html=True,
)