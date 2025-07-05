import os
from google.adk.agents import LlmAgent, Agent
from google.adk.tools import google_search
from ... import prompt
from .tools import ScrapeWebsiteTool, datetool

root_agent = Agent(
    model="gemini-2.0-flash",
    name="market_analysis_agent",
    instruction=prompt.MarketAnalysis,
    tools=[ScrapeWebsiteTool],
)
