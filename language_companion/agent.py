# import sqlite3

from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini
from google.adk.runners import Runner
from google.adk.tools import google_search, AgentTool, ToolContext

from language_companion import prompt
from language_companion.shared_libraries import utils

from language_companion.sub_agents.breakdown.agent import breakdown_agent
from language_companion.sub_agents.explainer.agent import explainer_agent
from language_companion.sub_agents.patterns.agent import patterns_agent
from language_companion.sub_agents.vocabulary.agent import vocabulary_agent

# root_agent = explainer_agent
root_agent = Agent(
    name='root_agent',
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=utils.retry_config
    ),
    description=prompt.ROOT_AGENT_DESC,
    instruction=prompt.ROOT_AGENT_INSTR,
    tools=[
      AgentTool(breakdown_agent),
      AgentTool(explainer_agent),
      AgentTool(patterns_agent),
      AgentTool(vocabulary_agent),
    ],
    before_agent_callback=utils.init_state,
)
