

import tkinter as tk
from tkinter import Entry, messagebox
import Management_Class
from tkinter import ttk

root = tk.Tk()

root.title("Management System")

appLabel = tk.Label(root, text="Management System", width = 20)
appLabel.config(font=("Sylfaen", 30))
appLabel.pack(padx=(20,20), pady=(30, 10))

nameLabel = tk.Label(root, text="Enter your name")
nameLabel.config(font=("Sylfaen", 13))
nameLabel.pack()

nameEntry = Entry(root, width=30)
nameEntry.pack(pady=(0, 20))

addressLabel = tk.Label(root, text="Enter your address")
addressLabel.config(font=("Sylfaen", 13))
addressLabel.pack()

addressEntry = Entry(root, width=30)
addressEntry.pack(pady=(0, 20))

phoneLabel = tk.Label(root, text="Enter your phone")
phoneLabel.config(font=("Sylfaen", 13))
phoneLabel.pack()

phoneEntry = Entry(root, width=30)
phoneEntry.pack(pady=(0, 20))

def save_details():
    name = nameEntry.get()
    address = addressEntry.get()
    phone = phoneEntry.get()
    if (len(name)>0 and len(address)>0 and len(phone)>0):
        obj = Management_Class.Management()
        obj.add_data(name, address, phone)
        obj.display_data()
        obj.save_details()
        messagebox.showinfo("Success", "Your details have saved successfully.")
    else:
        messagebox.showerror("Error", "Enter all the details to save the data.")

def display_records():
    second = tk.Tk()
    second.title('Displaying Data')

    second_appLabel = tk.Label(second, text="Displaying Data", width=30)
    second_appLabel.config(font=("Sylfaen", 30))
    second_appLabel.pack(padx=(20, 20), pady=(10, 20))

    obj = Management_Class.Management()
    details = obj.display_details()
################
    tree = ttk.Treeview(second)
    tree["columns"] = ("one", "two", "three")
    tree.heading("one", text="Student Name")
    tree.heading("two", text="Address")
    tree.heading("three", text="Phone Number")

    i = 0

    for row in details:
        tree.insert('', i, text="Student " + str(row[0]),
                    values=(row[1], row[2],
                            row[3]))
        i = i + 1

    tree.pack()
##############
    second.mainloop()

button = tk.Button(root, text="Save Details", command=lambda : save_details())
button.pack(pady=(0, 20))

display_button = tk.Button(root, text="Display Records",
                           command=lambda : display_records())
display_button.pack(pady=(0, 20))

root.mainloop()











































