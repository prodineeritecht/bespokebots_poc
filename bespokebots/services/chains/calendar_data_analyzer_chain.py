from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import Extra
import json
from langchain.base_language import BaseLanguageModel
from langchain.callbacks.manager import (
    AsyncCallbackManagerForChainRun,
    CallbackManagerForChainRun,
)
from langchain import LLMChain
from langchain.output_parsers import PydanticOutputParser

from bespokebots.services.chains.prompts.calendar_analysis_chat_prompt import (
    CalendarAnalysisChatPrompt,
)
from bespokebots.services.chains.calendar_templates import (
    CalendarDataAnalyzerTemplates as Templates,
)
from bespokebots.services.chains.output_parsers import (
    CalendarAnalyzerOutputParserFactory,
)


class CalendarAnalysisLlmChain:
    """Wrapper around an LLM Chain which will be used to analyze a user's calendar data,
    hopefully making it easier and quicker for an LLM to answer user's questions
    regarding their schedule and when it makes sense to schedule events for."""

    def __init__(self, prompt, llm, output_parser=None):
        self.prompt: CalendarAnalysisChatPrompt = prompt
        """Prompt object to use."""
        self.llm: BaseLanguageModel = llm
        """Language model to use."""
        self.output_parser: PydanticOutputParser = (
            CalendarAnalyzerOutputParserFactory.create_output_parser()
            if output_parser is None
            else output_parser
        )

    @staticmethod
    def build_calendar_chain(
        prompt, llm, output_parser=None
    ) -> CalendarAnalysisLlmChain:
        """Build a CalendarAnalysisLlmChain object."""
        return CalendarAnalysisLlmChain(
            prompt=prompt,
            llm=llm,
        )

    def run_chain(self, events: str, user_requirements: str):
        """Wraps around LLMChain's run semantics to ensure the OutputParser is used."""
        slack_schedule_event_command = "1. schedule_event_slack: Use this tool when, based on your reasoning, the user should be prompted to schedule an event on their calendar.  This will ensure a good user experience"
        salck_scheudle_event_args = {
            "summary": {
                "title": "Summary",
                "description": "The summary of the event to schedule.",
            },
            "start": {
                "title": "Start",
                "description": "The start time of the event to schedule.",
            },
            "end": {
                "title": "End",
                "description": "The end time of the event to schedule.",
            },
            "description": {
                "title": "Description",
                "description": "The description of the event to schedule.",
            },
        }
        finish_command = '8. finish: use this to signal that you have finished all your objectives, args: "response": "final response to let people know you have finished your objectives"'
        tools = (
            f"{slack_schedule_event_command} args: {json.dumps(salck_scheudle_event_args)}"
            f"{finish_command}"
        )

        chain = LLMChain(llm=self.llm, prompt=self.prompt)
        output = chain(
            inputs={
                "events_to_analyze": events,
                "user_requirements": user_requirements,
                "output_parser_template": self.output_parser.get_format_instructions(),
                "tools": tools,
            }
        )
        return self.output_parser.parse(output["text"])
