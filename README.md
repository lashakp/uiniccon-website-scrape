🕸️ Web Scraping Project: Uniccon Group Website
This Python script scrapes content from the Uniccon Group homepage and extracts key HTML elements such as:

Webpage title

Hyperlinks (<a> tags)

Headings (<h1> and <h2> tags)

Paragraphs (<p> tags)

Embedded CSS styles (<style> tags)

Meta tags (with both name and content attributes)

The extracted data is then saved in a structured format (CSV) for further analysis or processing.

🧾 Features
Extracts important content from a webpage using requests and BeautifulSoup

Cleans and structures data into a Pandas DataFrame

Saves the output as a CSV file for easy use

📂 Output
The CSV file includes columns for:

Title – the <title> tag of the page

Links – all extracted hyperlinks

Headings – text inside <h1> and <h2> tags

Paragraphs – cleaned text from <p> tags

Styles – embedded styles from <style> tags

Meta Tags – key-value pairs of meta information

