from langchain_google_community import GoogleSearchAPIWrapper
from langchain.tools.retriever import create_retriever_tool
from langchain_core.tools import Tool
from ..core.config import settings
from .retriever import retriever
from .llm import llm
import os
import requests
import json

fmp_api_key = settings.FMP_API_KEY


def call_stock_price_api(query: str) -> str:
    """
    Llama a la API de Financial Modeling Prep para obtener información bursátil de un símbolo de empresa determinado.

    Args:
        symbol (str): El símbolo de la empresa (por ejemplo, AAPL para Apple).

    Devuelve:
        str: La respuesta de la API en forma de cadena, o un mensaje de error si la llamada falla.
    """

    # Prompts para que el LLM devuelva el símbolo de la empresa
    prompt = (
        f"Identifica el símbolo de la empresa en la siguiente consulta: '{
            query}'. "
        "Devuelve solo el símbolo de la empresa, sin ningún otro texto."
    )

    # Llama al LLM
    symbol = llm.invoke(("human", prompt))

    url = f"https://financialmodelingprep.com/api/v3/quote/{
        symbol.content}?apikey={fmp_api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        json_rp = response.json()

        return json.dumps(json_rp[0])  # Return the response in JSON format
    except requests.exceptions.HTTPError as err:
        return f"HTTP error occurred: {err}"
    except Exception as err:
        return f"An error occurred: {err}"


def call_income_statement_api(query: str) -> str:
    """
    Llama a la API de Financial Modeling Prep para obtener información de estados contables de una empresa.

    Args:
        symbol (str): El símbolo de la empresa (por ejemplo, AAPL para Apple).

    Devuelve:
        str: La respuesta de la API en forma de cadena, o un mensaje de error si la llamada falla.
    """

    # Prompts para que el LLM devuelva el símbolo de la empresa
    prompt = (
        f"Identifica el símbolo de la empresa en la siguiente consulta: '{
            query}'. "
        "Devuelve solo el símbolo de la empresa, sin ningún otro texto."
    )

    # Llama al LLM
    symbol = llm.invoke(("human", prompt))

    url = f"https://financialmodelingprep.com/api/v3/income-statement/{
        symbol.content}?period=annual&apikey={fmp_api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        json_rp = response.json()

        return json.dumps(json_rp[0])  # Return the response in JSON format
    except requests.exceptions.HTTPError as err:
        return f"HTTP error occurred: {err}"
    except Exception as err:
        return f"An error occurred: {err}"


def key_metrics_api(query: str) -> str:
    """
    Obtenga las principales métricas financieras de una empresa, incluidos los ingresos, 
    los beneficios netos y la relación precio-beneficios (relación PER). Evalúe los resultados 
    financieros de una empresa y compárelos con los de sus competidores.
    Args:
        symbol (str): El símbolo de la empresa (por ejemplo, AAPL para Apple).

    Devuelve:
        str: La respuesta de la API en forma de cadena, o un mensaje de error si la llamada falla.
    """

    # Prompts para que el LLM devuelva el símbolo de la empresa
    prompt = (
        f"Identifica el símbolo de la empresa en la siguiente consulta: '{
            query}'. "
        "Devuelve solo el símbolo de la empresa, sin ningún otro texto."
    )

    # Llama al LLM
    symbol = llm.invoke(("human", prompt))

    url = f"https://financialmodelingprep.com/api/v3/key-metrics/{
        symbol.content}?period=annual&apikey={fmp_api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        json_rp = response.json()

        return json.dumps(json_rp[0])  # Return the response in JSON format
    except requests.exceptions.HTTPError as err:
        return f"HTTP error occurred: {err}"
    except Exception as err:
        return f"An error occurred: {err}"

# Crear las Tools


os.environ["GOOGLE_CSE_ID"] = settings.GOOGLE_CSE_ID
os.environ["GOOGLE_API_KEY"] = settings.GOOGLE_API_KEY
os.environ["SERPAPI_API_KEY"] = settings.SERPAPI_API_KEY

g_search = GoogleSearchAPIWrapper()

google_tool = Tool(
    name="google_search",
    description="Busca cotizaciones de acciones e informacion financiera",
    func=g_search.run,
)

retriever_tool = create_retriever_tool(
    retriever,
    "pdf_retriever",
    "Util para obtener información financiera. Consultar los documentos en español e ingles.",
)


stock_price_tool = Tool(
    name="FinancialModelingTool_Stock_Prices",
    func=call_stock_price_api,
    description=(
        "Trae informacion de las acciones de empresas que cotizan en bolsa."

    )
)

income_statement_tool = Tool(
    name="FinancialModelingTool_Income_Statements",
    func=call_income_statement_api,
    description=(
        "Trae informacion de los estados de resultados de estados contables de las empresas."

    )
)

key_metrics_tool = Tool(
    name="FinancialModelingTool_key_metrics",
    func=key_metrics_api,
    description=(
        "Obtiene las principales métricas financieras de una empresa, incluidos los ingresos, los beneficios netos y la relación precio-beneficios (relación PER). Evalúe los resultados financieros de una empresa y compárelos con los de sus competidores."

    )
)

tools = [retriever_tool, stock_price_tool,
         income_statement_tool, google_tool, key_metrics_tool]
