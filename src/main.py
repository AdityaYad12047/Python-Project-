import requests
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, messagebox

# Step 1: API Setup
API_KEY = "57NSFQM329SD308B"  # Replace with your API key
BASE_URL = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=57NSFQM329SD308B"

def get_stock_price(symbol):
    """
    Fetch the current stock price using Alpha Vantage API.
    """
    url = f"{BASE_URL}"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "1min",
        "apikey": API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()

    if "Time Series (1min)" in data:
        latest_time = list(data["Time Series (1min)"].keys())[0]
        latest_data = data["Time Series (1min)"][latest_time]
        price = float(latest_data["1. open"])
        return {"symbol": symbol, "price": price, "time": latest_time}
    else:
        return {"error": data.get("Note", "Error fetching data. Check API key or symbol.")}

def fetch_historical_data(symbol):
    """
    Fetch historical stock data using Alpha Vantage API.
    """
    url = f"{BASE_URL}"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()

    if "Time Series (Daily)" in data:
        daily_data = data["Time Series (Daily)"]
        dates = []
        prices = []
        for date, stats in daily_data.items():
            dates.append(date)
            prices.append(float(stats["1. open"]))
        return dates[::-1], prices[::-1]
    else:
        return None, None

def plot_stock_trend(dates, prices, symbol):
    """
    Plot the historical stock trend.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, marker="o", linestyle="-", color="b")
    plt.title(f"Stock Price Trend for {symbol}")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.xticks(rotation=45, fontsize=8)
    plt.tight_layout()
    plt.show()

def fetch_and_display_stock():
    """
    Handle fetching and displaying stock data through the GUI.
    """
    symbol = stock_symbol_entry.get().upper()
    if not symbol:
        messagebox.showerror("Error", "Please enter a stock symbol.")
        return

    stock_data = get_stock_price(symbol)
    if "error" in stock_data:
        messagebox.showerror("Error", stock_data["error"])
        return

    # Display stock information
    stock_price_label.config(text=f"Current Price: ${stock_data['price']}")
    stock_time_label.config(text=f"Time: {stock_data['time']}")

    # Fetch and plot historical data
    dates, prices = fetch_historical_data(symbol)
    if dates and prices:
        plot_stock_trend(dates, prices, symbol)
    else:
        messagebox.showerror("Error", "Unable to fetch historical data for plotting.")

# GUI Setup
root = Tk()
root.title("Stock Price Tracker")
root.geometry("400x300")

# Labels and Entry
Label(root, text="Enter Stock Symbol:", font=("Arial", 12)).pack(pady=10)
stock_symbol_entry = Entry(root, font=("Arial", 12))
stock_symbol_entry.pack(pady=5)

# Buttons
fetch_button = Button(root, text="Fetch Stock Data", font=("Arial", 12), command=fetch_and_display_stock)
fetch_button.pack(pady=10)

# Output Labels
stock_price_label = Label(root, text="Current Price: N/A", font=("Arial", 12))
stock_price_label.pack(pady=5)

stock_time_label = Label(root, text="Time: N/A", font=("Arial", 12))
stock_time_label.pack(pady=5)

# Run the GUI
root.mainloop()
