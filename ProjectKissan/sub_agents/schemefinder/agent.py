# ./adk_agent_samples/mcp_agent/agent.py
import os
from google.adk.agents import LlmAgent, Agent
from google.adk.tools import google_search
from ... import prompt
from .tools import ScrapeWebsiteTool

root_agent = Agent(
    model="gemini-2.0-flash",
    name="Government_Scheme_Finder",
    instruction=prompt.GovernmentSchemeNavigator,
    tools=[ScrapeWebsiteTool],
)
