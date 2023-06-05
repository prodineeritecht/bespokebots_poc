import pytest
from typing import List, Optional

from bespokebots.services.chains.prompts import (
    CalendarAnalysisChatPrompt
)
from bespokebots.services.chains.output_parsers import (
    CalendarAnalyzerOutputParserFactory
)

llm_response = """{
    "thoughts": {
        "text": "The user wants to attend a Vinyasa yoga class at 9:30 AM EST on 5/31/2023 or 6/1/2023. I need to analyze their calendar events and check if the requested yoga class time works with their current schedule.",
        "reasoning": "I will examine the calendar events on 5/31 and 6/1. According to the user's requirements, I need to ensure that there is at least 30 minutes of free time before and after the yoga class. I will also consider minimizing the number of appointments per day.",
        "plan": "- Find events on 5/31 and 6/1- Check for conflicts (30 min buffer)- Choose the day with the least number of appointments, if possible",
        "criticism": "The analysis is limited by the events provided in the calendar. If new events are created or existing events are updated, this analysis may not be accurate.",
        "speak": "I will check your calendar for 5/31 and 6/1 and see if there is enough free time for the Vinyasa yoga class. I'll make sure there's a 30-minute buffer before and after the class, as well as try to choose the day with fewer appointments."
    },
    "result": {
        "name": "check_calendar_availability",
        "answer": "On 5/31, there's a Therapy appointment at 10:00 AM, which conflicts with the yoga class. On 6/1, the yoga class can be scheduled without conflicts and with at least 30 minutes buffer before and after."
    }
}
"""

def test_inject_response_format_into_prompt(events):
    """Test that the response format is injected into the prompt."""
    prompt = CalendarAnalysisChatPrompt.from_user_request("hello")

    output_parser = CalendarAnalyzerOutputParserFactory.create_output_parser()

    formatted_prompt = prompt.format_prompt(
        events_to_analyze=events(),
        user_requirements="",
        output_parser_template=output_parser.get_format_instructions(),
    ).to_string()   

    print(formatted_prompt)

    assert formatted_prompt is not None
    assert (
        str.find(
            formatted_prompt,output_parser.get_format_instructions()
            )
     ) > -1
    
def test_parse_llm_response(events):
    output_parser = CalendarAnalyzerOutputParserFactory.create_output_parser()
    parsed_response = output_parser.parse(llm_response)
    assert parsed_response is not None
    assert parsed_response.result.answer == "On 5/31, there's a Therapy appointment at 10:00 AM, which conflicts with the yoga class. On 6/1, the yoga class can be scheduled without conflicts and with at least 30 minutes buffer before and after."
    assert parsed_response.thoughts.text == "The user wants to attend a Vinyasa yoga class at 9:30 AM EST on 5/31/2023 or 6/1/2023. I need to analyze their calendar events and check if the requested yoga class time works with their current schedule."
    assert parsed_response.thoughts.reasoning == "I will examine the calendar events on 5/31 and 6/1. According to the user's requirements, I need to ensure that there is at least 30 minutes of free time before and after the yoga class. I will also consider minimizing the number of appointments per day."
    assert parsed_response.thoughts.plan == "- Find events on 5/31 and 6/1- Check for conflicts (30 min buffer)- Choose the day with the least number of appointments, if possible"
    assert parsed_response.thoughts.criticism == "The analysis is limited by the events provided in the calendar. If new events are created or existing events are updated, this analysis may not be accurate."
    assert parsed_response.thoughts.speak == "I will check your calendar for 5/31 and 6/1 and see if there is enough free time for the Vinyasa yoga class. I'll make sure there's a 30-minute buffer before and after the class, as well as try to choose the day with fewer appointments."
    assert parsed_response.result.name == "check_calendar_availability"

