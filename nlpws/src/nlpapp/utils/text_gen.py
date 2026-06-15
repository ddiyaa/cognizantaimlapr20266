#read the hr policy txt file and summarize using encoder decoder model

import os

from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(__file__),'..', '.env')

load_dotenv(env_path)

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

#read the file

def read_file(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    return text

if __name__ == "__main__":
    file_path = os.getenv('file_path')
    text = read_file(file_path)
    print(text)