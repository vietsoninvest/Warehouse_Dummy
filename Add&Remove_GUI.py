#!/usr/bin/env python
# coding: utf-8

# In[1]:


# UIUX.py
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from Function import add_item, remove_item


# In[3]:


def add_item_to_inventory():
    product_code = int(product_code_entry.get())  # Convert to int
    quantity = int(quantity_entry.get())
    section = section_entry.get()  # Will be converted to int in the function
    column = column_entry.get()
    level = level_entry.get()  # Will be converted to int in the function
    
    add_item(product_code, quantity, section, column, level)
    messagebox.showinfo("Success", "Item successfully added.")

def remove_item_from_inventory():
    product_code = int(product_code_entry.get())  # Convert to int
    quantity = int(quantity_entry.get())
    section = section_entry.get()
    column = column_entry.get()
    level = level_entry.get()
    
    remove_item(product_code, quantity, section, column, level)
    messagebox.showinfo("Success", "Item successfully removed.")
    
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
app = tk.Tk()
app.title("Warehouse Inventory Update")

# Define the columns for the Treeview
columns = ('Quantity', 'Section', 'Column', 'Level')
tree = ttk.Treeview(app, columns=columns, show='headings')

# Define the column headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=50)  # Adjust the width as needed

# Pack the Treeview widget into the main window
tree.pack(side=tk.TOP, fill='x')

# Frame for Add/Remove UI
add_remove_frame = ttk.Frame(app)
add_remove_frame.pack(fill='x', padx=5, pady=5)

# Add/Remove Item UI
ttk.Label(add_remove_frame, text="Add/Remove Product Code:").pack(side=tk.LEFT)
product_code_entry = ttk.Entry(add_remove_frame)
product_code_entry.pack(side=tk.LEFT)

# Entry for Quantity
ttk.Label(add_remove_frame, text="Quantity:").pack(side=tk.LEFT)
quantity_entry = ttk.Entry(add_remove_frame)
quantity_entry.pack(side=tk.LEFT)

# Entry for location
ttk.Label(app, text="Section:").pack(side=tk.LEFT)
section_entry = ttk.Entry(app, width=5)
section_entry.pack(side=tk.LEFT)

ttk.Label(app, text="Column:").pack(side=tk.LEFT)
column_entry = ttk.Entry(app, width=5)
column_entry.pack(side=tk.LEFT)

ttk.Label(app, text="Level:").pack(side=tk.LEFT)
level_entry = ttk.Entry(app, width=5)
level_entry.pack(side=tk.LEFT)

# Button to Add Item
add_button = ttk.Button(add_remove_frame, text="Add Item", 
                        command=add_item_to_inventory)  
add_button.pack(side=tk.LEFT, padx=(10,0))

# Button to Remove Item
remove_button = ttk.Button(add_remove_frame, text="Remove Item", 
                        command=remove_item_from_inventory)  
remove_button.pack(side=tk.LEFT)

app.mainloop()
    


# In[ ]:




