import os
from pathlib import Path 
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)

model="openai/gpt-oss-120b"

def llm_ans(prompt):
    message = {
        "role":"user",
        "content": prompt
    }
    message = [message]
    response = client.chat.completions.create(model=model,messages=message)
    ans = response.choices[0].message.content
    return ans

bad_prompt = """
ROLE :
You are a support assistant at a mobile/laptop company
TASK :
You have to classify the issue in category
CONSTRAINT :
You have to classify the issue in one of three categories namely billing, technical, return.
OUTPUT FORMAT :
Your answer should be in one word only. The one word should be one of the categories given in constraints
EXAMPLE :
For instance if a user complain says he wants a refund then the category is return
FALLBACK :
If the issue is unrelated to any of the categories mentioned in constraint, then the answer should be OTHER

This is user complaint:
my laptop is not working
"""

print(llm_ans(bad_prompt))


