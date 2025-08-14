import pandas as pd

def transform_data():
    """
    Transforms the raw cryptocurrency data.
    """
    # Read the raw data from the CSV file
    df = pd.read_csv("crypto_data.csv")

    # We'll select only the columns we're interested in for our dashboard.
    columns_to_keep = [
        "id",
        "symbol",
        "name",
        "image",
        "current_price",
        "market_cap",
        "market_cap_rank",
        "total_volume",
        "high_24h",
        "low_24h",
        "price_change_24h",
        "price_change_percentage_24h",
        "last_updated"
    ]
    # This is the corrected line:
    df_transformed = df[columns_to_keep].copy()

    # Let's create a new column to make it clear that the prices are in USD.
    df_transformed["currency"] = "usd"

    # The 'last_updated' column is a string. Let's convert it to a proper datetime format.
    df_transformed["last_updated"] = pd.to_datetime(df_transformed["last_updated"])

    # Save the transformed data to a new CSV file.
    df_transformed.to_csv("crypto_data_transformed.csv", index=False)

    print("Data successfully transformed and saved to crypto_data_transformed.csv")

if __name__ == "__main__":
    transform_data()