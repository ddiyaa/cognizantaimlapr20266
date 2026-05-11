#weather change matrix and subtract it from the image
import numpy as np
import pandas as pd
from linearalgebra.configurations.conf import Config
def weather_change_mat_sub(image, weather_change_mat):
    #check if the weather change matrix is the same size as the image
    if weather_change_mat.shape != image.shape:
        raise ValueError("Weather change matrix must be the same size as the image")
    #subtract the weather change matrix from the image
    result = image - weather_change_mat
    return result.astype(np.float32)
if __name__ == "__main__":
    #test the function
    weather_path = Config.weather_path
    df=pd.read_csv(weather_path)
    #create 3x2 matrix using temperature change, humidity and pressure change
    #only take the first 3 rows of the dataframe
    df = df.head(3)
    weather_mat = df[['temperature_c', 'humidity_percent']].values
    #create matrix with temperature change
    weather_change_mat = df[['temperature_change_c']].values
    print("Weather Matrix:\n", weather_mat)
    print("Weather Change Matrix:\n", weather_change_mat)
    #create unity matrix of size 3x2
    unity_mat = np.ones((weather_mat.shape))*weather_change_mat
    print("Unity Matrix:\n", unity_mat)
    result = weather_change_mat_sub(weather_mat, unity_mat)
    print("Original Image:\n", weather_mat)
    print("Weather Change Matrix:\n", weather_change_mat)
    print("Resulting Image:\n", result)