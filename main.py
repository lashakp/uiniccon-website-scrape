# Importing required libraries
import requests                          # For making HTTP requests to fetch webpage content
from bs4 import BeautifulSoup            # For parsing HTML and extracting data from the page
import pandas as pd                      # For creating and saving tabular data

# Step 1: Define the URL of the webpage to scrape
url = "https://uniccongroup.com/"

# Step 2: Make a GET request to fetch the raw HTML content of the page
response = requests.get(url)

# Step 3: Check if the request was successful (status code 200 means OK)
if response.status_code != 200:
    # If the page couldn't be loaded, raise an exception with the status code
    raise Exception(f"Failed to load page with status code: {response.status_code}")

# Step 4: Print the response object (just for debugging or confirmation)
print(response)

# Step 5: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 6: Extract the title of the webpage
title = soup.title.string if soup.title else "No title found"  # Check if <title> tag exists
print(f"Title of the page: {title}")

# Step 7: Extract all hyperlinks (<a> tags with href attribute)
links = [a['href'].strip() for a in soup.find_all('a', href=True)]  # Clean whitespace from URLs
print(f"Links found on the page: {links}")

# Step 8: Extract all headings (only h1 and h2 tags)
headings = [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2'])]  # Get text without surrounding whitespace
print(f"Headings found on the page: {headings}")

# Step 9: Extract all paragraphs (<p> tags)
paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]  # Get text content of paragraphs
print(f"Paragraphs found on the page: {paragraphs}")

# Step 10: Extract all embedded CSS styles (inside <style> tags)
styles = [style.get_text(strip=True) for style in soup.find_all('style')]  # Get CSS code as text
print(f"Styles found on the page: {styles}")

# Step 11: Extract meta tags with both 'name' and 'content' attributes
# Typically used for SEO, page description, keywords, author info, etc.
meta_tags = {
    meta['name']: meta['content']
    for meta in soup.find_all('meta', attrs={'name': True, 'content': True})
}
print(f"Meta tags found on the page: {meta_tags}")

# Step 12: Prepare the extracted data into a dictionary for tabular conversion
data = {
    "Title": title,              # Single title string
    "Links": links,              # List of hyperlinks
    "Headings": headings,        # List of headings (h1, h2)
    "Paragraphs": paragraphs,    # List of paragraphs
    "Styles": styles,            # List of CSS styles
    "Meta Tags": meta_tags       # Dictionary of meta tags
}

# Step 13: Convert the data dictionary into a DataFrame
# Each list will be expanded into its own column with multiple rows
df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))

# Step 14: Display the resulting DataFrame
print(df)

# Step 15: Save the DataFrame as a CSV file
df.to_csv("extracted_data.csv", index=False)  # Exclude row numbers from the CSV
print("\n✅ Data saved to 'extracted_data.csv'")
