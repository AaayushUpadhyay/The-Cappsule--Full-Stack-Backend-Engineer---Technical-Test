import pandas as pd

# read the Master and Test sheets into pandas dataframes
master_df = pd.read_excel('Master.xlsx', sheet_name='Master')
test_df = pd.read_excel('Test.xlsx', sheet_name='Test')

# print(master_df.head(1))
# print("\n")
# print(test_df.head(1))
# print("\n")

# create Product ID column with unique identifiers for each product
def create_product_id(df):
    df['Unique ID'] = df.apply(lambda row: row['Item name'][0:3].upper() + str(row['Manufacturer'])[0:3].upper() + str(row.name), axis=1)
    return df

master_df = create_product_id(master_df)
test_df = create_product_id(test_df)

# print(master_df.head(1))
# print("\n")
# print(test_df.head(1))
# print("\n")
master_df = master_df.applymap(lambda s: s.lower() if isinstance(s, str) else s)
test_df = test_df.applymap(lambda s: s.lower() if isinstance(s, str) else s)

# create a dictionary mapping Item name to Product ID
id_dict = dict(zip(master_df['Item name'], master_df['Product ID']))
# print(id_dict)


test_df['Product ID'] = test_df['Item name'].map(id_dict)


print(test_df)

