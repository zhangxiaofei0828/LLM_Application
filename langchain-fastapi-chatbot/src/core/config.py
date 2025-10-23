import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    CSV_FILE_PATH = os.getenv("CSV_FILE_PATH", "path/to/your/private/documents.csv")
    PORT = int(os.getenv("PORT", 8000))
    HOST = os.getenv("HOST", "0.0.0.0")