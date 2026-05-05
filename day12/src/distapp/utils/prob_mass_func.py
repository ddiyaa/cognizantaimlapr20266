#create probability mass function for discrete distribution from api_requests.csv
from distapp.configurations.config import Config
import pandas as pd
import matplotlib.pyplot as plt
def create_prob_mass_func():
    #read api_requests.csv
    df = pd.read_csv(Config().api_requests_csv_path)
    #pmf = frequency of each endpoint / total number of requests
    pmf = df['api_requests'].value_counts() / len(df)
    return pmf.to_dict()

def draw_pmf(pmf):    
    plt.bar(pmf.keys(), pmf.values(), color='violet')
    plt.xlabel('API Requests')
    plt.ylabel('Probability')
    plt.title('Probability Mass Function of API Requests')
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    pmf = create_prob_mass_func()
    #sort pmf by key
    sorted_pmf = dict(sorted(pmf.items()))      
    print(sorted_pmf)
    draw_pmf(sorted_pmf)