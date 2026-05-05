import statistics
import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis
from distapp.configurations.config import Config
config=Config()
def calculate_statistics():
    df=pd.read_csv(config.csv_path)
    #mean of the scores
    mean_score=statistics.mean(df["Score"])
    #median of the scores
    median_score=statistics.median(df["Score"])
    #mode of the scores
    mode_score=statistics.mode(df["Score"])
    #standard deviation of the scores
    std_dev=statistics.stdev(df["Score"])
    #variance of the scores
    variance_score=statistics.variance(df["Score"])
    #skewness of the scores
    skewness_score=skew(df["Score"])
    #skewness_score=pd.Series(df["Score"]).skew()

    #kurtosis of the scores
    kurtosis_score=kurtosis(df["Score"])
    #kurtosis_score=pd.Series(df["Score"]).kurtosis()
    return mean_score, median_score, mode_score, std_dev, variance_score, skewness_score, kurtosis_score

if __name__ == "__main__":
    mean, median, mode, std_dev, variance, skewness, kurtosis = calculate_statistics()
    print(f"Mean: {mean}")
    #plotting the distribution of scores
    
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Standard Deviation: {std_dev}")
    print(f"Variance: {variance}")
    print(f"Skewness: {skewness}")
    print(f"Kurtosis: {kurtosis}")

    import matplotlib.pyplot as plt
    df=pd.read_csv(config.csv_path)
    plt.figure(figsize=(10,6))
    plt.plot(df["Score"], marker='o')
    plt.axhline(mean, color='r', linestyle='--', label=f'Mean: {mean:.2f}')
    plt.legend()
    plt.axhline(median, color='g', linestyle='--', label=f'Median: {median:.2f}')
    plt.legend()
    plt.axhline(mode, color='b', linestyle='--', label=f'Mode: {mode:.2f}')
    plt.legend()    
    
    plt.title("Distribution of Trainees Scores")    
    plt.xlabel("Trainee Index")
    plt.ylabel("Score")
    plt.grid()
    plt.show()