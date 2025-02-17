import requests
from bs4 import BeautifulSoup
import json

# URL of the page
url = "https://temml.org/tests/wiki-tests"

# Fetch the webpage
response = requests.get(url)
if response.status_code != 200:
    print("Failed to retrieve the page.")
    exit()

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all tables
tables = soup.find_all("table")

# Dictionary to store extracted data
data = {}

# Iterate through tables
for table in tables:
    rows = table.find_all("tr")[1:]  # Skip header row if it exists
    
    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 2:  # Ensure row has at least 2 columns (ID, Source)
            row_id = cols[0].text.strip()
            source = cols[1].text.strip()
            if row_id.isdigit():  # Ensure ID is a valid number
                data[row_id] = source

# Save to JSON file
output_filename = "wiki_tests_data.json"
with open(output_filename, "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print(f"Extracted {len(data)} items and saved to {output_filename}.")
