# child_profile.py
import streamlit as st
from datetime import date

def ensure_session_state():
    """Ensure all keys exist in session_state to avoid KeyErrors."""
    defaults = {
        # Basic Info
        "child_name": "",
        "child_age": "",
        "child_birthday": "",
        "child_gender": "",
        "parent_name": "",
        "parent_contact": "",

        # Diagnosis
        "diagnosis": "",
        "diagnosis_date": "",
        "diagnosed_by": "",
        "current_therapies": [],

        # Communication
        "communication_method": "",
        "expressive_level": "",
        "receptive_level": "",
        "communication_challenges": [],

        # Sensory
        "sensory_sensitivities": [],
        "sensory_needs": [],
        "calming_strategies": [],

        # Strengths & Interests
        "child_strengths": "",
        "child_interests": "",

        # Behavior
        "behavior_triggers": "",
        "behavior_management": "",

        # Learning
        "learning_style": "",
        "academic_focus": "",

        # Routines
        "routine_morning": "",
        "routine_school": "",
        "routine_bedtime": "",
        "eating_notes": "",

        # Safety
        "allergies": "",
        "emergency_contact": "",
        "safety_concerns": "",
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def child_profile(show_title=True):
    ensure_session_state()

    if show_title:
        st.title("🧩 Child Profile")
        st.markdown("Please provide or update the child's information below.")

    with st.form("child_profile_form"):
        st.subheader("👶 Basic Information")
        st.session_state.child_name = st.text_input(
            "Child Name", st.session_state.child_name
        )
        st.session_state.child_age = st.number_input(
            "Age", min_value=1, max_value=18, value=int(st.session_state.child_age) if st.session_state.child_age else 7
        )
        st.session_state.child_birthday = st.date_input(
            "Birthday",
            value=(
                st.session_state.child_birthday
                if isinstance(st.session_state.child_birthday, date)
                else date(2017, 1, 1)
            )
        )
        st.session_state.child_gender = st.selectbox(
            "Gender", ["Male", "Female", "Prefer not to say"], index=0
        )
        st.session_state.parent_name = st.text_input(
            "Parent/Guardian Name", st.session_state.parent_name
        )
        st.session_state.parent_contact = st.text_input(
            "Contact Information", st.session_state.parent_contact
        )

        st.markdown("---")
        st.subheader("🩺 Developmental & Diagnostic Information")
        st.session_state.diagnosis = st.text_input(
            "Diagnosis (e.g., ASD Level 1, ADHD)", st.session_state.diagnosis
        )
        st.session_state.diagnosis_date = st.date_input(
            "Diagnosis Date",
            value=(
                st.session_state.diagnosis_date
                if isinstance(st.session_state.diagnosis_date, date)
                else date(2020, 1, 1)
            )
        )
        st.session_state.diagnosed_by = st.text_input(
            "Diagnosed By / Clinic", st.session_state.diagnosed_by
        )
        st.session_state.current_therapies = st.multiselect(
            "Current Therapies",
            ["Occupational Therapy", "Speech Therapy", "ABA", "SPED", "Shadow Teacher", "Others"],
            default=st.session_state.current_therapies,
        )

        st.markdown("---")
        st.subheader("🗣 Communication Profile")
        st.session_state.communication_method = st.selectbox(
            "Primary Communication Method",
            ["Verbal", "Gestures", "AAC Device", "PECS", "Mixed"],
            index=0
        )
        st.session_state.expressive_level = st.text_input(
            "Expressive Language Level", st.session_state.expressive_level
        )
        st.session_state.receptive_level = st.text_input(
            "Receptive Language Level", st.session_state.receptive_level
        )
        st.session_state.communication_challenges = st.multiselect(
            "Communication Challenges",
            ["Echolalia", "Delayed response time", "Difficulty initiating conversation"],
            default=st.session_state.communication_challenges,
        )

        st.markdown("---")
        st.subheader("🎧 Sensory Profile")
        st.session_state.sensory_sensitivities = st.multiselect(
            "Sensory Sensitivities",
            ["Sound", "Light", "Touch", "Movement", "Crowds/Visual clutter"],
            default=st.session_state.sensory_sensitivities,
        )
        st.session_state.sensory_needs = st.multiselect(
            "Sensory Needs/Tools",
            ["Weighted items", "Movement breaks", "Chewelry", "Noise-cancelling headphones"],
            default=st.session_state.sensory_needs,
        )
        st.session_state.calming_strategies = st.multiselect(
            "Calming Strategies",
            ["Deep pressure", "Fidget toys", "Visual timer", "Soft music"],
            default=st.session_state.calming_strategies,
        )

        st.markdown("---")
        st.subheader("💡 Strengths & Interests")
        st.session_state.child_strengths = st.text_area(
            "Child's Strengths", st.session_state.child_strengths
        )
        st.session_state.child_interests = st.text_area(
            "Special Interests", st.session_state.child_interests
        )

        st.markdown("---")
        st.subheader("⚠️ Behavioral Information")
        st.session_state.behavior_triggers = st.text_area(
            "Common Triggers", st.session_state.behavior_triggers
        )
        st.session_state.behavior_management = st.text_area(
            "Effective Management Strategies", st.session_state.behavior_management
        )

        st.markdown("---")
        st.subheader("📘 Learning Profile")
        st.session_state.learning_style = st.selectbox(
            "Preferred Learning Style", ["Visual", "Auditory", "Kinesthetic", "Multi-sensory"]
        )
        st.session_state.academic_focus = st.text_area(
            "Academic Focus / Areas Needing Support", st.session_state.academic_focus
        )

        st.markdown("---")
        st.subheader("🕒 Routines")
        st.session_state.routine_morning = st.text_area(
            "Morning Routine Notes", st.session_state.routine_morning
        )
        st.session_state.routine_school = st.text_area(
            "School Routine Notes", st.session_state.routine_school
        )
        st.session_state.routine_bedtime = st.text_area(
            "Bedtime Routine Notes", st.session_state.routine_bedtime
        )
        st.session_state.eating_notes = st.text_area(
            "Eating Patterns / Notes", st.session_state.eating_notes
        )

        st.markdown("---")
        st.subheader("🛟 Safety & Health")
        st.session_state.allergies = st.text_area(
            "Allergies", st.session_state.allergies
        )
        st.session_state.emergency_contact = st.text_input(
            "Emergency Contact", st.session_state.emergency_contact
        )
        st.session_state.safety_concerns = st.text_area(
            "Safety Concerns (e.g., wandering)", st.session_state.safety_concerns
        )

        submitted = st.form_submit_button("Save Profile")

        if submitted:
            st.success("Child profile updated successfully!")
            
def ensure_profile_exists():
    """
    Ensures that a child profile has been created.
    Returns True if essential fields exist, otherwise False.
    """
    required_keys = ["child_name", "child_age"]

    # Check if essential fields exist and are filled
    for key in required_keys:
        if key not in st.session_state or st.session_state[key] in ("", None):
            return False

    return True