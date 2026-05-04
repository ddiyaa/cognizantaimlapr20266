#create random variable
import random
import pandas as pd

def create_discrete_random_variable():
   #create random variable
   df = pd.read_csv("src/distapp/resources/trainees_score.csv")
   #create discrete random variable
   random_variable = df['Score'].sample(n=5).tolist()
   return random_variable
def create_continuous_random_variable():
   #create continuous random variable
   df = pd.read_csv("src/distapp/resources/trainees_score.csv")
   min_score = df['Score'].min()
   max_score = df['Score'].max()
   random_variable = [_ for _ in range(min_score, max_score+1, 5)]
   return random_variable

if __name__ == "__main__":
   random_variable = create_discrete_random_variable()
   print(random_variable)
   random_variable = create_continuous_random_variable()
   print(random_variable)