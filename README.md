# ai-resume-screening-agent
AI-powered ATS Resume Analyzer using Groq Llama 3.3 70B  Set it to Public
AI-Resume-Screening-Agent

Developed an AI-powered resume screening tool using Python, Streamlit, and Groq LLM API.
The app extracts resume text, analyzes it against a given Job Description, calculates a match percentage, and provides ATS-style insights.

AI Resume Screening Agent

🔗 ats.py code

🔗 requirements

🔗 Sample Output

Features

Calculates match percentage

Highlights missing keywords / skills

Provides improvement suggestions

Extracts PDF text automatically

Ranks multiple resumes based on JD

How to Run

Install dependencies

pip install -r requirements.txt


Add your Groq API key
Create a .env file in the project folder:

GROQ_API_KEY=your_key_here


Start the app

streamlit run ats.py
