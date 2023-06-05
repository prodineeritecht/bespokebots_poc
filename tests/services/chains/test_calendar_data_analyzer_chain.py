import pytest

from langchain.schema import AIMessage, HumanMessage, SystemMessage
from bespokebots.services.chains.templates import (
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
    responses = ["""{
        "thoughts": {
            "text": "The user wants to attend a Vinyasa yoga class at 9:30 AM EST on 5/31/2023 or 6/1/2023. I need to analyze their calendar events and check if the requested yoga class time works with their current schedule.",
            "reasoning": "I will examine the calendar events on 5/31 and 6/1. According to the user's requirements, I need to ensure that there is at least 30 minutes of free time before and after the yoga class. I will also consider minimizing the number of appointments per day.",
            "plan": "- Find events on 5/31 and 6/1- Check for conflicts (30 min buffer)- Choose the day with the least number of appointments, if possible",
            "criticism": "The analysis is limited by the events provided in the calendar. If new events are created or existing events are updated, this analysis may not be accurate.",
            "speak": "I will check your calendar for 5/31 and 6/1 and see if there is enough free time for the Vinyasa yoga class. I'll make sure there's a 30-minute buffer before and after the class, as well as try to choose the day with fewer appointments."
        },
        "result": {
            "name": "check_calendar_availability",
            "answer": "On 5/31, there's a Therapy appointment at 10:00 AM, which conflicts with the yoga class. On 6/1, the yoga class can be scheduled without conflicts and with at least 30 minutes buffer before and after.",
            "next_action": "schedule_yoga_class"
        }
    }"""]    
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
    assert output.result.name == "check_calendar_availability"
    assert output.result.answer == "On 5/31, there's a Therapy appointment at 10:00 AM, which conflicts with the yoga class. On 6/1, the yoga class can be scheduled without conflicts and with at least 30 minutes buffer before and after."
    assert output.result.next_action == "schedule_yoga_class"