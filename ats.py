import streamlit as st
import re
import PyPDF2
from groq import Groq
from dotenv import load_dotenv
import os

# --------------------------------------------------------
# Load API key from .secrets.env (NOT hardcoded)
# --------------------------------------------------------
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# --------------------------------------------------------
# PDF EXTRACTION
# --------------------------------------------------------
def prepare_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    extracted_text = ""
    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            extracted_text += text + "\n"
    return extracted_text


# --------------------------------------------------------
# CALL LLM (uses your working model)
# --------------------------------------------------------
def get_llm_response(prompt, resume_text, job_description=""):
    text = prompt.format(resume=resume_text, jd=job_description)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": text}]
    )

    return response.choices[0].message.content


# --------------------------------------------------------
# MATCH SCORE EXTRACTION
# --------------------------------------------------------
def extract_match_score(text):
    match = re.search(r"(\d+)", text)
    if match:
        return int(match.group(1))
    return 0


# --------------------------------------------------------
# PROMPTS
# --------------------------------------------------------
prompt_review = """
You are an expert ATS resume analyst.
Provide a detailed review of this resume:

1. Key Skills  
2. Strengths  
3. Weaknesses  
4. Summary  

Resume:
{resume}
"""

prompt_match = """
Compare this resume with the following job description and give
ONLY a match percentage (0–100).

Resume:
{resume}

Job Description:
{jd}

Output format:
Match: 85%
"""


# --------------------------------------------------------
# UI
# --------------------------------------------------------
st.title("AI Resume Screening Agent (Groq Llama 3.3 70B)")
st.write("Upload resumes and paste the JD to rank candidates automatically.")

job_description = st.text_area("Paste Job Description Here", height=200)

uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

btn_review = st.button("Review ONE Resume")
btn_rank = st.button("Rank ALL Resumes")


# --------------------------------------------------------
# REVIEW MODE
# --------------------------------------------------------
if btn_review:
    if uploaded_files and len(uploaded_files) == 1:
        file = uploaded_files[0]
        st.info("Extracting resume text...")
        pdf_data = prepare_pdf(file)

        st.info("Analyzing resume…")
        response = get_llm_response(prompt_review, pdf_data)

        st.subheader("Resume Analysis")
        st.write(response)

    else:
        st.warning("Please upload EXACTLY ONE resume.")


# --------------------------------------------------------
# RANKING MODE
# --------------------------------------------------------
elif btn_rank:
    if not job_description.strip():
        st.warning("Please paste a Job Description.")
    elif not uploaded_files:
        st.warning("Please upload at least one resume.")
    else:
        st.info("Ranking candidates…")

        results = []
        for file in uploaded_files:
            pdf_data = prepare_pdf(file)
            response = get_llm_response(prompt_match, pdf_data, job_description)
            score = extract_match_score(response)
            results.append((file.name, score))

        results.sort(key=lambda x: x[1], reverse=True)

        st.subheader("Candidate Ranking")

        for rank, (name, score) in enumerate(results, start=1):
            if score >= 75:
                label = "⭐ Strong Match"
            elif score >= 50:
                label = "✅ Moderate Match"
            else:
                label = "⚠️ Weak Match"

            st.write(f"**Rank {rank}: {name} — {score}% Match** {label}")
