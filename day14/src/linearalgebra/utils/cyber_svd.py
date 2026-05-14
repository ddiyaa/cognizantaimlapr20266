#create svd for cyber security text file
from email import policy
from os import access

from cv2 import data
import pandas as pd
from linearalgebra.configurations.conf import Config
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
def calculate_svd(file_path):
    #open text file
    with(open(file_path, 'r',encoding='utf-8')) as f:
        text=f.read()
    #print(text)
    #split text into smaller documents
    documents=[p.strip() for p in text.split('\n') if p.strip()]
    print(documents)
    #length of total policies
    print(f"Total policies: {len(documents)}") 
    # apply TF and ITF vectorization to the documents
    vectorizer = TfidfVectorizer(
        stop_words="english"    
    )
    X = vectorizer.fit_transform(documents)
    # get all words/features
    feature_names = vectorizer.get_feature_names_out()

    for i, row in enumerate(X.toarray()):

        print("\n" + "="*60)
        print(f"Document {i+1}")
        print(f"Text: {documents[i]}")
        print("-"*60)

        # print only non-zero tfidf scores
        for j, value in enumerate(row):

            if value > 0:
                print(f"{feature_names[j]:20} : {value:.3f}")
  

    #print(f"TF-IDF matrix  {X}")
    #print(f"TF-IDF matrix shape: {X.shape}")
    # apply SVD to the TF-IDF matrix
    svd = TruncatedSVD(n_components=2)
    embeddings = svd.fit_transform(X)
    print(f"SVD matrix: {embeddings}")
    print(f"SVD matrix shape: {embeddings.shape}")


    #component 1
    #security
    #policy
    #protection
    #systems
    #access
    #data
    #component 2
    #users
    #passwords
    #access control
    #device rules
    for i, (doc, vec) in enumerate(zip(documents, embeddings)):
        print(f"\nDocument {i+1}")
        print("Text:", doc)
        print("Embedding:", vec)

   




if __name__ == "__main__":
    cyper_path = Config.cyber_path
    calculate_svd(cyper_path)