import requests
from bs4 import BeautifulSoup
import os
import json
import re  # For removing unwanted escape sequences
from config_scraping_URLs import source_path, easy_urls, medium_urls, hard_urls

# Function to clean text by removing unwanted Unicode escape sequences and line breaks
def clean_text(text):
    # Replace Unicode escape sequences with regular characters
    

    text = re.sub(r'\\u[0-9a-fA-F]{4}', '', text)  # Removes Unicode escapes
    text = text.replace('\\n\\n', ' ')  # Replace double newlines with a space
    text = text.replace('\n', ' ')  # Replace single newlines with a space
    text = text.replace('\n\n', ' ')  # Replace single newlines with a space
    #text = text.replace('\u', ' ')  # Replace single newlines with a space
    text = re.sub(r'\\', '', text)  # Removes stray backslashes
    return text.strip()  # Remove leading/trailing whitespace

# Function to scrape the content from sections and format it with "Text:" before headers
def scrape_website_to_json(url):
    # Fetch the webpage content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the <section> with id "main" and class "fullwidth"
    main_section = soup.find('section', {'id': 'main', 'class': 'fullwidth'})

    if not main_section:
        print(f"Main section not found for {url}. Skipping...")
        return None

    # Collect text content from headers and paragraphs
    content = []
    started_scraping = False

    for element in main_section.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']):
        # Start scraping after the first <h1>
        if element.name == 'h1' and not started_scraping:
            started_scraping = True
            content.append(f"Text: {element.get_text(strip=True)}")  # Add "Text:" before the first header
        elif started_scraping:
            if element.name.startswith('h'):  # Add "Text:" before subsequent headers
                content.append(f"Text: {element.get_text(strip=True)}")
            elif element.name == 'p':  # Append paragraph text
                content.append(element.get_text(strip=True))

    # Combine the content into a single cleaned text block
    text_content = '\n\n'.join(content)
    cleaned_content = clean_text(text_content)
    return {"content": cleaned_content}

# Function to scrape multiple URLs and save content into a single JSON file
def scrape_and_save_to_json(urls, json_path):
    if os.path.exists(json_path):
        # Load existing data if the file already exists
        with open(json_path, 'r', encoding='utf-8') as f:
            scraped_data = json.load(f)
    else:
        scraped_data = []

    for url in urls:
        print(f"Scraping URL: {url}")
        scraped_content = scrape_website_to_json(url)
        if scraped_content:
            # Append scraped content to the list
            scraped_data.append(scraped_content)
        else:
            print(f"Failed to scrape {url}.")

    # Write the updated scraped data to the JSON file
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(scraped_data, f, indent=4, ensure_ascii=False)

# Main function to scrape all difficulty levels and save to a JSON file
def scrape_all_to_single_json():
    os.makedirs(source_path, exist_ok=True)
    json_path = os.path.join(source_path, 'scraped_data.json')

    # Scrape and append all URLs into the JSON file
    scrape_and_save_to_json(easy_urls, json_path)
    scrape_and_save_to_json(medium_urls, json_path)
    scrape_and_save_to_json(hard_urls, json_path)

    print(f"All scraped content has been saved to {json_path}")

# Run the script
scrape_all_to_single_json()
