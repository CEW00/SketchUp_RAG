import requests
from config_models import current_dir
from bs4 import BeautifulSoup
import os
import json
import re  # For removing unwanted escape sequences

# Define the URLs to scrape
urls = [
    'https://designerhacks.com/how-to-create-sections-in-sketchup/',
    'https://designerhacks.com/how-to-stop-clipping-in-sketchup/',
    'https://designerhacks.com/how-to-get-rid-of-duplicate-shadows-in-sketchup/',
    'https://designerhacks.com/how-to-draw-2d-in-sketchup/',
    'https://designerhacks.com/how-to-make-an-architectural-2d-elevation-in-sketchup/',
    'https://designerhacks.com/mass-select-components-in-sketchup/',
    'https://designerhacks.com/how-to-add-materials-in-sketchup/',
    'https://designerhacks.com/getting-started-with-sketchup-for-beginners/',
    'https://designerhacks.com/stop-doing-this-with-your-sketchup-site-models/',
    'https://designerhacks.com/5-sketchup-mistakes-every-beginner-makes-and-how-to-avoid-them/',
    'https://designerhacks.com/how-to-get-essential-site-information-for-architecture-projects/',
    'https://designerhacks.com/how-to-snap-in-sketchup-tutorial/',
    'https://designerhacks.com/how-to-create-faces-automatically-sketchup-create-faces-q-a/',
    'https://designerhacks.com/how-to-quickly-convert-an-autocad-dwg-to-3d-in-sketchup/',
    'https://designerhacks.com/how-to-reduce-sketchup-file-size/',
    'https://designerhacks.com/how-to-import-components-in-the-sketchup-web-app/',
    'https://designerhacks.com/sketchup-scenes-tutorial/',
    'https://designerhacks.com/export-files-from-sketchup-to-stl/',
    'https://designerhacks.com/how-to-make-sketchup-shortcuts/',
    'https://designerhacks.com/install-sketchup/',
    'https://designerhacks.com/polygons-sketchup/',
    'https://designerhacks.com/3d-text-sketchup-create-move-manipulate/',
    'https://designerhacks.com/install-sketchup-plugins-extensions-increase-productivity/',
    'https://designerhacks.com/sketchup2014/',
    'https://designerhacks.com/sketchupgooglemaps/',
    'https://designerhacks.com/find-use-sketchups-dynamic-components/',
    'https://designerhacks.com/get-the-google-sketchup-free-download/',
    'https://designerhacks.com/getting-started-sketchup/',
    'https://designerhacks.com/sketchup-filesize-the-impact-of-groups-and-components/',

    'https://designerhacks.com/how-to-convert-objects-to-low-poly-in-sketchup/',
    'https://designerhacks.com/how-to-make-windows-in-sketchup/',
    'https://designerhacks.com/how-to-model-ikea-furniture-in-sketchup/',
    'https://designerhacks.com/getting-rid-of-ghosting-lines-in-sketchup/',
    'https://designerhacks.com/how-to-design-a-sloped-wall-in-sketchup/',
    'https://designerhacks.com/how-to-draw-lines-on-terrain-sketchup-tutorial/',
    'https://designerhacks.com/creating-a-curved-cutout-in-sketchup-sketchup-qa/',
    'https://designerhacks.com/creating-engraved-or-embedded-text-in-sketchup/',
    'https://designerhacks.com/how-to-make-an-angled-cut-in-sketchup-sketchup-q-a/',
    'https://designerhacks.com/how-to-import-and-edit-stl-files-in-sketchup/',
    'https://designerhacks.com/saki-house-sketchup-speed-model-lumion-9-render/',
    'https://designerhacks.com/how-to-soften-edges-and-round-corners-in-sketchup/',
    'https://designerhacks.com/how-to-create-domes-in-sketchup/',
    'https://designerhacks.com/sketch-floor-plan-to-3d-in-sketchup/',
    'https://designerhacks.com/from-concept-to-3d-in-sketchup/',
    'https://designerhacks.com/7-of-the-best-sketchup-plugins/',
    'https://designerhacks.com/how-to-align-objects-in-sketchup-the-easy-way/',
    'https://designerhacks.com/how-to-create-a-sphere-in-sketchup/',
    'https://designerhacks.com/how-to-push-pull-curved-surfaces-in-sketchup/',
    'https://designerhacks.com/how-to-generate-a-contour-map-with-sketchup/',
    'https://designerhacks.com/how-to-change-units-in-sketchup/',
    'https://designerhacks.com/how-to-import-a-dwg-to-sketchup-without-pro/',
    'https://designerhacks.com/how-to-use-the-sketchup-follow-me-tool/',
    'https://designerhacks.com/how-to-export-a-dwg-from-sketchup/',
    'https://designerhacks.com/sketchup-unfold/',
    'https://designerhacks.com/5-quick-tips-to-getting-started-with-sketchup-layout/',
    'https://designerhacks.com/sketchup-complex-curves/',
    'https://designerhacks.com/simple-ways-customize-sketchup-images-every-design/',
    'https://designerhacks.com/avoid-sketchup-bug-splat/',
    'https://designerhacks.com/embed-sketchup-models-3dwarehouse-onto-portfolio-site/',
    'https://designerhacks.com/import-sketchup-textures-create-custom-materials/',
    'https://designerhacks.com/create-sphere-dome-curved-shape-sketchup/',
    'https://designerhacks.com/setup-photo-matching-sketchup/',
    'https://designerhacks.com/5-essential-sketchup-plugins/',
    'https://designerhacks.com/5-reasons-creating-local-sketchup-library/'

    'https://designerhacks.com/how-to-create-a-beautiful-line-rendering-with-sketchup-and-vray/',
    'https://designerhacks.com/7-ways-to-make-money-with-sketchup/',
    'https://designerhacks.com/futuristic-sketchup-interior-design-sketchup-speed-model-lumion-9-render/',
    'https://designerhacks.com/moon-house-sketchup-speed-model/',
    'https://designerhacks.com/dealing-with-sketchup-error-number-of-segments-too-large/',
    'https://designerhacks.com/how-to-add-texture-to-a-curved-surface-in-sketchup/',
    'https://designerhacks.com/how-to-create-realistic-grass-with-vray-in-sketchup/',
    'https://designerhacks.com/creating-a-parametric-design-in-sketchup-with-viz-pro/',
    'https://designerhacks.com/how-to-get-area-calculations-in-sketchup/',
    'https://designerhacks.com/how-to-import-from-blender-to-sketchup/',
    'https://designerhacks.com/using-sketchup-for-architecture-design-workflow/',
    'https://designerhacks.com/how-to-turn-2d-typography-or-a-survey-to-3d-terrain-in-sketchup/',
    'https://designerhacks.com/how-to-create-sketchup-topography/',
    'https://designerhacks.com/how-to-3d-model-from-a-photo-sketchup/',
    'https://designerhacks.com/5-unconventional-sketchup-tips-might-know/',
    'https://designerhacks.com/speedupsketchup/'
    # Add more URLs here
]

# Directory to save the scraped content
books_dir = os.path.join(current_dir, 'books')  # Create a directory for the books
os.makedirs(books_dir, exist_ok=True)  # Ensure the directory exists
jsonl_path = os.path.join(books_dir, 'combined_scraped_content.json')

# Function to clean text by removing unwanted Unicode escape sequences and line breaks
def clean_text(text):
    text = re.sub(r'\\u[0-9a-fA-F]{4}', '', text)  # Removes Unicode escapes
    text = text.replace('\\n\\n', ' ')  # Replace double newlines with a space
    text = text.replace('\n', ' ')  # Replace single newlines with a space
    text = text.replace('\n\n', ' ')  # Replace double newlines with a space
    text = re.sub(r'\\', '', text)  # Removes stray backslashes
    return text.strip()  # Remove leading/trailing whitespace

# Function to scrape the website and extract instruction-response pairs
def scrape_website_to_jsonl(url):
    # Fetch the webpage content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the <section> with id "main" and class "fullwidth"
    main_section = soup.find('section', {'id': 'main', 'class': 'fullwidth'})

    if not main_section:
        print(f"Main section not found for {url}. Skipping...")
        return None

    # Initialize instruction and response variables
    instruction = None
    response_content = []
    started_scraping = False

    # Collect text from headers and paragraphs
    for element in main_section.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']):
        if element.name == 'h1' and not started_scraping:
            # Use the first <h1> as the instruction
            instruction = element.get_text(strip=True)
            started_scraping = True
        elif started_scraping:
            # Collect the rest of the content as the response
            response_content.append(element.get_text(strip=True))

    if not instruction:
        print(f"No valid instruction (header) found for {url}. Skipping...")
        return None

    # Combine the response content and clean it
    response = clean_text(' '.join(response_content))
    return {"instruction": instruction, "response": response}

# Function to scrape multiple URLs and save content in JSONL format
def scrape_and_save_to_jsonl(urls, jsonl_path):
    with open(jsonl_path, 'w', encoding='utf-8') as f:
        for url in urls:
            print(f"Scraping URL: {url}")
            scraped_content = scrape_website_to_jsonl(url)
            if scraped_content:
                # Write each instruction-response pair as a JSON object in JSONL format
                f.write(json.dumps(scraped_content, ensure_ascii=False) + '\n')
            else:
                print(f"Failed to scrape {url}.")

# Main function to scrape URLs and save to JSONL
def scrape_all_to_jsonl():
    # Scrape all URLs into a single JSONL file
    scrape_and_save_to_jsonl(urls, jsonl_path)

    print(f"All scraped content has been saved to {jsonl_path}")

# Run the script
scrape_all_to_jsonl()
