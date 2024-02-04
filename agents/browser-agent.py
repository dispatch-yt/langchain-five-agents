import sys
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import ( create_async_playwright_browser, create_sync_playwright_browser)
from langchain.agents import AgentType, initialize_agent
from langchain_openai import ChatOpenAI, OpenAI

async_browser = create_sync_playwright_browser()
toolkit = PlayWrightBrowserToolkit.from_browser(sync_browser=async_browser)
tools = toolkit.get_tools()

llm = OpenAI(temperature=0)
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)
result = agent.run(sys.argv[1])
print(result)


