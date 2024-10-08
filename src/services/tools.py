from langchain_community.tools import TavilySearchResults
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from langchain.tools.retriever import create_retriever_tool
from .retriever import retriever
from ..core.config import settings


# Configuración de la API de Tavily
tavilySearchAPIWrapper = TavilySearchAPIWrapper(
    tavily_api_key=settings.TAVILY_API_KEY)
search = TavilySearchResults(
    api_wrapper=tavilySearchAPIWrapper,
    search_depth="advanced",
    include_answer=True
)

# Creación de la herramienta de retriever
retriever_tool = create_retriever_tool(
    retriever,
    "pdf_retriever",
    "Util para obtener información financiera. Consultar los documentos en español e inglés.",
)

# opoen_ai_retriever = convert_to_openai_function(retriever_tool)
# open_ai_search = convert_to_openai_function(search)

# Lista de herramientas
# tools = [open_ai_search, opoen_ai_retriever]
tools = [search, retriever_tool]
