import pytest

from langchain.schema import AIMessage, HumanMessage, SystemMessage
from bespokebots.services.chains.calendar_templates import (
    CalendarDataAnalyzerTemplates as Templates
)
from bespokebots.services.chains.prompts import CalendarAnalysisChatPrompt
from bespokebots.services.chains.output_parsers import (
    CalendarAnalyzerOutputParserFactory as OutputParserFactory
)

from langchain.llms.fake import FakeListLLM

from bespokebots.services.chains import CalendarAnalysisLlmChain

def test_calendar_analysis_chain_run(events):
    """Test CalendarAnalysisLlmChain.run_chain."""
    responses = ["""{"thoughts": {
    "text": "There are two events in the calendar: 'Kids with me' from 2023-05-29 to 2023-06-08 and 'Future Event' on 2023-06-07T22:48:28-04:00. The user wants to schedule a yoga class at 9:30 AM EST for one hour on either 6/7 or 6/8.",
    "reasoning": "I will check if there are any events on 6/7 and 6/8 at 9:30 AM EST for one hour. I will also ensure there is a 30-minute buffer before and after the yoga class.",
    "plan": "- Check for events on 6/7 and 6/8\n- Ensure 30-minute buffer before and after the yoga class\n- Determine the best day for the yoga class",
    "criticism": "The analysis assumes that the given events are the only ones to consider and that the user's timezone is the same as the event timezone.",
    "speak": "I will analyze the calendar events and determine the best day for a yoga class at 9:30 AM EST for one hour, considering the 30-minute buffer before and after the class."
    },
    "analysis": {
        "events_dates_comparison": "Comparing the events' dates to 6/7 and 6/8.",
        "event_conflict_detection": "Checking for event conflicts on 6/7 and 6/8 at 9:30 AM EST for one hour.",
        "available_time_slot_detection": "Identifying available time slots on 6/7 and 6/8.",
        "best_date_time_selection": "Selecting the best date and time for the yoga class based on the user's requirements.",
        "answer": "The best date for the yoga class is 6/8 since it satisfies the user's requirements and has the most available time slots."
    },
    "command": {
        "name": "schedule_yoga_class",
        "args": {
        "date_options": "6/7, 6/8",
        "time": "9:30 AM EST",
        "duration": "1 hour",
        "buffer": "30 minutes"
        }
    }
} """]    
    fake_llm = FakeListLLM(responses=responses)

    human_question = """I want to go to a Vinyasa yoga class either on Thursday 5/31/2023 or Friday 6/1/2023, both at 9:30 AM EST for one hour. Today is Tuesday 5/30/2023. Could you please check my calendar and tell me on which day, 5/31 or 6/1, I don’t have any existing events that the yoga class would overlap?"""
    
    prompt = CalendarAnalysisChatPrompt().from_user_request(human_question)
    output_parser = OutputParserFactory.create_output_parser()
    
    chain = CalendarAnalysisLlmChain.build_calendar_chain(
        prompt = prompt,
        llm = fake_llm,
        output_parser = output_parser
    )
    output = chain.run_chain(events = events(), user_requirements = "I need to be free on Monday and Tuesday")
    assert output.command.name == "schedule_yoga_class"
    assert output.analysis.answer == "The best date for the yoga class is 6/8 since it satisfies the user's requirements and has the most available time slots."
    assert output.thoughts.speak == "I will analyze the calendar events and determine the best day for a yoga class at 9:30 AM EST for one hour, considering the 30-minute buffer before and after the class."