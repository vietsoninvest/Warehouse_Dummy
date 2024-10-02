#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd

# Ensure you have the Excel file in the same directory as your script or provide the full path to the file.
excel_file = 'stock.xlsx'

# Load the Excel file
df = pd.read_excel(excel_file)

# Function to search by rack
def search_rack(section, column, level):
    # Convert the Section, Column, and Level columns to the same data type as the input for proper comparison
    df['Section'] = df['Section'].astype(str)
    df['Column'] = df['Column'].astype(str)
    df['Level'] = df['Level'].astype(str)

    # Filter the dataframe based on the rack coordinates
    # Make sure to convert the input to string because DataFrame is in string format after the conversion above
    results = df[(df['Section'] == str(section)) & (df['Column'] == str(column)) & (df['Level'] == str(level))]
    
    # Instead of returning "Empty", return an empty DataFrame with the same columns
    if results.empty:
        return pd.DataFrame(columns=df.columns)
    
    return results

# Example usage:
# This will print the dataframe with all items in Section 1, Column 'A', Level 1
print(search_rack('1', 'A', '1'))
print(df.head())


# In[17]:


import pandas as pd

def search_item(product_code=None, product_name=None):
    # Load the Excel file
    df = pd.read_excel(excel_file)
    
    # Ensure 'Product_code' is treated as a string for consistent comparison
    df['Product_code'] = df['Product_code'].astype(str).str.strip()

    # Initialize an empty DataFrame with the desired columns for consistency
    empty_df = pd.DataFrame(columns=['Quantity', 'Section', 'Column', 'Level'])

    # Perform the search based on product_code or product_name
    if product_code:
        product_code_str = str(product_code).strip()  # Convert input to string and strip whitespaces
        item_location = df[df['Product_code'] == product_code_str]
    elif product_name:
        # Use .str.contains for partial matches; case=False makes it case-insensitive
        item_location = df[df['Product_name'].str.contains(product_name, case=False, na=False)]
    else:
        # If neither product_code nor product_name is provided, return the empty_df
        return empty_df

    # Return the search result if found; otherwise, return the empty_df with the specified columns
    return item_location[['Product_code','Product_name','Quantity', 'Section', 'Column', 'Level']] if not item_location.empty else empty_df


# In[18]:


import pandas as pd

def add_item(product_code, quantity, section, column, level):
    df = pd.read_excel(excel_file)
    
    # Convert product_code, section, and level to integers
    product_code = int(product_code)
    section = int(section)
    level = int(level)
    
    # Find if the product already exists at the specified location
    exists = df[(df['Product_code'] == product_code) &
                (df['Section'] == section) &
                (df['Column'] == column) &
                (df['Level'] == level)]
    
    if not exists.empty:
        # If exists, update the quantity
        df.loc[exists.index, 'Quantity'] += quantity
    else:
        # If not exists, add a new row
        new_row = {'Product_code': product_code, 'Quantity': quantity,
                   'Section': section, 'Column': column, 'Level': level}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    
    df.to_excel(excel_file, index=False)

def remove_item(product_code, quantity, section, column, level):
    df = pd.read_excel(excel_file)
    
    # Convert product_code, section, and level to integers
    product_code = int(product_code)
    section = int(section)
    level = int(level)
    
    # Find the item's index
    item_index = df[(df['Product_code'] == product_code) &
                    (df['Section'] == section) &
                    (df['Column'] == column) &
                    (df['Level'] == level)].index
    
    if not item_index.empty:
        # Subtract the quantity
        df.loc[item_index, 'Quantity'] -= quantity
        # Optionally, remove the row if quantity <= 0
        df = df[df['Quantity'] > 0]
    
    df.to_excel(excel_file, index=False)


# In[ ]:




