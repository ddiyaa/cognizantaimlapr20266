#create cumulative distribution function for sip dataset
import pandas as pd
import matplotlib.pyplot as plt
from distapp.configurations.config import Config

def create_cdf():
    config = Config()
    sip_df = pd.read_csv(config.sip_path)
    sip_df = sip_df.sort_values(by='portfolio_value', ascending=True).reset_index(drop=True)
    sip_df['CDF'] = (sip_df.index + 1) / len(sip_df)
    plt.plot(sip_df['portfolio_value'], sip_df['CDF'])
    plt.xlabel('Portfolio Value')
    plt.ylabel('Cumulative Distribution Function')
    plt.title('CDF of SIP')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    create_cdf()