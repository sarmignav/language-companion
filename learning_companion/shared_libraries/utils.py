"""Common functions for language companion agent."""
from google.adk.agents.callback_context import CallbackContext
from google.genai import types as types

# Retry with exponetial backoff
retry_config=types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1, # Initial delay before first retry (in seconds)
    http_status_codes=[429, 500, 503, 504] # Retry on these HTTP errors
)

def init_state(callback_context: CallbackContext):
    callback_context.state.update({ 'target_language': 'Spanish', 'source_language': 'Chinese' })
