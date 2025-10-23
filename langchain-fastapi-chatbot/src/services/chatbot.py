from langchain import OpenAI
from langchain.chains import ConversationalChain
from langchain.memory import ConversationBufferMemory
import pandas as pd

class ChatbotService:
    def __init__(self, csv_file_path):
        self.memory = ConversationBufferMemory()
        self.llm = OpenAI()
        self.conversational_chain = ConversationalChain(
            llm=self.llm,
            memory=self.memory
        )
        self.documents = self.load_documents(csv_file_path)

    def load_documents(self, csv_file_path):
        try:
            df = pd.read_csv(csv_file_path)
            return df.to_dict(orient='records')
        except Exception as e:
            print(f"Error loading documents: {e}")
            return []

    def get_response(self, user_input):
        response = self.conversational_chain.run(user_input)
        return response

    def get_documents(self):
        return self.documents