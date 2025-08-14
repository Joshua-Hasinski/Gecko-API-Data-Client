import requests
import pandas as pd

def extract_data():
    """
    Extracts cryptocurrency data from the CoinGecko API.
    """
    # The URL for the CoinGecko API endpoint we want to get data from
    url = "https://api.coingecko.com/api/v3/coins/markets"

    # Parameters for the API request. We're asking for the top 100 cryptocurrencies by market cap in USD.
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": False
    }

    # Send a GET request to the API
    response = requests.get(url, params=params)

    # The API returns data in JSON format. We can convert it to a Python list of dictionaries.
    data = response.json()

    # We'll use pandas to create a DataFrame, which is like a spreadsheet in Python.
    df = pd.DataFrame(data)

    # We'll save the data to a CSV file. This is a common format for storing structured data.
    df.to_csv("crypto_data.csv", index=False)

    print("Data successfully extracted and saved to crypto_data.csv")

if __name__ == "__main__":
    extract_data()