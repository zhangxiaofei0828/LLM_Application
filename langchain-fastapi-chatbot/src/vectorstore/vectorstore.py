from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import pandas as pd

class VectorStore:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.vector_store = None

    def load_documents(self):
        df = pd.read_csv(self.csv_file_path)
        documents = df['text'].tolist()  # Assuming the CSV has a column named 'text'
        return documents

    def create_vector_store(self):
        documents = self.load_documents()
        embeddings = OpenAIEmbeddings()
        self.vector_store = Chroma.from_documents(documents, embeddings)

    def get_vector_store(self):
        if self.vector_store is None:
            self.create_vector_store()
        return self.vector_store

    def search(self, query, k=5):
        if self.vector_store is None:
            self.create_vector_store()
        return self.vector_store.similarity_search(query, k)