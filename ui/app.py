import streamlit as st
import requests
from datetime import datetime
import time

# Page Config
st.set_page_config(page_title="💡 AI Tech Support Agent", page_icon="💡", layout="wide")

# Custom CSS: Dark neon theme + animations
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@500;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
        background-color: #0F3D3D;
        color: #E0F2F1;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    h1 {
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(90deg, #38BDF8, #22D3EE, #0EA5E9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: move 4s linear infinite;
    }

    @keyframes move {
        0% {background-position: 0%;}
        100% {background-position: 200%;}
    }

    .stTextInput > div > div > input {
        border: 2px solid #38BDF8;
        border-radius: 0.5rem;
        padding: 0.8rem;
        background-color: #FFFFFF;
        color: #111827;
    }

    .stButton > button {
        background-color: #0EA5E9;
        color: #0F172A;
        border-radius: 0.5rem;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
        margin-top: 1rem;
        box-shadow: 0 0 12px #38BDF8;
    }

    .stButton > button:hover {
        background-color: #38BDF8;
        color: #000;
    }

    .stTextArea > div > textarea {
        border: 2px solid #38BDF8;
        border-radius: 0.5rem;
        background-color: #F1F5F9;
        color: #0F172A;
        font-size: 1.05rem;
        padding: 0.75rem;
    }

    .neon-bar {
        height: 3px;
        background: linear-gradient(90deg, #0EA5E9, #22D3EE, #38BDF8);
        border-radius: 3px;
        margin: 20px 0;
        animation: move 3s linear infinite;
    }

    .footer {
        font-size: 0.85rem;
        color: #94A3B8;
        text-align: center;
        margin-top: 3rem;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Sidebar: Agent Profile
with st.sidebar:
    st.image("suport ai assis.jpg", width=300)
    st.title("🤖 TechSupport Agent")
    st.caption("Built by Abel")
    st.markdown("---")
    st.write("**🕰️ Current Time:**")
    st.write(datetime.now().strftime("%A %d %B, %I:%M %p"))
    st.markdown("---")
    st.write("**Chat History**")
    if "history" not in st.session_state:
        st.session_state.history = []
    for idx, (q, a) in enumerate(reversed(st.session_state.history[-5:])):
        st.markdown(f"**Q:** {q}\n\n**A:** {a[:40]}...")

# App Title
st.title("💡 AI Technical Support Assistant")

# Neon separator bar
st.markdown('<div class="neon-bar"></div>', unsafe_allow_html=True)

# Query input
query = st.text_input("📥 Describe your issue:", placeholder="e.g., Why is my laptop overheating?")

# Submit Button
if st.button("Get Help", key="support_button"):
    if query.strip():
        with st.spinner("📝 Typing response..."):
            try:
                response = requests.post("http://localhost:8000/support", json={"query": query})

                if response.status_code == 200:
                    result = response.json()
                    ai_response = result['response']

                    # Animated typing effect
                    display_text = ""
                    response_placeholder = st.empty()
                    for char in ai_response:
                        display_text += char
                        response_placeholder.text(display_text)
                        time.sleep(0.015)

                    st.session_state.history.append((query, ai_response))

                else:
                    st.error(f"❌ Backend error ({response.status_code}): {response.text}")

            except requests.exceptions.RequestException as e:
                st.error(f"⚠️ Connection error: {e}")
    else:
        st.warning("⚠️ Please type your issue first!")

# Neon separator bar
st.markdown('<div class="neon-bar"></div>', unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>© 2025 Technical Support AI — Custom UI by Abel ⚡</div>", unsafe_allow_html=True)
