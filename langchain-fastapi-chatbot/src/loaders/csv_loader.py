import pandas as pd

class CSVLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        try:
            data = pd.read_csv(self.file_path)
            return data
        except Exception as e:
            print(f"Error loading CSV file: {e}")
            return None