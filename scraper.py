# This module scrapes the URL content and extracts text.

import requests
from bs4 import BeautifulSoup

def scrape(url):
    try:
        # Make a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful
        response.raise_for_status() # Raise an exception for 4xx and 5xx status codes

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract text from all paragraphs
        text = ' '.join([p.get_text() for p in soup.find_all('p')])

        return text
    # Handle exceptions
    except requests.RequestException as e:
        print(f'Error: {e}')
        return None