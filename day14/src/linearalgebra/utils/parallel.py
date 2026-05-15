#create tax calculator function for products in products.csv using parallel processing
from multiprocessing import Pool
import time

import pandas as pd
from linearalgebra.configurations.conf import Config

def sequential_tax_calculator(product_path):
    #read products.csv
    products = pd.read_csv(product_path)
    start_time = time.time()
    #convert cost column to array
    cost_array = products['cost'].values
    tax_array = []
    for i in range(len(cost_array)):
        tax = cost_array[i] * 0.1
        tax_array.append(tax)
    end_time = time.time()
    print(f"Time taken for sequential tax calculation: {end_time - start_time} seconds")
    return tax_array
def calculate_tax(cost):
    return cost * 0.1
def parallel_tax_calculator(product_path):
    products = pd.read_csv(product_path)

    cost_array = products["cost"].values
    start_time = time.time()
    with Pool() as p:
        tax_array = p.map(calculate_tax, cost_array)
    end_time = time.time()
    print(f"Time taken for parallel tax calculation: {end_time - start_time} seconds")
    return tax_array

    


if __name__ == "__main__":
    #read products.csv
    product_path=Config.product_path
    tax = sequential_tax_calculator(product_path)
    tax=print(tax)
    parallel_tax_calculator(product_path)
 