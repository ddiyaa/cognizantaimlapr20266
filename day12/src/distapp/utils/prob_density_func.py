#create probability density function for delivery time csv file
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
from distapp.configurations.config import Config

def create_prob_density_func():
    config = Config()
    delivery_time_df = pd.read_csv(config.delivery_time_csv_path)
    #create probability density function for delivery time
    delivery_time = delivery_time_df['delivery_time_seconds'].values
    #fit a normal distribution to the data
    mu, std = norm.fit(delivery_time)
    #plot the histogram of the data and the probability density function    
    plt.hist(delivery_time, bins=25, density=True, alpha=0.6, color='g')
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    plt.title("Fit results: mu = %.2f,  std = %.2f" % (mu, std))
    plt.show()

if __name__ == "__main__":
    create_prob_density_func()  