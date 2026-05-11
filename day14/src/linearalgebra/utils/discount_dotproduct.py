#create dot product function using productwise discount dataset
import pandas as pd
from linearalgebra.configurations.conf import Config

def discount_dotproduct(df):
    #create a new column for the dot product
    df['dot_product'] = df['discount_percent'] * df['original_price']/100
    print(f"Dot product calculated and added to the dataframe.{df['dot_product'].head()}")
    return df
    


if __name__ == "__main__":
    discount_path=Config.discount_path
    print(f"Discount path: {discount_path}")
    df=pd.read_csv(discount_path)
    #print(df.head())
    result=discount_dotproduct(df)
    #total savings as scalar value
    total_savings=result['dot_product'].sum()
    print(f"Total savings from discounts: {total_savings}")
