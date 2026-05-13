#create svd for cyber security text file
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
    #print(f"TF-IDF matrix  {X}")
    #print(f"TF-IDF matrix shape: {X.shape}")
    # apply SVD to the TF-IDF matrix
    svd = TruncatedSVD(n_components=2)
    embeddings = svd.fit_transform(X)
    print(f"SVD matrix: {embeddings}")
    print(f"SVD matrix shape: {embeddings.shape}")

   




if __name__ == "__main__":
    cyper_path = Config.cyber_path
    calculate_svd(cyper_path)