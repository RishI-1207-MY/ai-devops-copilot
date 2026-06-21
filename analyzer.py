from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

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

    return llm.invoke(prompt)