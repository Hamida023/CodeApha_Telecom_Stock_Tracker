import yfinance as yf  # To fetch stock data
import matplotlib.pyplot as plt  # For creating visualizations
import json  # To save and load portfolio data


# Define a class to manage the telecom stock portfolio
class TelecomPortfolioTracker:
    """A simple stock tracker for telecom companies.
      It allows you to add, remove, and track telecom stocks,
      as well as visualize your portfolio's distribution."""

    def __init__(self):
        # Predefined list of popular telecom companies and their stock symbols
        self.telecom_stocks = {
            "AT&T": "T",
            "Verizon": "VZ",
            "Vodafone": "VOD",
            "Nokia": "NOK",
            "Ericsson": "ERIC",
        }
        # Initialize an empty portfolio to store the user's stocks
        self.portfolio = {}

    def add_stock(self, company_name, quantity, purchase_price):
        """Add a telecom stock to your portfolio.
        company_name (str): Name of the company (e.g., "AT&T").
        quantity (int): Number of shares purchased.
        purchase_price (float): Price paid per share."""
        if not isinstance(quantity, int) or quantity <= 0:
            print("Error: Quantity should be a positive integer.")
            return
        if not isinstance(purchase_price, (int, float)) or purchase_price <= 0:
            print("Error: Purchase price should be a positive number.")
            return

        # Look up the company's stock symbol
        ticker = self.telecom_stocks.get(company_name)
        if not ticker:
            print(f"Error: {company_name} is not in our telecom stock list.")
            return

        # Add the stock to the portfolio
        self.portfolio[ticker] = {
            "quantity": quantity,
            "purchase_price": purchase_price,
        }
        print(f"Added {quantity} shares of {company_name} ({ticker}) at ${purchase_price} each.")

    def remove_stock(self, ticker):
        """Remove a stock from your portfolio using its stock symbol.
        ticker (str): The stock symbol (e.g., "T" for AT&T)."""
        if ticker in self.portfolio:
            del self.portfolio[ticker]
            print(f"Removed {ticker} from the portfolio.")
        else:
            print(f"Error: {ticker} is not in your portfolio.")

    def fetch_live_prices(self):
        """Fetch the latest prices for all stocks in the portfolio.
        Returns: A dictionary with stock symbols as keys and current prices as values."""
        prices = {}
        for ticker in self.portfolio.keys():
            try:
                stock = yf.Ticker(ticker)  # Fetch stock data from Yahoo Finance
                prices[ticker] = stock.info.get("currentPrice", 0)  # Get the current price
                if prices[ticker] == 0:  # Handle cases where the price is unavailable
                    print(f"Warning: Live price for {ticker} is unavailable.")
            except Exception as e:
                print(f"Error fetching price for {ticker}: {e}")
                prices[ticker] = 0
        return prices

    def calculate_portfolio_value(self):
        """Calculate the total value of your portfolio based on current stock prices.
        Returns: float: The total portfolio value in dollars."""
        live_prices = self.fetch_live_prices()
        total_value = 0
        # Calculate the value of each stock in the portfolio
        for ticker, details in self.portfolio.items():
            current_price = live_prices.get(ticker, 0)
            total_value += details["quantity"] * current_price
        return total_value

    def visualize_telecom_stocks(self):
        """Create a pie chart to visualize the distribution of your portfolio."""
        live_prices = self.fetch_live_prices()
        # Calculate the value of each stock in the portfolio
        data = {
            ticker: details["quantity"] * live_prices.get(ticker, 0)
            for ticker, details in self.portfolio.items()
        }
        # Filter out stocks with zero value
        data = {k: v for k, v in data.items() if v > 0}

        if not data:
            print("No data available for visualization.")
            return

        # Prepare data for the pie chart
        labels = data.keys()
        sizes = data.values()

        # Create and display the pie chart
        plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
        plt.title("Telecom Portfolio Distribution")
        plt.gcf().canvas.manager.set_window_title("Telecom Portfolio Tracker - Pie Chart")
        plt.show()

    def save_portfolio(self, filename="telecom_portfolio.json"):
        """Save your portfolio to a JSON file for future use.
        filename (str): The name of the file to save the data."""
        try:
            with open(filename, "w") as f:
                json.dump(self.portfolio, f)
            print(f"Portfolio saved to {filename}.")
        except Exception as e:
            print(f"Error saving portfolio: {e}")

    def load_portfolio(self, filename="telecom_portfolio.json"):
        """Load a saved portfolio from a JSON file.
        filename (str): The name of the file to load data from."""
        try:
            with open(filename, "r") as f:
                self.portfolio = json.load(f)
            print(f"Portfolio loaded from {filename}.")
        except FileNotFoundError:
            print(f"Error: {filename} not found.")
        except json.JSONDecodeError:
            print(f"Error: Failed to decode {filename}. Ensure it is a valid JSON file.")


if __name__ == "__main__":
    # Create an instance of the TelecomPortfolioTracker
    tracker = TelecomPortfolioTracker()
    # Add some telecom stocks to the portfolio
    tracker.add_stock("AT&T", 50, 18)  # 50 shares of AT&T at $18 each
    tracker.add_stock("Verizon", 20, 50)  # 20 shares of Verizon at $50 each
    # Display the total portfolio value
    print("Portfolio Value:", tracker.calculate_portfolio_value())
    # Visualize the portfolio distribution
    tracker.visualize_telecom_stocks()
    # Save the portfolio to a file
    tracker.save_portfolio()
    # Load the portfolio (demonstrating functionality)
    tracker.load_portfolio()
