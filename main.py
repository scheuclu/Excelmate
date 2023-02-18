"import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    model="text-davinci-002",
    # prompt=" Write an example VBA function that will take a list of",
    prompt=""
           "def sum_list(arr) -> int:",
    temperature=0.1,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=1
)

print(f"{response=}")
print(f"{response.choices[0].text}")
"