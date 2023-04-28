
import openai
openai.api_key = "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"

params = {}

params["temperature"] = 0.7
params["max_tokens"]=256
params["model"] = "text-davinci-003"

prompt = "Why is water conservation important?"

def llm(prompt):

  res = openai.Completion.create(
      engine = params["model"],
      prompt = prompt,
      temperature = params["temperature"],
      max_tokens = params["max_tokens"],
  )

  return res.choices[0].text
  
  llm("Why is water conservation important? ")
  
