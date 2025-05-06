import streamlit as st
import base64

def show_home_screen(): 

    # Create two columns
    col1, col2 = st.columns([2, 5])  

    with col1:
        st.image("FPU_images/FPU logo.webp", width=150) 

    with col2:
        st.title("SUNNY THE SUNBIRD AI")
        st.write("Learn about Fresno Pacific University!")

    # Define image path
    logo_path = "FPU_images/sunbirds.png"
    logo_path1 = "FPU_images/FPU.png"
    logo_path2 = "FPU_images/FresnoPacific.png"

    # Encode image to base64
    with open(logo_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode()
    with open(logo_path1, "rb") as img_file:
        b64_string1 = base64.b64encode(img_file.read()).decode()
    with open(logo_path2, "rb") as img_file:
        b64_string2 = base64.b64encode(img_file.read()).decode()

    # URLs
    link_url = "https://www.fpusunbirds.com"
    link_url2 = "https://www.fresno.edu/admission"
    link_url3 = "https://www.fresno.edu/undergraduate/programs"

    # Embed in HTML
    st.markdown(
    f"""
    
    <style>
    html, body, .stApp {{
        background-color: #2a5873 !important;
        margin: 0 !important;
        padding: 0 !important;
        overflow-x: hidden;
        base="dark"
        primaryColor="#2a5873"
        backgroundColor="#2a5873"
    }}
    header, footer {{
        background-color: #2a5873 !important;
    }}
    .row {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        gap: 10px;
    }}
    .clickable-box1, .clickable-box2, .clickable-box3 {{
        background-color: #aebbc2;
        padding: 20px;
        border-radius: 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        box-shadow: 0 4px 8px #000000;
        text-align: center;
        width: 250px;
        text-decoration: none;
    }}
    .clickable-box1 img, .clickable-box2 img, .clickable-box3 img {{
        height: 100px;
        margin-bottom: 15px;
        border-radius: 8px;
    }}
    .clickable-box1 p, .clickable-box2 p, .clickable-box3 p {{
        font-size: 18px;
        font-weight: bold;
        color: #000000;
        margin: 0.5px 0;
    }}
    .clickable-circle {{
        width: 150px;
        height: 150px;
        border-radius: 50%;
        background-color: #d67a45;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        font-size: 16px;
        font-weight: bold;
        color: #000;
        cursor: pointer;
        circle-shadow: 0 4px 8px #000000;
        padding: 20px;
        text-decoration: none;
        transition: transform 0.2s ease;
    }}
    .clickable-circle:hover {{
        transform: scale(1.05);
    }}
    .clickable-circle p {{
        font-size: 15px;
        font-weight: bold;
        color: #000000;
        margin: 0.5px 0;
    }}
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 200px;
        pointer-events: none;
        background: linear-gradient(to bottom, #2a5873, rgba(42, 88, 115, 0));
        z-index: 1000;
    }}
    </style>

    <!-- Row 1 -->
    <div class="row">
        <a href="{link_url}" class="clickable-box1" target="_blank">
            <img src="data:image/png;base64,{b64_string}" alt="Sunbirds Logo">
            <p>FPU ATHLETICS</p>
            <p>Website Here!</p>
        </a>
        <a class="clickable-circle" onclick="window.open('{link_url2}', '_blank')">
        <div>
            <p>Charlottes</p>
            <p>Opening</p>
            <p>Hours</p>
        </div>
        </a>
    </div>

    <!-- Row 2 -->
    <div class="row">
        <a class="clickable-circle" onclick="window.open('{link_url2}', '_blank')">
        <div>
            <p>Hiebert Library</p>
            <p>Opening</p>
            <p>Hours</p>
        </div>
        </a>
        <a href="{link_url2}" class="clickable-box2" target="_blank">
            <img src="data:image/png;base64,{b64_string1}" alt="Sunbirds Logo">
            <p>APPLY HERE!</p>
        </a>
    </div>

    <!-- Row 3 -->
    <div class="row">
        <a href="{link_url3}" class="clickable-box3" target="_blank">
            <img src="data:image/png;base64,{b64_string2}" alt="Sunbirds Logo">
            <p>Check out our</p>
            <p>Undergraduate</p>
            <p>Programs!</p>
        </a>
        <a class="clickable-circle" onclick="window.open('{link_url2}', '_blank')">
        <div>
            <p>Main Campus</p>
            <p>Map</p>
        </div>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
