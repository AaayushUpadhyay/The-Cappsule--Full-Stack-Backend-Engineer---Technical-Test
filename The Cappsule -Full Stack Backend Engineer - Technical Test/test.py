import pandas as pd
from fuzzywuzzy import process

# read the first sheet into a DataFrame
df1 = pd.read_excel('master.xlsx')

# read the second sheet into a DataFrame
df2 = pd.read_excel('test.xlsx')

# create a dictionary mapping Item name to Product ID
id_dict = {}
for item_name in df2['Item name']:
    match = process.extractOne(item_name, df1['Item name'])
    if match[1] >= 80:  # set a similarity threshold of 80%
        id_dict[item_name] = df1.loc[df1['Item name'] == match[0], 'Product ID'].iloc[0]

# add a new column to df2 with the matching Product ID for each Item name
df2['Product ID'] = df2['Item name'].map(id_dict)
df2 = df2.rename(columns={'Product ID': 'Product ID_Master'})

# write the updated DataFrame to a third sheet
with pd.ExcelWriter('Output.xlsx') as writer:
    df2.to_excel(writer, sheet_name='Sheet3', index=False)
