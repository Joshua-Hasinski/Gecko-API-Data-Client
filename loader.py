import pandas as pd
import sqlite3

def load_data_to_db():
    """
    Loads the transformed data into a SQLite database.
    """
    # Read the transformed data from the CSV file
    df = pd.read_csv("crypto_data_transformed.csv")

    # Create a connection to the SQLite database.
    # This will create the file 'crypto.db' if it doesn't exist.
    conn = sqlite3.connect('crypto.db')

    # Load the DataFrame into a table named 'coins'.
    # if_exists='replace' means if the table already exists, it will be deleted and recreated.
    # This is useful for rerunning our script with updated data.
    df.to_sql('coins', conn, if_exists='replace', index=False)

    # Close the database connection
    conn.close()

    print("Data successfully loaded into crypto.db")

if __name__ == "__main__":
    load_data_to_db()