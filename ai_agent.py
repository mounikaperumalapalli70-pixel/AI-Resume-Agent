import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Read Gemini API Key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_resume(user_data):
    prompt = f"""
You are an expert ATS Resume Writer.

Create a professional one-page resume.

User Details:

Name: {user_data['name']}
Email: {user_data['email']}
Phone: {user_data['phone']}
Location: {user_data['location']}
LinkedIn: {user_data['linkedin']}
GitHub: {user_data['github']}
Education: {user_data['education']}
Skills: {user_data['skills']}
Projects: {user_data['projects']}
Experience: {user_data['experience']}
Certifications: {user_data['certifications']}
Languages: {user_data['languages']}
Career Objective: {user_data['objective']}

Instructions:
- Make the resume ATS-friendly.
- Use professional headings.
- Improve the wording where appropriate.
- Highlight technical skills and achievements.
- Keep the formatting clean and professional.
"""

    response = model.generate_content(prompt)

    return response.text