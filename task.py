from crewai import Task
from tools import yt_tool
from agent import blog_researcher,blogwriter

# reasearcher Task 
research_task=Task(
    description=(
        "identify the video {topic}."
        "Get detailed information about the video from the channel"
    ),
    expected_output='A comprehensive 3 paragraph long report based on the {topic} of video',
    tools=[yt_tool]
    agent=blog_researcher
    
) 

writing_task=Task(
    description=(
        "Get detailed information about the video from the channel on the topic {topic}"
    ),
    expected_output='Summerize the info from youtube channel video on the topic {topic}',
    tools=[yt_tool]
    output_file='new-blog-post.md'
    
) 