#!/usr/bin/env python
# coding: utf-8

# In[1]:


# UIUX.py
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from TestFunction import search_item, search_rack


# In[3]:


def search_by_product_code():
    product_code = product_code_entry.get()
    df = search_item(product_code=product_code)  # Assuming this returns a DataFrame
    update_treeview(df)

def search_by_product_name():
    product_name = product_name_entry.get()
    df = search_item(product_name=product_name)  # Adjusted to search by product name
    update_treeview(df)

def search_rack_contents():
    section = section_entry.get()
    column = column_entry.get()
    level = level_entry.get()
    result = search_rack(section, column, level)  # This should return a DataFrame or "N/A"
    
    if isinstance(result, str) and result == "N/A":
        tree.delete(*tree.get_children())  # Clear the treeview
        messagebox.showinfo("Search Result", "No items found in the specified rack.")
    else:
        update_treeview(result)      

def configure_treeview_columns(dataframe):
    # Clear the existing content in the Treeview
    tree.delete(*tree.get_children())

    # Reconfigure the Treeview columns based on the DataFrame columns
    tree['columns'] = list(dataframe.columns)

    # Set up the new column headings
    for col in tree['columns']:
        tree.heading(col, text=col)
        # Here we use `font` directly since it has been imported
        tree.column(col, width=font.Font().measure(col.title()), anchor='w')

def update_treeview(dataframe):
    # Check if the DataFrame is empty
    if dataframe.empty:
        # Clear the existing content in the Treeview
        tree.delete(*tree.get_children())
        # Optionally, you could update the treeview or a status label to say "No results"
        messagebox.showinfo("Search Result", "No items found.")
    else:
        # Configure Treeview columns based on the DataFrame
        configure_treeview_columns(dataframe)
        # Add new rows to the Treeview
        for _, row in dataframe.iterrows():
            tree.insert("", "end", values=list(row))

# Set up the main application window
app_search = tk.Tk()
app_search.title("Warehouse Inventory Search")

# Define the columns for the Treeview
columns = ('Quantity', 'Section', 'Column', 'Level')
tree = ttk.Treeview(app_search, columns=columns, show='headings')

# Define the column headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=50)  # Adjust the width as needed

# Pack the Treeview widget into the main window
tree.pack(side=tk.TOP, fill='x')

# Frame for Search UI
search_frame = ttk.Frame(app_search)
search_frame.pack(fill='x', padx=5, pady=5)

# Search by Product Code UI
ttk.Label(search_frame, text="Search Product Code:").pack(side=tk.LEFT)
product_code_entry = ttk.Entry(search_frame)
product_code_entry.pack(side=tk.LEFT)
search_code_button = ttk.Button(search_frame, text="Search by Code", command=search_by_product_code)
search_code_button.pack(side=tk.LEFT)

# Search by Product Name UI
ttk.Label(search_frame, text="Search Product Name:").pack(side=tk.LEFT)
product_name_entry = ttk.Entry(search_frame)
product_name_entry.pack(side=tk.LEFT)
search_name_button = ttk.Button(search_frame, text="Search by Name", command=search_by_product_name)
search_name_button.pack(side=tk.LEFT)

# Rack Search UI
ttk.Label(app_search, text="Section:").pack(side=tk.LEFT)
section_entry = ttk.Entry(app_search, width=5)
section_entry.pack(side=tk.LEFT)

ttk.Label(app_search, text="Column:").pack(side=tk.LEFT)
column_entry = ttk.Entry(app_search, width=5)
column_entry.pack(side=tk.LEFT)

ttk.Label(app_search, text="Level:").pack(side=tk.LEFT)
level_entry = ttk.Entry(app_search, width=5)
level_entry.pack(side=tk.LEFT)

search_rack_button = ttk.Button(app_search, text="Search Rack", command=search_rack_contents)
search_rack_button.pack(side=tk.LEFT)


app_search.mainloop()

