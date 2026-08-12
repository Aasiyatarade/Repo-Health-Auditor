from crewai import Agent
from llm_config import llm

from tools import (
    github_metadata_tool,
    github_issue_tool,
    github_community_tool
)

metadata_collector = Agent(
    role="Repository Metadata Collector",
    goal="Collect repository metadata.",
    backstory="GitHub metadata expert.",
    tools=[github_metadata_tool],
    llm=llm,
    verbose=True
)

community_researcher = Agent(
    role="Community Signal Researcher",
    goal="Analyze repository popularity.",
    backstory="Open-source community expert.",
    tools=[github_community_tool],
    llm=llm,
    verbose=True
)

issue_engineer = Agent(
    role="Issue Triage Engineer",
    goal="Analyze GitHub issues.",
    backstory="Senior software engineer.",
    tools=[github_issue_tool],
    llm=llm,
    verbose=True
)

report_writer = Agent(
    role="Health Report Writer",
    goal="Write a professional Markdown report.",
    backstory="Technical report specialist.",
    llm=llm,
    verbose=True
)