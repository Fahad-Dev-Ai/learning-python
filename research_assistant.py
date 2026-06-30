import warnings
warnings.filterwarnings("ignore")
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.prebuilt import create_react_agent
from langchain.tools import tool

llm = ChatGroq(model = "openai/gpt-oss-120b")
search = DuckDuckGoSearchRun()

@tool
def summarizer(text):
    """this tool is used to summarize long informational texts into plain and simple bullet points"""
    print("it was called")
    bullets = llm.invoke(f"""summarize this text {text} into plain and simple bullets 
                         , dont miss any given information amd give clean readable bullets""")
    return bullets.content

tools = [search,summarizer]
llm_with_tools = llm.bind_tools(tools)

agent = create_react_agent(llm_with_tools,tools)
topic = input("Type the topic or question you want to get information of : ")
summary1 = agent.invoke(
{"messages":[{"role" : "user" , "content" :f"""research about this topic {topic} and give answer in form of 
                clean and plain bullets while actually using the summarizer tool """}]},
                  config = {"recursion_limit" : 25} 
                  )
print(summary1["messages"][-1].content)