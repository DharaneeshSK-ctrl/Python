import requests
from bs4 import BeautifulSoup
import csv

# List of web pages to scrape
urls = [
    "https://quotes.toscrape.com/page/1/",
    "https://quotes.toscrape.com/page/2/",
    "https://quotes.toscrape.com/page/3/"
]

# Store extracted data
quotes_data = []

# Loop through each page
for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:
            text = quote.find("span", class_="text").get_text(strip=True)
            author = quote.find("small", class_="author").get_text(strip=True)
            tags = ", ".join(
                [tag.get_text(strip=True) for tag in quote.find_all("a", class_="tag")]
            )

            quotes_data.append([text, author, tags])

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")

# Save data to CSV
output_file = "quotes_data.csv"

with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author", "Tags"])
    writer.writerows(quotes_data)

print(f"\nData successfully exported to '{output_file}'")
print(f"Total Quotes Extracted: {len(quotes_data)}")
