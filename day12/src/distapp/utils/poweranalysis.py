#create power analysis using medicine_effect 
import numpy as np
import pandas as pd
from distapp.configurations.config import Config
#power is assumed to be 0.8 and alpha is assumed to be 0.05
def power_analysis(medicine_effect, alpha, power=0.8):
    # Calculate the required sample size using the effect size and power
    from statsmodels.stats.power import TTestIndPower
    analysis = TTestIndPower()
    effect_size = calculate_medicine_effect(medicine_effect, 0)  # Assuming control effect is 0
    sample_size = analysis.solve_power(effect_size=effect_size, alpha=alpha, power=power, alternative='two-sided')
    return sample_size

def calculate_medicine_effect(medicine_effect, control_effect):
    # Calculate the effect size (Cohen's d)
    effect_size = (medicine_effect - control_effect) / np.sqrt((medicine_effect + control_effect) / 2)
    return effect_size


if __name__ == "__main__":
    config = Config()
    df=pd.read_csv(config.effectiveness_path)
    medicine_effect_count = (df['medicine_name'] == 'Metformin').sum()
    print(medicine_effect_count)
    medicine_effect_mean= medicine_effect_count/len(df)
    control_effect_count = (df['medicine_name']=='Glimepiride').sum()
    print(control_effect_count)
    control_effect_mean= control_effect_count/len(df)
    effect_size = calculate_medicine_effect(medicine_effect_mean, control_effect_mean) 
    #objective is increas medicine effect mean by 20%
    new_medicine_effect_mean = medicine_effect_mean * 1.2
    alpha = new_medicine_effect_mean - medicine_effect_mean

    print(f"Medicine Effect Mean: {medicine_effect_mean}")
    print(f"Control Effect Mean: {control_effect_mean}")
    print(f"Effect Size (Cohen's d): {effect_size}") 
    print(f"New Medicine Effect Mean (20% increase): {new_medicine_effect_mean}")
    print(f"Alpha (Difference between new and old medicine effect mean): {alpha}")

    #invoke power analysis function
    required_sample_size = power_analysis(medicine_effect_mean, alpha)
    print(f"Required Sample Size for 80% Power and Alpha of {alpha}: {required_sample_size}")

    