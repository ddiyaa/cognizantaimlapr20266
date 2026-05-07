#calculate effect using cohen's d for medicine effectiveness using medicine_effect.csv
import pandas as pd
from scipy import stats
from distapp.configurations.config import Config

def calculate_effectiveness():
    config = Config()
    df = pd.read_csv(config.effectiveness_path)
    group1 = df[df['medicine_name'] == 'Metformin']['recovery_speed']
    group2 = df[df['medicine_name'] == 'Glimepiride']['recovery_speed']
    print(group1.to_list())
    print(group2.to_list())

if __name__ == "__main__":
    calculate_effectiveness()