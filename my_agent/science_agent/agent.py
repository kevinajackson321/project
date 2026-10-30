from google.adk.agents.llm_agent import Agent

science_agent = Agent(
    model='gemini-3.8-flash',
    name='science_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',

    tools=[
        science_agent_tool,
    ]
)
