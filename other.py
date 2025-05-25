import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Define the URL
url = "https://uniccongroup.com/"

# Step 2: Make the HTTP request
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

# Step 3: Check if the request was successful
if response.status_code != 200:
    raise Exception(f"Failed to load page. Status code: {response.status_code}")
print(f"HTTP Response: {response}")

# Step 4: Parse HTML using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 5: Extract the title
title = soup.title.string.strip() if soup.title and soup.title.string else "No title found"
print(f"Title of the page: {title}")

# Step 6: Extract all links (anchor tags with href)
links = [a['href'].strip() for a in soup.find_all('a', href=True)]
print(f"Links found on the page: {links}")

# Step 7: Extract headings (h1 and h2 only)
headings = [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2'])]
print(f"Headings found on the page: {headings}")

# Step 8: Extract all paragraph text
paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
print(f"Paragraphs found on the page: {paragraphs}")

# Step 9: Extract internal style blocks
styles = [style.get_text(strip=True) for style in soup.find_all('style')]
print(f"Styles found on the page: {styles}")

# Step 10: Extract meta tags with name and content attributes
meta_tags = {
    meta['name'].strip(): meta['content'].strip()
    for meta in soup.find_all('meta', attrs={'name': True, 'content': True})
}
print(f"Meta tags found on the page: {meta_tags}")

# Step 11: Prepare data for DataFrame
# Note: Lists and dicts must be handled carefully in a DataFrame
data = {
    "Title": [title],
    "Links": [links],
    "Headings": [headings],
    "Paragraphs": [paragraphs],
    "Styles": [styles],
    "Meta Tags": [meta_tags]
}

# Step 12: Create DataFrame
df = pd.DataFrame(data)

# Step 13: Print and save DataFrame
print("\n--- Extracted DataFrame ---")
print(df)

df.to_csv("new_extracted_data.csv", index=False)
print("\n✅ Data saved to 'new_extracted_data.csv'")
