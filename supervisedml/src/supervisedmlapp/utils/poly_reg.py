#create polynomial regression model for the population dataset
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from supervisedmlapp.configurations.conf import POPULATION_FILE_PATH
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
def polynomial_regression_model():
    # Load the dataset
    data = pd.read_csv(POPULATION_FILE_PATH)
    
    # Define features and target variable
    X = data[['Year']] # Features
    y = data['Population']  # Target variable

    #normalize the features
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    y_scaled = scaler.fit_transform(y.values.reshape(-1, 1))
    
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.3, random_state=42)
     
    # Create a polynomial regression model
    # we will use degree 2 for the polynomial regression
   
    polynomial_features = PolynomialFeatures(degree=5)
    X_train_poly = polynomial_features.fit_transform(X_train)
    X_test_poly = polynomial_features.transform(X_test)
    model = LinearRegression()
    # Fit the model to the training data
    # we will fit the model to the polynomial features
    # this will allow us to capture the non-linear relationship between the features and the target variable
    model.fit(X_train_poly, y_train)
    # Make predictions on the test set
    y_pred = model.predict(X_test_poly)
    # Evaluate the model
   
    mse = mean_squared_error(y_test, y_pred)**0.5
    r2 = r2_score(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')
    print(f'R^2 Score: {r2}')

    #predict the population for the year 2050
    year_2050 = [[2050]]
    year_2050_scaled = scaler.transform(year_2050)  
    year_2050_poly = polynomial_features.transform(year_2050_scaled)
    population_2050_scaled = model.predict(year_2050_poly)
    population_2050 = scaler.inverse_transform(population_2050_scaled)
    print(f'Predicted population for the year 2050: {population_2050[0][0]}')
    #find the difference between actual and predicted population for the year 2020
    year_2020 = [[2020]]
    year_2020_scaled = scaler.transform(year_2020)
    year_2020_poly = polynomial_features.transform(year_2020_scaled)
    population_2020_scaled = model.predict(year_2020_poly)
    population_2020 = scaler.inverse_transform(population_2020_scaled)
    actual_population_2020 = data[data['Year'] == 2020]['Population'].values[0]
    difference = actual_population_2020 - population_2020[0][0]
    print(f'Actual population for the year 2020: {actual_population_2020}')
    print(f'Predicted population for the year 2020: {population_2020[0][0]}')
    print(f'Difference between actual and predicted population for the year 2020: {difference}')


if __name__ == "__main__":
    polynomial_regression_model()
