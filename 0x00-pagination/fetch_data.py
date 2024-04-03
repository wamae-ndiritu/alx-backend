#!/usr/bin/env python3
"""
Fetches data from the internet
"""
import requests
import csv


def fetch_data_and_save_to_csv(url: str, filename: str):
    """
    Fetch data from the given URL and save it to a CSV file.

    Args:
        url (str): The URL from which to fetch the data.
        filename (str): The name of the CSV file to save the data.
    """
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text

        # Write data to CSV file
        with open(filename, 'w', newline='') as csvfile:
            csvfile.write(data)
        
        print(f"Data saved to {filename}")
    else:
        print(f"Failed to fetch data from {url}")

if __name__ == "__main__":
    url ="https://intranet.alxswe.com/rltoken/NBLY6mdKDBR9zWvNADwjjg"
    filename = "Popular_Baby_Names.csv"
    fetch_data_and_save_to_csv(url, filename)

