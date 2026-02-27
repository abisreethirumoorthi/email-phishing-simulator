import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Email Phishing Simulator",
    layout="wide"
)

# ---------------- HEADER ----------------

st.title("📧 Email Phishing Simulator")
st.caption("Educational Phishing Detection & Awareness | Output Dashboard")

st.divider()

# ---------------- EMAIL INPUT ----------------

st.subheader("Simulated Email Content")

email_text = st.text_area(
    "Email Body",
    value="Your account has been suspended. Click the link below to verify your identity immediately.",
    height=120
)

sender = st.text_input("Sender Email", "support@secure-account-check.com")
link = st.text_input("Embedded Link", "http://secure-login-verify.com")

st.divider()

# ---------------- ANALYSIS ----------------
if st.button("Analyze Email"):
    st.subheader("Analysis Output")

# Simulated risk logic

    risk_score = 78
    verdict = "Phishing Suspected"

    col1, col2, col3 = st.columns(3)
    col1.metric("Risk Score", f"{risk_score} / 100")
    col2.metric("Verdict", verdict)
    col3.metric("Confidence", "92%")

    st.progress(risk_score / 100)

    st.divider()

    # ---------------- DETECTION RESULTS ----------------

    st.subheader("Detection Indicators")

    indicators = pd.DataFrame({
        "Indicator": [
            "Urgent Language",
            "Suspicious Sender Domain",
            "External Embedded Link",
            "Credential Request"
        ],
        "Detected": ["Yes", "Yes", "Yes", "Yes"]
    })

    st.dataframe(indicators, use_container_width=True)

    # ---------------- AWARENESS OUTPUT ----------------
    st.subheader("User Awareness Output")

    st.warning("⚠ This email shows strong signs of phishing.")
    st.info("✔ Never click unknown links or share credentials.")
    st.info("✔ Verify sender identity before responding.")

    st.caption(
        "Model: Rule-Based Phishing Detection + NLP Patterns | Mode: Educational Simulation"
    )

else:
    st.info("Enter email details and click 'Analyze Email' to simulate phishing detection.")
