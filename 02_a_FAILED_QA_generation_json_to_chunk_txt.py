
import os
import json
from transformers import T5Tokenizer
from config_scraping_URLs import source_path

# Initialize the tokenizer for T5 (or use your desired model)
tokenizer = T5Tokenizer.from_pretrained('t5-base')

# Function to split text into chunks of a specified token limit
def chunk_text(text, max_length=175):
    # Tokenize the text using the T5 tokenizer
    tokens = tokenizer.encode(text, add_special_tokens=True)
    
    # Split the tokens into chunks of max_length
    chunks = [tokens[i:i + max_length] for i in range(0, len(tokens), max_length)]
    
    # Decode the chunks back into text
    return [tokenizer.decode(chunk, skip_special_tokens=True) for chunk in chunks]

# Function to save content as individual .txt files from a JSON file
def convert_json_to_txt():
    # Define the JSON path and output directory
    json_path = os.path.join(source_path, 'scraped_data.json')  # Path to your JSON file
    txt_output_dir = os.path.join('books', 'txt_files')  # Directory where .txt files will be saved

    # Check if JSON file exists
    if not os.path.exists(json_path):
        print(f"Error: {json_path} does not exist.")
        return
    
    # Create output directory if it doesn't exist
    os.makedirs(txt_output_dir, exist_ok=True)

    # Load data from JSON file
    with open(json_path, 'r', encoding='utf-8') as f:
        scraped_data = json.load(f)

    # Iterate over each entry in the JSON and save it as a .txt file
    for idx, data in enumerate(scraped_data, start=1):
        content = data['content']
        
        # Split the content into chunks if it exceeds the token limit
        content_chunks = chunk_text(content)

        # Save each chunk as a separate .txt file
        for chunk_idx, chunk in enumerate(content_chunks, start=1):
            file_name = f"scraped_content_{idx}_chunk_{chunk_idx}.txt"
            file_path = os.path.join(txt_output_dir, file_name)

            # Write the chunk to the .txt file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(chunk)

            print(f"Saved chunk {chunk_idx} of document {idx} to {file_path}")

# Call the function to convert JSON to txt files
convert_json_to_txt()

