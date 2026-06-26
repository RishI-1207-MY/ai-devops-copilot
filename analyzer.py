from groq import Groq
import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_logs(log_text):

    prompt = f"""
You are a Senior DevOps Engineer.

Analyze the logs.

Return exactly:

Severity: CRITICAL/HIGH/MEDIUM/LOW

Root Cause:
<root cause>

Impact:
<impact>

Recommendation:
<recommendation>

Logs:
{log_text[:5000]}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content