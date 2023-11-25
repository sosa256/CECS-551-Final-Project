import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# Load in data.
data_frame = pd.read_csv('./Coffee_Stores_Data.csv')

# Removes last two columns since they are not needed.
data_frame = data_frame.drop(['GroupID', 'MissedSales'], axis=1)



# For debugging
print(type(data_frame))
print(data_frame.head())