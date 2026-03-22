from crewai import Task

def create_tasks(blog_researcher, blog_writer):

    research_task = Task(
        description=(
            "Find videos related to {topic} from the YouTube channel. "
            "Do not rely on exact match, find relevant content."
        ),
        expected_output="Detailed research summary of the topic.",
        agent=blog_researcher,
    )

    write_task = Task(
        description=(
            "Write a detailed blog on {topic} using the research."
        ),
        expected_output="Full blog content.",
        agent=blog_writer,
    )

    return research_task, write_task