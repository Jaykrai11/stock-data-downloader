# stock-data-downloader
Tool to manage and download stock market data

Simple Python tool to download historical stock data (CSV) using yfinance. Calculates 20/50-day moving averages and plots the price trend.

## Features
- Download historical stock data for any ticker symbol
- User inputs ticker, start date, and end date
- Calculates 20-day and 50-day moving averages
- Saves data as CSV
- Plots and saves a PNG chart of price and moving averages
- Error handling for invalid input, missing data, and download issues

## Installation
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

## Usage

Run the downloader script:

```sh
python downloader.py
```

You will be prompted to enter:
- Stock ticker symbol (e.g., AAPL, TSLA)
- Start date (YYYY-MM-DD)
- End date (YYYY-MM-DD)

The script will:
- Download the data
- Calculate moving averages
- Save a CSV file and a PNG chart in the current folder

## Example

```
Enter the stock ticker symbol (e.g.,TSLA, AAPL): AAPL
Enter the start date (yyyy-mm-dd): 2024-01-01
Enter the end date (yyyy-mm-dd): 2024-06-01
```

## Requirements
- Python 3.7+
- yfinance
- pandas
- matplotlib

Install requirements with:
```
pip install -r requirements.txt
```

