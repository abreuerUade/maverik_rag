from langchain_core.messages import HumanMessage
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from ..core.prompt import prompt_template
from .tools import tools
from ..utils.helpers import format_chat_history
from langchain.agents import AgentExecutor
from .llm import llm
from langchain_core.utils.function_calling import convert_to_openai_function


llm_with_tools = llm.bind(
    functions=[convert_to_openai_function(t) for t in tools])


def create_agent_executor(user_profile_message):
    agent = (
        {
            "user_profile": lambda x: [HumanMessage(content=user_profile_message)],
            "input": lambda x: x["input"],
            "chat_history": lambda x: format_chat_history(x["chat_history"]),
            "agent_scratchpad": lambda x: format_to_openai_function_messages(
                x["intermediate_steps"]
            ),
        }
        | prompt_template
        | llm_with_tools
        | OpenAIFunctionsAgentOutputParser()
    )

    agent_executor = AgentExecutor(agent=agent, tools=tools)
    return agent_executor
