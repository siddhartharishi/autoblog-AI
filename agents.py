from crewai import Agent
from tools import get_yt_tool

def create_agents():

    yt_tool = get_yt_tool()

    blog_researcher = Agent(
        role="Blog researcher from Youtube videos",
        goal="Get relevant video content for topic {topic} from YouTube channel",
        verbose=True,
        memory=True,
        backstory="Expert in researching YouTube content",
        tools=[yt_tool],
        allow_delegation=True
    )

    blog_writer = Agent(
        role="Blog Writer",
        goal="Write blog based on topic {topic}",
        verbose=True,
        memory=True,
        backstory="Expert blog writer",
        tools=[yt_tool],
        allow_delegation=False
    )

    return blog_researcher, blog_writer