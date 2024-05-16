from openai import OpenAI

print("")

regex_query = input("What would you like your regex to match?\n")

message = f"Return a regex that matches the following case: '{regex_query}'"

client = OpenAI()

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
     {"role": "system", "content": "You must return a regex statement that satisfies the constraints you are given. Return the statement properly formatted between forward slashes, and with all necessary modifiers. Use global and multiline flags unless otherwise asked. Regex statement shouldn't include any other characters around it."},
    {"role": "user", "content": message}
  ]
)

print(chat_completion.choices[0].message.content)