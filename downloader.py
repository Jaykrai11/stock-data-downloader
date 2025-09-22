import sys
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# ticker ='AAPL'
# start_date='2020-01-01'
# end_date='2024-01-01'

# data= yf.download(ticker,start=start_date,end=end_date)

# print(data.head())

# data.to_csv(f'{ticker}_stock_data.csv',index=True)

# print(f"Stock data of {ticker}_stock_data.csv saved successfully")

def main():
    try:
        ticker = input("Enter the stock ticker symbol (e.g.,TSLA, AAPL): ").strip().upper()
        start_date = input("Enter the start date (yyyy-mm-dd): ").strip()
        end_date = input("Enter the end date (yyyy-mm-dd): ").strip()

        if not ticker or not start_date or not end_date:
            print("Invalid input. Please provide valid inputs.")
            sys.exit(1)
        try:
            start_dt = pd.to_datetime(start_date, format="%Y-%m-%d")
            end_dt = pd.to_datetime(end_date, format="%Y-%m-%d")
            if start_dt > end_dt:
                print("Start date must be before or equal to end date.")
                sys.exit(1)
        except ValueError:
            print("Dates must be in YYYY-MM-DD format.")
            sys.exit(1)
        
        print(f"Downloading stock data for {ticker} from {start_date} to {end_date}...")
        try:
            data = yf.download(ticker, start=start_date, end=end_date, progress=True, auto_adjust=True)
        except Exception as e:
            print(f"Error downloading data: {e}")
            sys.exit(1)

        if data.empty:
            print("No data found in the given date range.")
            sys.exit(1)
        
        # Moving averages
        try:
            data["MA20"] = data["Close"].rolling(window=20).mean()
            data["MA50"] = data["Close"].rolling(window=50).mean()
        except KeyError:
            print("Downloaded data does not contain 'Close' column.")
            sys.exit(1)

        print(data.head())

        filename = f"{ticker}_{start_date}_to_{end_date}.csv"
        try:
            data.to_csv(filename, index=True)
            print(f"Saved: {filename}")
        except Exception as e:
            print(f"Error saving CSV: {e}")

        # Plot price and MAs
        try:
            plt.figure(figsize=(12, 6))
            plt.plot(data.index, data["Close"], label=f"{ticker} Close", linewidth=1.2)
            plt.plot(data.index, data["MA20"], label="MA 20", linewidth=1)
            plt.plot(data.index, data["MA50"], label="MA 50", linewidth=1)

            plt.title(f"{ticker} Price with 20/50-day Moving Averages")
            plt.xlabel("Date")
            plt.ylabel("Price")
            plt.grid(True, alpha=0.3)
            plt.legend()
            plt.tight_layout()

            # Save chart
            png_name = f"{ticker}_{start_date}_to_{end_date}.png"
            plt.savefig(png_name, dpi=150)
            print(f"Saved Chart: {png_name}")

            # Show chart
            plt.show()
        except Exception as e:
            print(f"Error plotting or saving chart: {e}")

    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()