
from .AlphaVantage_API import df 
import pandas as pd
filter  = ["CAPM"]
stock = []


import numpy as np  # Import NumPy for array operations

def calculateCAPM(stockValue, minvalue):
    minValue = np.array(minvalue)  # Convert minvalue to a NumPy array
    stockValue = np.array(stockValue)  # Convert stockValue to a NumPy array
    
    if np.all(stockValue > minValue):  # Perform element-wise comparison
        return False
    else:
        return True
 

def choose(filter, number):
    #maybe need to check if filter has empty spots 
    for i in range(len(filter)):
        
        if filter[i] == "CAPM":
            for col in df.columns:
                new = df[col]
                new = pd.to_numeric(new, errors='coerce')
                dfavg = new.sum() / len(new)
                result = calculateCAPM(dfavg, number)  # Calculate CAPM and store the result
                if result:  # Check the result (True or False)
                    stock.append(col)  # Append the column name to stock
                    print(stock)


        elif filter[i] == "Volatility":
            x = "vol"
        elif filter[i] == "Beta":
            x = "beta"

    



