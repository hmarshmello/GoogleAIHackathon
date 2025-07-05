# ./adk_agent_samples/mcp_agent/agent.py
import os
from google.adk.agents import Agent
from . import prompt
from .sub_agents import crop_agent, scheme_agent, market_agent


def datetool():
    from datetime import date

    return date.today().strftime("%d-%b-%Y")


root_agent = Agent(
    model="gemini-2.0-flash",
    name="All_in_One_FarmerManager",
    instruction=prompt.Manager,
    sub_agents=[crop_agent, scheme_agent, market_agent],
    tools=[datetool],  # Add the date tool to the root agent
)
