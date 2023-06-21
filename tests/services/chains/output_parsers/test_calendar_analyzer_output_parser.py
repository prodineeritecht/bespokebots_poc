import pytest
from typing import List, Optional

from bespokebots.services.chains.prompts import (
    CalendarAnalysisChatPrompt
)
from bespokebots.services.chains.output_parsers import (
    CalendarAnalyzerOutputParserFactory,
    Thoughts,
    Analysis,
    Command,
    CalendarAnalysisResponse,
)

llm_response = """{"thoughts": {
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
    assert parsed_response.thoughts.text == "There are two events in the calendar: 'Kids with me' from 2023-05-29 to 2023-06-08 and 'Future Event' on 2023-06-07T22:48:28-04:00. The user wants to schedule a yoga class at 9:30 AM EST for one hour on either 6/7 or 6/8."
    assert parsed_response.thoughts.reasoning == "I will check if there are any events on 6/7 and 6/8 at 9:30 AM EST for one hour. I will also ensure there is a 30-minute buffer before and after the yoga class."
    assert parsed_response.thoughts.plan == "- Check for events on 6/7 and 6/8\n- Ensure 30-minute buffer before and after the yoga class\n- Determine the best day for the yoga class"
    assert parsed_response.thoughts.criticism == "The analysis assumes that the given events are the only ones to consider and that the user's timezone is the same as the event timezone."
    assert parsed_response.thoughts.speak == "I will analyze the calendar events and determine the best day for a yoga class at 9:30 AM EST for one hour, considering the 30-minute buffer before and after the class."
    assert parsed_response.analysis.events_dates_comparison == "Comparing the events' dates to 6/7 and 6/8."
    assert parsed_response.analysis.event_conflict_detection == "Checking for event conflicts on 6/7 and 6/8 at 9:30 AM EST for one hour."
    assert parsed_response.analysis.available_time_slot_detection == "Identifying available time slots on 6/7 and 6/8."
    assert parsed_response.analysis.best_date_time_selection == "Selecting the best date and time for the yoga class based on the user's requirements."
    assert parsed_response.analysis.answer == "The best date for the yoga class is 6/8 since it satisfies the user's requirements and has the most available time slots."
    assert parsed_response.command.name == "schedule_yoga_class"
    assert parsed_response.command.args is not None

def test_deserialze_calendar_analysis_response():
    """Test that the CalendarAnalysisResponse can be deserialized from a String, but not JSON."""
    thoughts_text = """Thoughts(text='The user wants to schedule a yoga class on either 6/7 or 6/8 at 9:30 AM EST for one hour. We need to analyze the calendar events to determine if there is an available time slot on either of these days.', reasoning='I will analyze the calendar events to find any existing events on 6/7 and 6/8. Then, I will check if there is a 30-minute buffer before and after the proposed yoga class time. Finally, I will choose the day with the least number of appointments.', plan='1. Analyze the calendar events on 6/7 and 6/8. 2. Check for 30-minute buffers before and after the proposed yoga class time. 3. Choose the day with the least number of appointments.', criticism='The analysis assumes that the calendar events provided are complete and up-to-date. If there are any changes or additional events, the suggested time slot may not be accurate.', speak='I will analyze the calendar events on 6/7 and 6/8 to determine if there is an available time slot for a yoga class at 9:30 AM EST for one hour.')"""
    thoughts = Thoughts(data=thoughts_text)

    assert thoughts is not None
