# pages/home.py
import streamlit as st
from pages.child_profile import child_profile
from utils.background import apply_background

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="AI Ausome Assistant",
    page_icon="💙",
    layout="wide"
)

# ----------------------------
# APPLY BACKGROUND CSS
# ----------------------------
apply_background()

# ----------------------------
# PAGE HEADER
# ----------------------------
st.title("🎨 AI Ausome Assistant")
st.markdown("Welcome! Please enter child information to continue.")

# ----------------------------
# CHILD PROFILE FORM
# ----------------------------
child_profile(show_title=False)

# ----------------------------
# SELECT ACTIVITY FOCUS
# ----------------------------
selected_focus = st.radio(
    "Choose focus area:",
    ["Cognitive", "Self-Help"],
    index=0 if st.session_state.get("child_activity") is None else
          (0 if st.session_state["child_activity"] == "Cognitive" else 1)
)

# Save the selection to session_state
st.session_state["child_activity"] = selected_focus

# ----------------------------
# GENERATE ACTIVITY BUTTON
# ----------------------------
if st.button("Generate Activity"):
    st.switch_page("pages/ausome_chatbot.py")  # match the filename exactly

