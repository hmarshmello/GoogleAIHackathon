# ./adk_agent_samples/mcp_agent/agent.py
import os
from google.adk.agents import LlmAgent, Agent
from ... import prompt

root_agent = Agent(
    model='gemini-2.0-flash',
    name='crop_analysis_agent',
    instruction=prompt.CropDiseaseDiagnosis,
)