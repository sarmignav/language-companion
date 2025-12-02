from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini

from learning_companion.sub_agents.explainer import prompt
from learning_companion.shared_libraries import types, utils

explainer_agent = Agent(
    name='explainer_agent',
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=utils.retry_config
    ),
    description=prompt.ROOT_AGENT_DESC,
    instruction=prompt.ROOT_AGENT_INSTR,
    # output_schema=types.SentenceAnalysis,
)
