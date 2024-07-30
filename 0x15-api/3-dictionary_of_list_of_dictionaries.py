#!/usr/bin/python3
"""extend your Python script to export data in the JSON format."""

import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
