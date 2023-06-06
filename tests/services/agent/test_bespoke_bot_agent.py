import pytest

from langchain.callbacks import get_openai_callback
from langchain.llms.fake import FakeListLLM
from bespokebots.services.agent import BespokeBotAgent
from langchain.docstore import InMemoryDocstore
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import faiss

#Things the ai assistant needs to be able to do
#1. Take in a user goal
#2. Take in a list of tools
#3. Take in an LLM Model, will default to OpenAI GPT-4
#4. Take in a vector store, will default to FAISS maybe?
#5. Take in a prompt
#6. Take in an outputparser, will default to a custom output parser
#7. Execute the agent's LLMChain in a loop until the user goal is met
#   a. The loop will also be built with either a timeout or a max number of iterations


def test_run_agent():
    prefix = """Your role is that of an Assistant and Coach to a client. Help your client by answering their quesitons and completing tasks for them.
    You have four main responsibilities when it comes to helping out your human client
    Time Management: Schedule management, event planning, as well as daily and weekly schedule reviews
    Daily Log: Help your client keep track of their daily activities, thoughts, and metrics.  Also help them track their ideas around various initiatives.
    Habit Tracking: Help your client track their current habits, help them develop new habits and replace bad habits.
    Procrastination Slayer: Help your client break through procrastination by recommending stragegies and even setting reminders and timers for them.
    """

    suffix = """Be sure to minimize the number of commands you have to use to complete the client's request.
    Question:{input}

    {agent_scratchpad}
    """

    embeddings_model = OpenAIEmbeddings()
    # Initialize the vectorstore as empty
    
    embedding_size = 1536
    index = faiss.IndexFlatL2(embedding_size)
    vectorstore = FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})

    bb_agent = BespokeBotAgent(
        ai_name="BespokeBot",
        memory=vectorstore
    )

    executor = bb_agent.initialize_agent(prefix, suffix)

    weather_in_portland_request = """Hi, what's the weather like in Portland today?"""
    count_days_request = """Hi could you look at the events on my calendar from 5/1/2023 to today 6/2/2023 and tell me how many days in that time period my kids have been with me? You can look for multi-day events with titles like “Kids with me” or “Rob kid week”."""
    output = executor.run(count_days_request)
    print(output)

    assert output is not None





