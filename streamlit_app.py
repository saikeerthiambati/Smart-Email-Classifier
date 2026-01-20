import streamlit as st

st.set_page_config(
    page_title="AI Powered Smart Email Classifier",
    page_icon="📧",
    layout="centered"
)

st.markdown(
    """
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    .main-title {
        font-size: 40px;
        font-weight: 700;
        color: #4ea1ff;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 16px;
        color: #b0b0b0;
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">📧 AI Powered Smart Email Classifier</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enterprise Email Categorization & Urgency Detection</div>', unsafe_allow_html=True)

email_text = st.text_area(
    "✉️ Enter Email Content",
    placeholder="Paste the email content here...",
    height=180
)

def classify_email(text):
    text = text.lower()
    if any(word in text for word in ["urgent", "immediately", "asap", "critical"]):
        urgency = "High"
    else:
        urgency = "Normal"

    if any(word in text for word in ["invoice", "payment", "salary"]):
        category = "Finance"
    elif any(word in text for word in ["meeting", "schedule", "appointment"]):
        category = "Meetings"
    elif any(word in text for word in ["offer", "promotion", "discount"]):
        category = "Marketing"
    else:
        category = "General"

    return category, urgency

if st.button("🚀 Classify Email"):
    if email_text.strip() == "":
        st.warning("Please enter email content.")
    else:
        category, urgency = classify_email(email_text)
        st.success("✅ Email Classified Successfully")
        st.write(f"**Category:** {category}")
        st.write(f"**Urgency:** {urgency}")

st.markdown(
    "<hr style='margin-top:40px'>"
    "<p style='text-align:center;color:gray;'>Built by Sai Keerthi · Infosys Springboard Project</p>",
    unsafe_allow_html=True
)
