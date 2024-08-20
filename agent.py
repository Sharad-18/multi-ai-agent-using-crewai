from crewai import Agent
import os 
from dotenv import load_dotenv
from tools import yt_tool
from langchain_groq import ChatGroq
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]=os.getenv("OPENAI_MODEL_NAME")
llm=ChatGroq(api_key="OPENAI_API_KEY",model="OPENAI_MODEL_NAME")


blog_researcher=Agent(
    role='Blog Reseacher from Youtube Videos',
    goal='get the relevant video Content for the topic {topic} from YT Channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI data Science , machine Learning , Deep learning and Generative Ai"
    ),
    tools=[yt_tool],
    allow_delegation=True,
    llm=llm
   
)

# create blog writing agent 
blogwriter=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT Channel',
    verbose=True,
    memory=True,
    backstory=(
        "With A flair for simplifying complex topics, you craft"
        "engaging narratives that capativate and educate,bringing new "
        "discover to light in accesible manner"
    ),
    tools=[yt_tool],
    allow_delegation=True
    llm=llm
)
