import os
from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

HOUSE_FILE_PATH = os.getenv('house_file_path')
POPULATION_FILE_PATH = os.getenv('population_file_path')
BANK_FILE_PATH = os.getenv('bank_files_path')
LOAN_FILE_PATH = os.getenv('loan_files_path')