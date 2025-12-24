import streamlit as st
from pages.child_profile import ensure_profile_exists
from openai import OpenAI
import base64
import os
from dotenv import load_dotenv
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

# ---------------------------
# OPENAI CLIENT
# ----------------------------
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ----------------------------
# PAGE HEADER
# ----------------------------
st.markdown("<h1 style='text-align:center;'>🧩 Activity Generator for Ausome Kids 🌈♾️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Generate custom activity worksheets for children</p>", unsafe_allow_html=True)

# ----------------------------
# TABS
# ----------------------------
tabs = st.tabs(["🧩 Child Profile", "📝 Generate Worksheet", "ℹ️ About"])

# ----------------------------
# CHILD CONTEXT FUNCTION
# ----------------------------
def build_child_context():
    profile = st.session_state
    return f"""
Child Profile:
- Name: {profile.get('child_name')}
- Age: {profile.get('child_age')}
- Learning Style: {profile.get('learning_style')}
- Academic Level: {profile.get('academic_level')}

Behavioral Information:
- Notes: {profile.get('behavioral_notes')}

Strengths & Interests:
- Strengths: {profile.get('child_strengths')}
- Interests: {profile.get('child_interests')}

Sensory Profile:
- Sensitivity Level: {profile.get('sensory_profile')}
- Triggers: {profile.get('sensory_triggers')}

Communication Profile:
- Level: {profile.get('comm_level')}
- Methods: {profile.get('comm_methods')}
"""

# ----------------------------
# WORKSHEET PROMPT FUNCTION
# ----------------------------
def build_worksheet_prompt(activity_type):
    child_age = st.session_state.get("child_age", "")
    learning_style = st.session_state.get("learning_style", "")
    behavior = st.session_state.get("behavioral_notes", "")
    strengths = st.session_state.get("child_interests", "")
    sensory = st.session_state.get("sensory_profile", "")
    communication = st.session_state.get("comm_level", "")

    base_profile = f"""
You are an AI that generates sensory-friendly worksheets for children with ASD.

Child Profile:
- Age: {child_age}
- Learning Style: {learning_style}
- Behavioral Notes: {behavior}
- Strengths & Interests: {strengths}
- Sensory Sensitivity: {sensory}
- Communication Level: {communication}

Follow ASD-friendly design:
- Black & white only
- Thick outlines, minimal details
- Structured and predictable layout
- Very simple instructions
- Wide spacing
"""
    # Example activity types
    if activity_type == "CVC Blending":
        return base_profile + """Create a black-and-white, sensory-friendly phonics worksheet focused on CVC word blending.
            Include:
            - A clear name header line: “Name: ___________”
            - A short, simple instruction: “Read the sounds. Blend the word.”
            - A table with 4 columns and 3 rows.
            - Each cell should contain:
                • One CVC word (e.g., tap, gap, cap, mop, dog, sun, bed, lip)
                • The word should be in large, clear font.
            - Use only beginner-level CVC words.
            - Avoid pictures unless explicitly requested.
            - Keep layout low-visual-clutter for ASD-friendly processing."""
    if activity_type == "Alphabet Tracing":
        return base_profile + "Generate an alphabet tracing worksheet (uppercase + lowercase) with simple related objects and dotted lines to trace."
    if activity_type == "Line Tracing":
        return base_profile + "Generate a line tracing worksheet with straight, zigzag, curved, and wavy lines."
    if activity_type == "Shape Tracing":
        return base_profile + "Generate a shape tracing worksheet with square, circle, triangle, star, heart, etc., with labels and dashed lines."
    if activity_type == "Writing Practice":
        return base_profile + "Generate a handwriting practice worksheet with large model letters/numbers and multiple rows of dotted traceable characters."

    # Default custom topic
    return base_profile + f"""
Generate a sensory-friendly worksheet based on this topic:
"{activity_type}"

Requirements:
- Black & white only
- Simple illustrations
- Very simple instructions
- Structured layout
- Header: "Name: ________"
"""

# ---------- TAB 1: Child Profile ----------
with tabs[0]:
    st.header("Child Profile")
    ensure_profile_exists()
    st.info("You can update the child profile below. Changes are saved automatically.")

    st.subheader("👤 Personal Information")
    st.text_input("Name", value=st.session_state.get('child_name',''), key='child_name')
    st.number_input("Age", value=st.session_state.get('child_age',5), min_value=1, max_value=18, key='child_age')
    learning_options = ["Visual","Auditory","Kinesthetic","Mixed"]
    st.selectbox("Learning Style", learning_options, index=learning_options.index(st.session_state.get('learning_style','Visual')), key='learning_style')
    academic_options = ["Preschool","Kindergarten","Grade 1","Grade 2","Grade 3+"]
    st.selectbox("Academic Level", academic_options, index=academic_options.index(st.session_state.get('academic_level','Preschool')), key='academic_level')

    st.subheader("📝 Behavioral Information")
    st.text_area("Behavioral Notes", value=st.session_state.get('behavioral_notes',''), height=80, key='behavioral_notes')

    st.subheader("🌟 Strengths & Interests")
    st.text_area("Strengths", value=st.session_state.get('child_strengths',''), height=60, key='child_strengths')
    st.text_area("Interests", value=st.session_state.get('child_interests',''), height=60, key='child_interests')

    st.subheader("🔍 Sensory Profile")
    sensory_options = ["Low","Medium","High"]
    st.selectbox("Sensitivity Level", sensory_options, index=sensory_options.index(st.session_state.get('sensory_profile','Medium')), key='sensory_profile')
    st.text_area("Triggers", value=st.session_state.get('sensory_triggers',''), height=60, key='sensory_triggers')

    st.subheader("💬 Communication Profile")
    comm_options = ["Non-verbal","Basic Words","Full Sentences"]
    st.selectbox("Communication Level", comm_options, index=comm_options.index(st.session_state.get('comm_level','Basic Words')), key='comm_level')
    st.text_area("Communication Methods", value=st.session_state.get('comm_methods',''), height=60, key='comm_methods')

    focus_options = ["Cognitive","Self-Help"]
    current_focus_val = st.session_state.get("child_activity", focus_options[0])
    if isinstance(current_focus_val,list) and current_focus_val:
        current_focus_val = current_focus_val[0]
    st.selectbox("Focus", focus_options, index=focus_options.index(current_focus_val) if current_focus_val in focus_options else 0, key='child_activity')

# ---------- TAB 2: Generate Worksheet ----------
with tabs[1]:
    st.header("Generate Worksheet")

    raw_focus = st.session_state.get("child_activity", None)
    if isinstance(raw_focus, list) and raw_focus:
        focus = raw_focus[0]
    else:
        focus = raw_focus

    if not focus:
        st.warning("⚠️ Please go back to the profile tab and select an activity focus.")
    else:
        st.subheader(f"Focus: {focus} (Age: {st.session_state.get('child_age','N/A')})")
        topic_input_key = f"user_topic_input_{focus}"
        activity_type_for_prompt = None

        # -----------------------------
        #  SELECT ACTIVITY TYPE
        # -----------------------------
        if focus.lower() == "cognitive":
            subtype = st.radio(
                "Choose a Cognitive Activity type:",
                ["Basic Reading (Phonics)", "Shapes (Math)", "Tracing (Writing)", "Other/Custom"],
                key="cog_radio_type"
            )
            subtype_map = {
                "Basic Reading (Phonics)": "CVC Blending",
                "Shapes (Math)": "Shape Tracing",
                "Tracing (Writing)": "Line Tracing"
            }
            if subtype in subtype_map:
                activity_type_for_prompt = subtype_map[subtype]
            elif subtype == "Other/Custom":
                topic = st.text_input("Enter the custom lesson topic:", key=topic_input_key)
                activity_type_for_prompt = topic.strip()

            # For tracing options
            if subtype == "Tracing (Writing)":
                tracing_type = st.radio(
                    "Select Tracing Focus:",
                    ["Line Tracing", "Alphabet Tracing", "Writing Practice"],
                    key="tracing_focus"
                )
                activity_type_for_prompt = tracing_type

        elif focus.lower() == "self-help":
            subtype = st.radio(
                "Choose a Self-Help skill:",
                ["Personal Hygiene", "Daily Routines", "Household Skills", "Other/Custom Skill"],
                key="self_help_radio_type"
            )
            if subtype == "Other/Custom Skill":
                topic = st.text_input("Enter the custom skill topic:", key=topic_input_key)
                activity_type_for_prompt = topic.strip()
            else:
                activity_type_for_prompt = subtype

        if not activity_type_for_prompt:
            st.warning("Please enter a custom topic or select an activity type.")

        # ---------------------------------------------------------
        #   🔵 BUTTON 1 — GENERATE TEXT ACTIVITY (MODEL A)
        # ---------------------------------------------------------
        if st.button("Generate Text Activity"):
            if activity_type_for_prompt.strip():
                with st.spinner("Generating activity text..."):

                    text_prompt = f"""
                    You are an expert SPED teacher.
                    Create an autism-friendly worksheet activity for a child age {st.session_state.get('child_age','N/A')}.
                    Topic: {activity_type_for_prompt}

                    Include:
                    - clear instructions
                    - 3 to 5 items
                    - simple, encouraging tone
                    - very child-friendly language
                    """

                    try:
                        text_response = client.chat.completions.create(
                            model="gpt-4.1-mini",
                            messages=[{"role": "user", "content": text_prompt}]
                        )

                        st.subheader("📘 Generated Activity Instructions")
                        st.write(text_response.choices[0].message.content)

                    except Exception as e:
                        st.error(f"Error generating activity text: {e}")
            else:
                st.warning("Please select or enter an activity topic before generating.")

        # ---------------------------------------------------------
        #   🔵 BUTTON 2 — GENERATE IMAGE WORKSHEET (MODEL B)
        # ---------------------------------------------------------
        if st.button("Generate Activity Image"):
            if activity_type_for_prompt and activity_type_for_prompt.strip():
                with st.spinner("Generating worksheet image..."):
                    full_prompt = build_worksheet_prompt(activity_type_for_prompt)
                    dall_e_prompt = f"Black & white sensory-friendly worksheet for a child with ASD. {full_prompt}"

                    try:
                        image_response = client.images.generate(
                            model="dall-e-3",
                            prompt=dall_e_prompt,
                            size="1024x1024",
                            quality="standard",
                            n=1,
                            response_format="b64_json"
                        )
                        image_data = base64.b64decode(image_response.data[0].b64_json)

                        col1, col2 = st.columns(2)
                        with col1:
                            st.image(
                                image_data,
                                caption=f"Generated: {activity_type_for_prompt}",
                                use_container_width=True
                            )
                        with col2:
                            st.download_button(
                                label="📥 Download Image",
                                data=image_data,
                                file_name=f"{activity_type_for_prompt.replace(' ','_')}.png",
                                mime="image/png"
                            )
                    except Exception as e:
                        st.error(f"Error during image generation: {e}")
            else:
                st.warning("Please specify an activity topic before generating.")

        # ---------------------------------------------------------
        # BACK BUTTON
        # ---------------------------------------------------------
        if st.button("⬅️ Back to Home", key="back_to_home_btn"):
            st.switch_page("ausome_main")

# ---------- TAB 3: About ----------
with tabs[2]:
    st.header("About AI Ausome Assistant")
    st.info("""
    This app allows teachers and parents to generate **customized worksheets** for children with ASD.
    
    Features:
    - Cognitive, Language, and Self-Help worksheets
    - AI-generated images for worksheets
    - Downloadable PNG worksheets
    - Child-friendly pastel design
    
    2025 Uplift Project Presentation
    """)
