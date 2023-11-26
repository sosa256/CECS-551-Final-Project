import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# Load in data.
orginal_df = pd.read_csv('./Coffee_Stores_Data.csv')

# Removes last two columns since they are not needed.
# CategoryLvl1Desc - there is only type of label in this column ('Food')
# GroupID - Instructions say it's not relevent
# MissedSales - same as above
orginal_df = orginal_df.drop(['CategoryLvl1Desc', 'GroupID', 'MissedSales'], axis=1)

# Create a new data frame only containing entries that have a specific PLU.
# code from: https://stackoverflow.com/a/38186202
PLU = 3000227
plu_specific_df = orginal_df[(orginal_df == PLU).any(axis=1)]
#print(plu_specific_df)

# Drop columns that dont have any info ( aka have one unique value).
for label in plu_specific_df.columns.tolist():
    if len(plu_specific_df[label].unique()) == 1:
        plu_specific_df = plu_specific_df.drop([label], axis=1)
        print('Dropped: %s column' % label)
#print(plu_specific_df)


# Aggregate entries with same dates.
plu_specific_df = plu_specific_df.drop(['StoreID'], axis=1)
# code: https://stackoverflow.com/a/46827686
aggregation_functions = { 'BusinessDate': 'first', 'ReceivedQuantity': 'sum', 'SoldQuantity': 'sum', 'EndQuantity': 'sum', 'LatestOrder': 'sum', 'StockedOut': 'sum'}
aggregate_df = plu_specific_df.groupby(plu_specific_df['BusinessDate']).aggregate(aggregation_functions)

# TODO
# Plot date by the following on one graph.
#   ReceivedQuantity
#   SoldQuantity
#   EndQuantity
#   LatestOrder
#   StockedOut

# # Plot date by SoldQuantity.
plt.plot(aggregate_df["BusinessDate"], aggregate_df["SoldQuantity"])
plt.show()









# For debugging
print('\n\nInfo: original dataframe')
print(orginal_df)
print('amount of unique Stores: %d' % len(orginal_df['StoreID'].unique()))                  # 132
print('amount of unique Dates: %d' % len(orginal_df['BusinessDate'].unique()))              # 367
print('amount of unique Items: %d' % len(orginal_df['PLU'].unique()))                       # 31
print('amount of unique Descriptions: %d' % len(orginal_df['Description'].unique()))        # 31
print('amount of unique Item Types: %d' % len(orginal_df['ItemType'].unique()))            # 3
print('amount of unique Category desc2: %d' % len(orginal_df['CategoryLvl2Desc'].unique())) # 2
print('amount of unique Category desc3: %d' % len(orginal_df['CategoryLvl3Desc'].unique())) # 7
print('\n')

# Associate the ItemType lables with a number.
# 'Unassigned' = 0
# 'Core' = 1
# 'Seasonal' = 2
#orginal_df['ItemType'] =
