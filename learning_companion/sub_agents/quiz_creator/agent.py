from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools.mcp_tool import McpToolset, StreamableHTTPConnectionParams

from learning_companion.sub_agents.quiz_creator import prompt
from learning_companion.shared_libraries import utils

quiz_creator_agent = Agent(
    name='quiz_creator_agent',
    model=Gemini(
        model="gemini-2.5-flash",
        retry_options=utils.retry_config
    ),
    description=prompt.ROOT_AGENT_DESC,
    instruction=prompt.ROOT_AGENT_INSTR,
    tools=[
      McpToolset(
        connection_params=StreamableHTTPConnectionParams(
          url="http://10.89.0.2:9000/mcp",
          # headers={"Authorization": "Bearer your-auth-token"},
        ),
      )
    ],
)
