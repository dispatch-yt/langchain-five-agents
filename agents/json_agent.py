import json, sys
from langchain.agents import ( create_json_agent, AgentExecutor)
from langchain_community.agent_toolkits import JsonToolkit
from langchain.chains import LLMChain
from langchain.llms.openai import OpenAI
from langchain.requests import TextRequestsWrapper
from langchain.tools.json.tool import JsonSpec

with open('../sources/people.json', 'r') as reader:
    data = json.load(reader)

json_spec = JsonSpec(dict_= data, max_value_length=4000)
json_toolkit = JsonToolkit(spec=json_spec)

json_agent_executor = create_json_agent(
    llm=OpenAI(temperature=0),
    toolkit=json_toolkit,
    verbose=True
)

json_agent_executor.run(sys.argv[1])
