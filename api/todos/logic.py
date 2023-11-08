
from .AlphaVantage_API import df 
import pandas as pd
filter  = ["CAPM"]
stock = []


import numpy as np  # Import NumPy for array operations
 

def choose(filter, number):
    #maybe need to check if filter has empty spots 
    for i in range(len(filter)):
        
        if filter[i] == "CAPM":
            for col in df.columns:
                new = df[col]
                new = pd.to_numeric(new, errors='coerce')
                dfavg = new.sum() / len(new)
                
                
                stock.append(col)  # Append the column name to stock
                print(stock)

                return stock, dfavg


        elif filter[i] == "Volatility":
            x = "vol"
        elif filter[i] == "Beta":
            x = "beta"

    



