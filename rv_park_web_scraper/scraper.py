import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

# Enhanced regular expression to find email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Function to extract the first valid email from a given URL
def extract_first_email_from_url(url, timeout=10):
    try:
        with requests.get(url, timeout=timeout) as response:
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                # Find all email addresses in the page content
                emails = re.findall(email_pattern, soup.get_text())

                # Filter out invalid email addresses
                valid_emails = [email for email in emails if re.match(email_pattern, email)]

                # Return the first valid email found, or None if no valid emails found
                return valid_emails[0] if valid_emails else None
            else:
                print(f"Failed to fetch {url}. Status code: {response.status_code}")
                return None
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# Load the CSV file containing website URLs
csv_file = 'master_file_websites.csv'  # Replace with your CSV filename
output_csv = 'emails_extracted.csv'  # Output CSV filename

# Read the CSV file into a pandas DataFrame
data = pd.read_csv(csv_file)

# Function to process each row in parallel
def process_row(row):
    website_url = row.website
    url = f"https://{website_url}" if not urlparse(website_url).scheme else website_url
    return extract_first_email_from_url(url)

# Use ThreadPoolExecutor for parallel processing
with ThreadPoolExecutor() as executor:
    data['First_Email'] = list(executor.map(process_row, data.itertuples()))

# Save the updated DataFrame to a new CSV file
data.to_csv(output_csv, index=False)
