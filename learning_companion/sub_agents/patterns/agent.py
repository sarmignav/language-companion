from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini
from google.genai import types as ai_types

from learning_companion.sub_agents.patterns import prompt
from learning_companion.shared_libraries import types, utils

patterns_agent = Agent(
    name='patterns_agent',
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=utils.retry_config
    ),
    description=prompt.ROOT_AGENT_DESC,
    instruction=prompt.ROOT_AGENT_INSTR,
)
