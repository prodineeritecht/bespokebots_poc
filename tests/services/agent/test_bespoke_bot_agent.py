import pytest

from langchain.callbacks import get_openai_callback
from langchain.llms.fake import FakeListLLM
from bespokebots.services.agent import BespokeBotAgent
from bespokebots.services.chains.templates import (
    STRUCTURED_CHAT_PROMPT_PREFIX, 
    STRUCTURED_CHAT_PROMPT_SUFFIX
    )
from langchain.agents.structured_chat.prompt import SUFFIX
from langchain.docstore import InMemoryDocstore
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import faiss

from bespokebots.models import (
    CommunicationChannel
)

import json

#Things the ai assistant needs to be able to do
#1. Take in a user goal
#2. Take in a list of tools
#3. Take in an LLM Model, will default to OpenAI GPT-4
#4. Take in a vector store, will default to FAISS maybe?
#5. Take in a prompt
#6. Take in an outputparser, will default to a custom output parser
#7. Execute the agent's LLMChain in a loop until the user goal is met
#   a. The loop will also be built with either a timeout or a max number of iterations

class FakeSlackCommsChannel(CommunicationChannel):
    def __init__(self, name, channel_id):
        self.name = name
        self.channel_id = channel_id

    def send_response(self, response: str):
        return "RESPONSE SENT"
    
    def format_response(self, response: str):
        return "RESPONSE FORMATTED"

def test_run_agent(create_bespoke_bot_agent):
    prefix = STRUCTURED_CHAT_PROMPT_PREFIX

    suffix = STRUCTURED_CHAT_PROMPT_SUFFIX

    bb_agent = create_bespoke_bot_agent()

    bb_agent.initialize_agent(prefix, suffix)


    weather_in_portland_request = """Hi, what's the weather like in Portland today?"""
    count_days_request = """Hi could you look at the events on my calendar from 5/1/2023 to today 6/2/2023 and tell me how many days in that time period my kids have been with me? You can look for multi-day events with titles like “Kids with me” or “Rob kid week”."""
    next_kid_visit = """Hi Tom, I am trying to plan something with a friend, but need to know what my kid schedule looks like.  Today is Tuesday, 6/6/2023, my kids go back to their mom's house on Wednesday, 6/7/2023.  Can you tell me when my next kid visit is after our current one?"""
    vinyasa = """I want to go to a Vinyasa yoga class either on Wednesday 6/7/2023 or Thursday 6/8/2023, both at 9:30 AM EST for one hour. Today is Tuesday 6/6/2023. Could you please check my calendar and tell me on which day, 6/7 or 6/8, I don’t have any existing events that the yoga class would overlap? You can ignore the "Kids with me" events for this request."""
    weekly_planning = """Hi, I am trying to plan out my week next week, can you tell me what I have on my calendar for next week?  I am looking for events that between Monday 6/12/2023 and Sunday 6/18/2023."""


    output = bb_agent.executor.run(weekly_planning)
    print(output)

    assert output is not None

def test_agent_response_with_event_list_can_be_parsed_as_json(create_bespoke_bot_agent):
    prefix = STRUCTURED_CHAT_PROMPT_PREFIX

    suffix = STRUCTURED_CHAT_PROMPT_SUFFIX

    bb_agent = create_bespoke_bot_agent()

    bb_agent.initialize_agent(prefix, suffix)

    fake_comms_channel = FakeSlackCommsChannel("Fake Slack Channel", "12345")

    weekly_planning = """Hi, I am trying to plan out my week next week, can you tell me what I have on my calendar for next week?  I am looking for events that occur between Monday 6/12/2023 and Sunday 6/18/2023."""

    output = bb_agent.run_agent(weekly_planning)

    #punting on this test for now, not going to sweat the comms channel stuff yet.
    assert output is not None



        





