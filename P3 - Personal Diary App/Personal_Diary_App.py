import os
from tkinter import Tk, Text, Button, Label, Scrollbar, filedialog, messagebox, END, RIGHT, Y

# Function to save diary entry
def save_entry():
    content = diary_text.get("1.0", END).strip()
    if not content:
        messagebox.showwarning("Warning", "Diary entry cannot be empty!")
        return

    # Ask for file location
    filepath = filedialog.asksaveasfilename(
        title="Save Diary Entry",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")],
    )
    if filepath:
        with open(filepath, "w") as file:
            file.write(content)
        messagebox.showinfo("Success", "Diary entry saved successfully!")
        diary_text.delete("1.0", END)

# Function to open a diary entry
def open_entry():
    filepath = filedialog.askopenfilename(
        title="Open Diary Entry",
        filetypes=[("Text Files", "*.txt")],
    )
    if filepath:
        with open(filepath, "r") as file:
            content = file.read()
        diary_text.delete("1.0", END)
        diary_text.insert("1.0", content)

# Function to clear the text area
def clear_entry():
    diary_text.delete("1.0", END)

# Setting up GUI
root = Tk()
root.title("Personal Diary")
root.geometry("600x500")

# Title Label
Label(root, text="Personal Diary", font=("Arial", 18, "bold")).pack(pady=10)

# Text Area
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
diary_text = Text(root, wrap="word", yscrollcommand=scrollbar.set, font=("Arial", 12))
diary_text.pack(expand=True, fill="both", padx=10, pady=10)
scrollbar.config(command=diary_text.yview)

# Buttons
Button(root, text="Save Entry", command=save_entry, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=5)
Button(root, text="Open Entry", command=open_entry, bg="#2196F3", fg="white", font=("Arial", 12)).pack(pady=5)
Button(root, text="Clear Entry", command=clear_entry, bg="#f44336", fg="white", font=("Arial", 12)).pack(pady=5)

# Run the GUI
root.mainloop()
