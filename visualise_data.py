import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# Load in data.
data_frame = pd.read_csv('./Coffee_Stores_Data.csv')

# Removes last two columns since they are not needed.
data_frame = data_frame.drop(['GroupID', 'MissedSales'], axis=1)

# Associate the ItemType lables with a number.
# 'Unassigned' = 0
# 'Core' = 1
# 'Seasonal' = 2
#data_frame['ItemType'] =





# For debugging
#print(type(data_frame))
#print(data_frame)
print(data_frame.head())
print()

#print(type(data_frame.ItemType))
#print(data_frame.ItemType)
#print()

#print(type(data_frame.ItemType.array))
#print(data_frame.ItemType.array)
#print()

print("data entries: %s" % len(data_frame.ItemType.array))
#print("set_length: %s" % len(set(data_frame.ItemType.array)))
#print(set(data_frame.ItemType.array))
print()

#
print('amount of unique Stores: %d' % len(data_frame['StoreID'].unique()))                  # 132
print('amount of unique Dates: %d' % len(data_frame['BusinessDate'].unique()))              # 367
print('amount of unique Items: %d' % len(data_frame['PLU'].unique()))                       # 31
print('amount of unique Descriptions: %d' % len(data_frame['Description'].unique()))        # 31
print('amount of unique Item Typess: %d' % len(data_frame['ItemType'].unique()))            # 3
print('amount of unique Category desc1: %d' % len(data_frame['CategoryLvl1Desc'].unique())) # 1
print('amount of unique Category desc1: %d' % len(data_frame['CategoryLvl2Desc'].unique())) # 2
print('amount of unique Category desc1: %d' % len(data_frame['CategoryLvl3Desc'].unique())) # 7