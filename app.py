import streamlit as st

# Page Configuration
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱", layout="centered")

# Styling
st.markdown(
    """
    <style>
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #4CAF50;
        }
        .quote {
            font-size: 20px;
            font-style: italic;
            color: #555;
            text-align: center;
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title & Header
st.markdown("<div class='title'>🌱 Growth Mindset Challenge 🌱</div>", unsafe_allow_html=True)
st.subheader("Welcome to Your Growth Mindset Journey!")

# Quote Section
st.markdown("<div class='quote'>\"Every challenge is an opportunity to grow. Embrace the process, learn from failures, and keep moving forward!\" 🚀</div>", unsafe_allow_html=True)

# User Input for Challenges
st.header("💡 Share Your Challenge")
user_input = st.text_input("What challenge are you facing today?", placeholder="Write your challenges here...")

if user_input:
    st.success(f"You're facing: **{user_input}**. Keep pushing forward! 💪")
else:
    st.warning("Please share your challenge to continue.")

# Reflection Section
st.header("📝 Reflect on Your Learning")
reflection = st.text_area("Write your reflection here:", placeholder="How are you growing from this experience?")

if reflection:
    st.success("Great! Reflection helps you grow. 🌱")
else:
    st.info("Take a moment to reflect and write down your thoughts.")

# Achievements Section
st.header("🎉 Celebrate Your Wins")
achievement = st.text_input("Share something you've achieved recently:", placeholder="Big or small, every achievement matters!")

if achievement:
    st.success(f"You're achieving: **{achievement}**. Keep going! 🚀")
else:
    st.info("Recognizing achievements helps you stay motivated!")

# Footer
st.divider()
st.write("✨ Thank you for your participation! Keep growing and learning! ✨")
st.write("👤 **Created by:** Muhammad Shaheryar")
