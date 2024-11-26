import requests
from tkinter import Tk, Label, Entry, Button, Text, END, messagebox

# Function to shorten the URL
def shorten_url():
    original_url = url_input.get().strip()
    if not original_url:
        messagebox.showwarning("Warning", "Please enter a URL to shorten.")
        return

    try:
        # Making a POST request to the API
        response = requests.post(f"https://api.shrtco.de/v2/shorten?url={original_url}")
        data = response.json()

        if response.status_code == 201 or data["ok"]:
            short_url = data["result"]["full_short_link"]
            # Display the shortened URL in the output box
            output_text.delete("1.0", END)
            output_text.insert(END, f"Original URL: {original_url}\nShortened URL: {short_url}")
        else:
            error_message = data.get("error", "Failed to shorten URL.")
            messagebox.showerror("Error", error_message)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to clear the input and output
def clear_fields():
    url_input.delete(0, END)
    output_text.delete("1.0", END)

# Setting up the Tkinter GUI
root = Tk()
root.title("URL Shortener")
root.geometry("600x400")
root.resizable(False, False)

# Title Label
Label(root, text="URL Shortener", font=("Arial", 20, "bold")).pack(pady=10)

# URL Input
Label(root, text="Enter the URL to shorten:", font=("Arial", 12)).pack(pady=5)
url_input = Entry(root, font=("Arial", 14), width=50)
url_input.pack(pady=5)

# Buttons
Button(root, text="Shorten URL", font=("Arial", 12), bg="#4CAF50", fg="white", command=shorten_url).pack(pady=10)
Button(root, text="Clear", font=("Arial", 12), bg="#f44336", fg="white", command=clear_fields).pack(pady=5)

# Output Box
Label(root, text="Shortened URL Output:", font=("Arial", 12)).pack(pady=5)
output_text = Text(root, font=("Arial", 12), height=10, width=65)
output_text.pack(pady=10)

# Run the application
root.mainloop()
