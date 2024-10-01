#!/usr/bin/python3
"""
This module provides functionality to convert CSV data to JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON format and write to 'data.json'.

    Args:
    csv_filename (str): The name of the CSV file to convert

    Returns:
    bool: True if conversion was successful, False otherwise
    """
    try:
        # Read the CSV file
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        # Write the JSON data
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
