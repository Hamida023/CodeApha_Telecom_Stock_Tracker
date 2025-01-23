# TelecomPortfolioTracker

A simple Python tool for managing and tracking telecom stock investments. This tracker allows you to add or remove stocks from your portfolio, calculate the total portfolio value using live stock prices, and visualize the distribution of your investments with a pie chart. It also supports saving and loading portfolio data.

---[portfolio tracker image](https://github.com/user-attachments/assets/f06b9f5c-586c-409c-9b8d-e360474cd768)

## Features

- **Add Telecom Stocks**: Add stocks of popular telecom companies to your portfolio.
- **Remove Stocks**: Remove stocks from your portfolio using their stock symbol.

- **Live Price Fetching**: Automatically fetch the latest stock prices using Yahoo Finance.
- **Portfolio Value Calculation**: Calculate the total value of your portfolio based on live stock prices.
- **Portfolio Visualization**: Display a pie chart showing the distribution of your telecom investments.
- **Save and Load Portfolio**: Save your portfolio to a JSON file and load it for future use.

---

## Requirements

- **Python 3.x**: The script is written in Python 3.
- **yfinance**: For fetching live stock data.
- **matplotlib**: For creating visualizations (pie charts).
- **json**: For saving and loading portfolio data.

You can install the required libraries with pip:

pip install yfinance matplotlib

## Usage

### 1. Clone the repository or copy the code into your own Python script.
### 2. Create an instance of the `TelecomPortfolioTracker` class:


tracker = TelecomPortfolioTracker()


### 3. Add stocks to your portfolio:


tracker.add_stock("AT&T", 50, 18)  # 50 shares of AT&T at $18 each
tracker.add_stock("Verizon", 20, 50)  # 20 shares of Verizon at $50 each


### 4. View the total value of your portfolio:

```python
print("Portfolio Value:", tracker.calculate_portfolio_value())
```

### 5. Visualize your portfolio distribution:


tracker.visualize_telecom_stocks()


### 6. Save your portfolio to a file:


tracker.save_portfolio()


### 7. Load a saved portfolio:

tracker.load_portfolio()

## Example Output

After adding stocks and calculating the portfolio value, the script will print the total portfolio value and display a pie chart with the portfolio's distribution.


## Notes

- The script currently supports a predefined list of telecom companies (e.g., AT&T, Verizon, Nokia).
- It fetches live stock prices from Yahoo Finance using the `yfinance` library, so an internet connection is required.
- Data is saved in a `telecom_portfolio.json` file by default.

---
This README provides a clear and concise guide on using the **TelecomPortfolioTracker** and covers installation, features, and usage examples.
