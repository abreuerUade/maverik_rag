from langchain_mongodb.vectorstores import MongoDBAtlasVectorSearch
from app.services.database import MONGODB_COLLECTION
from app.services.embedding import embeddings
from app.core.config import settings
from langchain.chains.query_constructor.base import AttributeInfo
from langchain.retrievers import SelfQueryRetriever
from app.services.llm import llm

# Configuración del vector store
vector_store = MongoDBAtlasVectorSearch(
    collection=MONGODB_COLLECTION,
    embedding=embeddings,
    index_name=settings.ATLAS_VECTOR_SEARCH_INDEX_NAME,
    relevance_score_fn="cosine",
)

# Información de los campos de metadatos
metadata_field_info = [
    AttributeInfo(
        name="idioma",
        description="El idioma en que están escritos los documentos. 'en' es para inglés y 'es' es para español",
        type="string",
    ),
    AttributeInfo(
        name="description",
        description="Una breve descripción sobre el tipo de información en el documento",
        type="string",
    )
]

# Contenido de los documentos
document_contents = "Libros financieros, libros y entrevistas de Warren Buffett e información sobre finanzas personales"

# Configuración del retriever
retriever = SelfQueryRetriever.from_llm(
    llm=llm,
    vectorstore=vector_store,
    document_contents=document_contents,
    metadata_field_info=metadata_field_info,
    verbose=False,
    enable_limit=True
)
