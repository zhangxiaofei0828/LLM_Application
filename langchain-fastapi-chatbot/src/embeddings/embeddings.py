from langchain.embeddings import OpenAIEmbeddings
import pandas as pd

class Embeddings:
    def __init__(self, model_name="text-embedding-ada-002"):
        self.embeddings_model = OpenAIEmbeddings(model_name=model_name)

    def embed_text(self, text):
        return self.embeddings_model.embed(text)

    def embed_csv(self, csv_file):
        df = pd.read_csv(csv_file)
        embeddings = df['text_column'].apply(self.embed_text)  # Replace 'text_column' with the actual column name
        return embeddings.tolist()