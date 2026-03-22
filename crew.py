# crew.py

import os
from crewai import Crew, Process
from agents import create_agents
from tasks import create_tasks

def run_crew(topic, channel, api_key):

    # set dynamic values
    os.environ["OPENAI_API_KEY"] = api_key
    os.environ["YOUTUBE_CHANNEL"] = channel

    # create agents dynamically
    blog_researcher, blog_writer = create_agents()

    # create tasks dynamically
    research_task, write_task = create_tasks(
        blog_researcher,
        blog_writer
    )

    crew = Crew(
        agents=[blog_researcher, blog_writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff(inputs={"topic": topic})

    return result