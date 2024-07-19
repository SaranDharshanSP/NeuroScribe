import streamlit as st

st.set_page_config(
    page_title="Neuroscribe: Contributors",
    page_icon="👥",
    layout="wide",
)

st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 48px;
        font-weight: bold;
        margin-bottom: 40px;
        color: #343a40; /* Dark Gray */
    }

    .contributor-container {
        display: flex;
        flex-direction: column; 
        align-items: center;
        text-align: center; 
        padding: 20px;
        margin-bottom: 20px;
        border: 1px solid #ddd; 
        border-radius: 5px;
        box-shadow: 2px 2px 5px #888888; 
    }

    .contributor-image {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        margin-bottom: 10px;
        object-fit: cover; 
    }

    .contributor-name {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

contributors = [
    {"name": "Kathir A", "reg_no": "CB.EN.U4AIE22001", "photo": "https://github.com/SaranDharshanSP/Leetcode-Solution-Python/assets/126688534/8723a911-441e-43c6-8997-41bc559a344d"},
    {"name": "Arivananthan M", "reg_no": "CB.EN.U4AIE22007", "photo": "https://github.com/SaranDharshanSP/Leetcode-Solution-Python/assets/126688534/79dff7fa-6013-401b-93ae-34cf4bea62e0"},
    {"name": "Saran Dharshan S.P", "reg_no": "CB.EN.U4AIE22045", "photo": "https://github.com/SaranDharshanSP/Leetcode-Solution-Python/assets/126688534/406281b4-0cb6-42dc-858b-6e66df7791ef"},
    {"name": "Shreyas Sivakumar", "reg_no": "CB.EN.U4AIE22050", "photo": "https://github.com/SaranDharshanSP/NueroScribe/assets/126688534/391a4ebc-95d2-40ce-87e7-b1d84b706459"},
]

mentor_name = "Dr. Navaneeth Haridasan"
mentor_photo = "https://github.com/SaranDharshanSP/Leetcode-Solution-Python/assets/126688534/7e14f007-75f7-4d81-8ba4-4e5e8905c4b1"

st.markdown('<div class="title">Contributors 👥</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,1,1]) 

with col2:
    st.markdown(
        f"""
        <div class="contributor-container">
            <img src="{mentor_photo}" width="150" style="border-radius:50%;"/>
            <div class="contributor-info">
                <div class="contributor-name" style="font-size:20px; font-weight:bold; margin-top:10px;">{mentor_name}</div>
                <div>Assistant Professor at School of AI, <br>Amrita Vishwa Vidyapeetham.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
col1, col2, col3, col4 = st.columns(4)

for i, contributor in enumerate(contributors):
    with eval(f"col{i+1}"): 
        st.markdown(
            f"""
            <div class="contributor-container">
                <img src="{contributor['photo']}" alt="Profile Picture" class="contributor-image">
                <div class="contributor-info">
                    <div class="contributor-name">{contributor['name']}</div>
                    <div>{contributor['reg_no']}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )