import streamlit as st
from ChatHelpers import init_chat_session, handle_user_input, display_chat_messages

def show_chat_screen():
    # Back button at the top right
    top_col1, top_col2 = st.columns([8, 3])  # Wide left, narrow right

    with top_col2:
        st.markdown("<div style='text-align: right;'>", unsafe_allow_html=True)
        if st.button("← Back to Home"):
            st.session_state['screen'] = 'home'
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # Now the logo and title below
    col1, col2 = st.columns([2, 5])  

    with col1:
        st.image("FPU_images/FPU logo.webp", width=150) 

    with col2:
        st.title("SUNNY THE SUNBIRD AI")
        st.write("Learn about Fresno Pacific University!")

    with st.container():
        st.markdown('<div class="chat-screen">', unsafe_allow_html=True)

        init_chat_session()

        # Display chat messages after handling input
        display_chat_messages()

        st.markdown('</div>', unsafe_allow_html=True)
