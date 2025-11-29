# ai-resume-screening-agent

An AI-powered tool that analyzes and ranks resumes based on a job description using LLMs, NLP, and ATS-style evaluation.
Built using Python, Streamlit, Groq LLM API, and PDF parsing.

---
[ats.py code](https://github.com/brunda-yadav/ai-resume-screening-agent/blob/main/ats.py)
---
[ranking](https://github.com/brunda-yadav/ai-resume-screening-agent/blob/main/output_2.png)
---
[student one resume analysed ](https://github.com/brunda-yadav/ai-resume-screening-agent/blob/main/Screenshot%202025-11-29%20122955.png)

---

Features
- Upload one or multiple resumes (PDF format)
- Extract text using PyPDF2
- AI-powered analysis using Groq LLM
- ATS-style resume review
- Resume–Job Description (JD) matching score
- Ranks all candidates based on job fit
- Clean, modern Streamlit UI
- Works locally with secure .env API keys
---
How It Works:
User uploads resumes (PDF)
- The app extracts text using PyPDF2
- JD is given by the recruiter/hiring manager
- Groq LLM evaluates:
- Skills match
- Strengths & weaknesses
- Experience relevance
- ATS-style breakdown
- A Match Score (0–100%) is generated
- Candidates are ranked from strongest → weakest fit
---
Tech Stack:
- Python 3.10+
- Streamlit (UI framework)
- Groq LLM API
- PyPDF2 (PDF text extraction)
- dotenv (secure environment variables)
---
RUN:
streamlit run ats.py
---
Clone the Repository:
git clone https://github.com/brunda-yadav/ai-resume-screening-agent.git
Start the app


