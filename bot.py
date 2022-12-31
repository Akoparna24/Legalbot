import openai

openai.api_key = "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"
completion = openai.Completion()

start_sequence = "\nLegalbot:"
restart_sequence = "\nHuman: "

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nLegalbot: I am an AI created by OpenAI. How can I help you today?\nHuman: What is the meaning of the taffic signal lights: red, gree, orange?\nLegalbot:",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=[" Human:", " Legalbot:"]
)

print(response)