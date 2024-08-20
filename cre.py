from crewai import Crew,Process
from crewai import Task
from tools import yt_tool
from agent import blog_researcher,blogwriter
from task import research_task,writing_task

crew=Crew(
    agents=[blog_researcher,blogwriter],
    tasks=[research_task,writing_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)
result=crew.kickoff(inputs={'topic':'AI VS ML VS DL VS Data Science'})
print(result)