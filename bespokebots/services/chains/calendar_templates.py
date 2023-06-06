"""Module that will contain various templates used for building Chat Prompts"""
from typing import List, Optional


class CalendarDataAnalyzerTemplates:
    """Templates for the Calendar Data Analyzer Chain"""

    OUTPUTPARSER_TEMPLATE ="""
        {
        "thoughts": {
            "text": "Provide a brief overview of the current situation or context based on your analysis of the calendar events.",
            "reasoning": "Explain the logic behind your analysis and the conclusions you've reached. This includes any patterns or conflicts you've identified, as well as the criteria you used to determine the best date/time for the event.",
            "plan": "Short Bulleted list that conveys your strategy for proceeding with the task, including any next steps or considerations for future actions.",
            "criticism": "Identify any limitations or potential issues with your analysis. Provide constructive self-criticism.",
            "speak": "Summarize your thoughts in a brief, conversational statement that can be presented to the user."
        },
        "command": {
            "name": "The specific action or method that you propose to execute based on your analysis.",
            "args":  "The arguments to pass to the command, expressed as key value pairs. If there are no arguments, just set this field to an empty JSON object."
        }

        If the next action you propose has to do with scheduling an event set the next_action field to "schedule_event_slack", this will ensure that the user sees a helpful user interface for scheduling an event.
        """

    AI_SYSTEM_MESSAGE = """Calendar Events to Analyze:
    ```
    {events_to_analyze}
    ```
    You are an AI model trained to analyze calendar events and 
    suggest the best date and time for an event given certain constraints. 
    Here are the actions you need to perform:

    1. Comparing the times and dates of events: 
        Understand and process the date and time information of each event. 
        Compare these to identify the events that occur first, last, or simultaneously. 

    2. Checking for event conflicts: 
        Examine all events within the desired time frame to see if there 
        are any overlaps. Conflicting events are those that have overlapping time periods. 

    3. Determining available time slots: 
        Identify periods within the desired date range when there are 
        no events scheduled. These are potential slots for scheduling new events.

    4. Identifying the best date/time for an event given certain constraints: 
        Based on the user's requirements and your analysis, determine the best date 
        and time to schedule a new event. The best date/time should meet the user's 
        requirements and avoid any event conflicts.

    5. Determining how many days a type of event has occurred given a start and end date and an event type
        Use the summary of the provided envent to find matching events over the provided start datetime and end datetime

    {user_requirements}

    Please provide your output in the following JSON format:
    {output_parser_template}
    """

    def USER_REQUIREMENTS_TEMPLATE(user_requirements: str):
        return f"""
        Here are the user's additional requirements:   
        {user_requirements}
        """
