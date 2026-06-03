#create linear regression model for house price prediction
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression   
from sklearn.metrics import mean_squared_error, r2_score
from src.supervisedmlapp.configurations.conf import HOUSE_FILE_PATH

def linear_regression_model():
    # Load the dataset
    data = pd.read_csv(HOUSE_FILE_PATH)
    
    # Define features and target variable
    X = data.drop('Price', axis=1)  # Features
    y = data['Price']  # Target variable
    
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create a linear regression model
    model = LinearRegression()
    
    # Fit the model to the training data
    model.fit(X_train, y_train)
    
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f'Mean Squared Error: {mse}')
    print(f'R^2 Score: {r2}')
    
    return model