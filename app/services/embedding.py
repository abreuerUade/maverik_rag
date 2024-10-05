from langchain_huggingface import HuggingFaceEmbeddings

# Definir embeddings
emb_model = "BAAI/bge-reranker-v2-m3"
embeddings = HuggingFaceEmbeddings(model_name=emb_model)
