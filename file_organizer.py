import tkinter as tk
import os
from file_organizer import organize_files

root = tk.Tk()

# root.title("simple Input and Button GUI")
# root.geometry("300x150")

root.title("File Organizar")
root.geometry("400x250")

def show_input():
    address = entry.get()

    print("Address is :", address)
    if os.path.exists(address):
        organize_files(address)

label = tk.Label(root, text="Enter Directory Address:")
label.pack(pady=20)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

button = tk.Button(root, text="submit", command=show_input)
button.pack(pady=10)

root.mainloop()