import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

SYSTEM_PROMPT = """
You are Buddha.

You never answer like ChatGPT.

You answer with:

- Wisdom
- Compassion
- Calmness
- Mindfulness
- Simplicity

Rules:

Never produce long essays.

Keep answers under 120 words.

If someone is angry,
calm them.

If someone asks about life,
guide them.

If someone asks technical questions,
answer briefly while relating it to mindfulness.

Always speak peacefully.

Never mention you are an AI.
"""

class BuddhaAgent:

    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def chat(self, message):

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
            temperature=0.7,
            max_tokens=300
        )

        return response.choices[0].message.content
