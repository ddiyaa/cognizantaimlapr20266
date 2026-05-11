#create matrix transpose of census data census.csv and
# make male and female row and stat as column and vice versa
import pandas as pd
from linearalgebra.configurations.conf import Config

def census_mat_transpose():
    #read census data from census_path
    census_data = pd.read_csv(Config.census_path)
    #create subset of census data with state, population
    df= census_data[['state','male_population','female_population']]
    print(df.head())

if __name__ == "__main__":
    census_mat_transpose()