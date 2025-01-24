# from openai import OpenAI
# import os
# from dotenv import load_dotenv
from actions import *
from prompts import *
# from json_helpers import *

from SimplerLLM.language.llm import LLM, LLMProvider
from SimplerLLM.tools.json_helpers import extract_json_from_text


# load_dotenv()

# openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

llm_instance = LLM.create(LLMProvider.OPENAI, model_name="gpt-4o-mini")

# def generate_text_with_conversation(messages, model = "gpt-4o-mini"):
#   response = openai_client.chat.completions.create(
#     model=model,
#     messages=messages
#   )
#   return response.choices[0].message.content

# available_actions = {
#   "get_response_time": get_response_time
# }

available_actions = {
    "get_seo_page_report": get_seo_page_report
}

# website = input("Enter a website: ")

# user_prompt = f"What is the response time of {website}.com?"

user_query = input("Enter a command: ")

messages = [
  {"role" : "system", "content": system_prompt},
  {"role" : "user", "content" : user_query},
]

turn_count = 1
max_turns = 5

while turn_count < max_turns:
  print(f"Loop: {turn_count}")
  print("---------------------")
  turn_count += 1
  
  agent_response = llm_instance.generate_response(messages=messages)
  
  messages.append({"role": "assistant", "content": agent_response})

  print(agent_response)
  
  # json_function = extract_json_from_text(response)
  
  # if json_function:
  #   function_name = json_function[0]['function_name']
  #   function_params = json_function[0]['function_params']
    # if function_name not in available_actions:
    #   # raise Exception(f"Unknown action: {function_name}: {function_params}")
    #   print("Information unavailable.")
    #   break
    # print(f" -- running {function_name} {function_params}")
    # action_function = available_actions[function_name]
    
    # result = action_function(**function_params)
    # function_result_message = f"Action Response: {result}"
    # messages.append({"role": "user", "content": function_result_message})
    # print(function_result_message)
  # else:
  #   break