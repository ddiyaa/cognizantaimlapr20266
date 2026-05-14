#create standard normalization function for angola population data
import pandas as pd
from linearalgebra.configurations.conf import Config
from matplotlib import pyplot as plt
def standard_normalization(file_path):
    df = pd.read_excel(file_path)
    #select year column and apply standard normalization
    year = df.iloc[:, 0]  # Assuming the year column is the first column
    mean_year = year.mean()
    std_year = year.std()
    normalized_year = (year - mean_year) / std_year
    df['Year'] = normalized_year
    #select population column and apply standard normalization
    population = df.iloc[:, 1]  # Assuming the population column is the second column
    mean_population = population.mean()
    std_population = population.std()
    normalized_population = (population - mean_population) / std_population
    df['Population'] = normalized_population
    df.drop(df.columns[0:2], axis=1, inplace=True)  # Drop any additional columns
    #draw the plot of the normalized data
    plt.figure(figsize=(10, 5))
    plt.plot(df['Year'], df['Population'], marker='o')
    plt.title('Standard Normalized Population Data')
    plt.xlabel('Normalized Year')
    plt.ylabel('Normalized Population')
    plt.grid()
    plt.show()
    normalized_file_path = file_path.replace('.xlsx', '_std_normalized.xlsx')
    df.to_excel(normalized_file_path, index=False)
    print(f"Normalized data saved to {normalized_file_path}")


if __name__ == "__main__":
    file_path = Config.population_path
    standard_normalization(file_path)