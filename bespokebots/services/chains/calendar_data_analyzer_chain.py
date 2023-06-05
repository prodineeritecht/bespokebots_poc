from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import Extra

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
from bespokebots.services.chains.templates import (
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
        chain = LLMChain(llm = self.llm, prompt = self.prompt)
        output = chain(inputs={'events_to_analyze': events, 'user_requirements': user_requirements, 'output_parser_template': self.output_parser.get_format_instructions()})
        return self.output_parser.parse(output['text'])