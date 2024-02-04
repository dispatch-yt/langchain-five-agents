import sys
from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

db_uri = "postgresql+psycopg2://postgres:postgres@localhost:5432/school"

llm = ChatOpenAI()
sqlDatabaseToolkit = SQLDatabaseToolkit(db=SQLDatabase.from_uri(db_uri), llm=llm)

executor = create_sql_agent(
    llm=llm,
    toolkit=sqlDatabaseToolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)
executor.run(sys.argv[1])
