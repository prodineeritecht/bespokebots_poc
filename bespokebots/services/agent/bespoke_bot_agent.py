from __future__ import annotations

from typing import List, Optional

from pydantic import ValidationError
import os

from langchain.chains import LLMChain
from langchain import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chat_models.base import BaseChatModel
from langchain.tools.base import BaseTool
from langchain.callbacks.base import BaseCallbackManager
from langchain.callbacks import StdOutCallbackHandler
from langchain.tools.human.tool import HumanInputRun
from langchain.vectorstores.base import VectorStoreRetriever
from langchain.output_parsers import PydanticOutputParser
from langchain.agents import Tool, ZeroShotAgent, AgentExecutor,StructuredChatAgent
from langchain.agents import AgentType
from langchain.callbacks import get_openai_callback
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    BaseMessage,
)

from langchain.docstore import InMemoryDocstore
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import faiss

from langchain.tools.file_management.read import ReadFileTool
from langchain.tools.file_management.write import WriteFileTool
from langchain.utilities import SerpAPIWrapper

from bespokebots.services.agent.google_calendar_tools import (
    GoogleCalendarCreateEventTool,
    GoogleCalendarViewEventsTool,
    GoogleCalendarUpdateEventTool,
    GoogleCalendarDeleteEventTool,
)
from bespokebots.services.chains.output_parsers import (
    CalendarAnalyzerOutputParserFactory
)
from bespokebots.services.chains import CalendarDataAnalyzerTool
from bespokebots.models import (
    CommunicationChannel
)

from bespokebots.services.agent.todoist_tools import (
    CreateTaskTool,
    CloseTaskTool,
    ViewProjectsTool,
    CreateProjectTool
) 


# Things the ai assistant needs to be able to do
# 1. Take in a user goal
# 2. Take in a list of tools
# 3. Take in an LLM Model, will default to OpenAI GPT-4
# 4. Take in a vector store, will default to FAISS maybe?
# 5. Take in a prompt
# 6. Take in an outputparser, will default to a custom output parser
# 7. Execute the agent's LLMChain in a loop until the user goal is met
#   a. The loop will also be built with either a timeout or a max number of iterations


class BespokeBotAgent:
    """The BespokeBotAgent class is responsible for handling the agent mechanics required for the digital assistant.
    This class is really a wrapper around the StructuredChatAgent class from langchain. It is responsible for
    setting up the tools, the LLMChain, and the agent itself. It also handles the execution of the agent.

    """
    # Default vector store
    embeddings_model = OpenAIEmbeddings()
    # Initialize the vectorstore as empty
    
    embedding_size = 1536
    index = faiss.IndexFlatL2(embedding_size)
    vectorstore = FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})


    # turn on tracing for the agent
    os.environ["LANGCHAIN_TRACING"] = "true"
    serp_api_key = os.getenv("SERPAPI_API_KEY")
    # Set up the tools for the agent
    #search = SerpAPIWrapper()
    tools = [
        # Tool(
        #     name="search",
        #     func=search.run,
        #     description="useful for when you need to answer questions about current events. You should ask targeted questions",
        # ),
        GoogleCalendarCreateEventTool(),
        GoogleCalendarViewEventsTool(),
        GoogleCalendarUpdateEventTool(),
        GoogleCalendarDeleteEventTool(),
        CalendarDataAnalyzerTool(return_direct = True),
        ViewProjectsTool(),
        CreateProjectTool(),
        CreateTaskTool(),
        CloseTaskTool(),
    ]

    def __init__(
        self,
        ai_name: str,
        llm_model: str = "gpt-4",
        temperature: float = 0.0,
        memory: VectorStoreRetriever = None,
        additional_tools: List[BaseTool] = None,
        callback_manager: Optional[BaseCallbackManager] = None,
        feedback_tool: Optional[HumanInputRun] = None,
    ):
        self.ai_name = ai_name
        self.memory = BespokeBotAgent.vectorstore if memory is None else memory
        self.full_message_history: List[BaseMessage] = []
        self.next_action_count = 0
        self.additional_tools = additional_tools
        self.feedback_tool = feedback_tool
        self.agent = None
        self.prompt = None
        self.llm_model = llm_model
        self.temperature = temperature
        self.llm_chain = None
        self.llm = None
        self.executor = None
        self.prefix = None
        self.suffix = None

    # def estimate_tokens(self, message: str) -> int:
    #     """Estimate the number of tokens required to generate a response."""
    #     token_usage = ""
    #     with get_openai_callback() as callback:
    #         response self.llm()
        
    #     return self.agent.estimate_tokens(message)
    
    def initialize_agent(
        self, prefix: str, suffix: str, input_variables: List[str] = None
    ) -> AgentExecutor:
        """Initialize the agent with the tools and prompt."""
        if self.additional_tools:
            self.tools.extend(self.additional_tools)

        self.llm = ChatOpenAI(temperature=self.temperature, model_name=self.llm_model)

        # self.prompt = StructuredChatAgent.create_prompt(
        #     tools=self.tools,
        #     prefix=prefix,
        #     suffix=suffix,
        #     input_variables=input_variables,
        # )
        # print("This was generated using the ZeroShotAgent.create_prompt method:")
        # print(self.prompt)
        # print("++++++++++++++++++++++++++++++++++++++++++++++++++")

        # self.llm_chain = LLMChain(
        #     llm=ChatOpenAI(temperature=self.temperature, model_name=self.llm_model),
        #     prompt=self.prompt,
        # )
        calendar_format_instructions = CalendarAnalyzerOutputParserFactory.create_output_parser()
        
        self.agent = StructuredChatAgent.from_llm_and_tools(
            llm=self.llm,
            tools=self.tools,
            prefix=prefix,
            suffix=suffix,
            input_variables=input_variables
        )

        self.agent.llm_chain.verbose = True

        self.executor = AgentExecutor.from_agent_and_tools(agent=self.agent, tools=self.tools)

    def run_agent(self, user_goal: str) -> str:
        """Run the agent with a user goal."""
        if self.executor is None:
            self.initialize_agent(prefix=self.prefix, suffix=self.suffix)
        
        return self.executor.run(user_goal)
