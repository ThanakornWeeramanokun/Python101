import tkinter as tk
from tkinter import ttk
import csv

def fetch_data():
    # Clear the Treeview widget
    for row in tree.get_children():
        tree.delete(row)
        
    # Read data from the CSV file
    with open('data.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        # Skip the header row
        next(reader)
        # Add data to the Treeview widget
        for row in reader:
            tree.insert("", tk.END, values=row)

# Create the main window
root = tk.Tk()
root.geometry('800x600')

# Create the Treeview widget
tree = ttk.Treeview(root, columns=('date', 'time', 'title', 'description', 'user', 'department', 'location', 'phone'))
tree.heading('#0', text='No.')
tree.heading('date', text='Date')
tree.heading('time', text='Time')
tree.heading('title', text='Title')
tree.heading('description', text='Description')
tree.heading('user', text='User')
tree.heading('department', text='Department')
tree.heading('location', text='Location')
tree.heading('phone', text='Phone')
tree.column('#0', width=50, minwidth=50, anchor=tk.CENTER)
tree.column('date', width=100, minwidth=100, anchor=tk.CENTER)
tree.column('time', width=100, minwidth=100, anchor=tk.CENTER)
tree.column('title', width=150, minwidth=150, anchor=tk.CENTER)
tree.column('description', width=250, minwidth=250, anchor=tk.CENTER)
tree.column('user', width=100, minwidth=100, anchor=tk.CENTER)
tree.column('department', width=100, minwidth=100, anchor=tk.CENTER)
tree.column('location', width=100, minwidth=100, anchor=tk.CENTER)
tree.column('phone', width=100, minwidth=100, anchor=tk.CENTER)
tree.grid(row=1, column=0, sticky="nsew")

# Create a label widget for spacing
label = tk.Label(root, text="", height=2)
label.grid(row=0, column=0)

# Create the fetch data button
button_fetch_data = tk.Button(root, text='Refresh', command=fetch_data)
button_fetch_data.grid(row=2, column=0, sticky="nsew")

# Configure grid weights
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

# Fetch data from the CSV file
fetch_data()

root.mainloop()
