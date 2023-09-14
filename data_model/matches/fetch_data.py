import requests
import json
import os
import zipfile

def extract_zip(zip_filepath, output_dir):
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        zip_ref.extractall(output_dir)

def download_and_extract_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_filename = 'match_data.json'
    json_filepath = os.path.join(current_dir, json_filename)

    if os.path.exists(json_filepath):
        print('JSON file already exists:')
        with open(json_filepath, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            print(data)
    else:
        zip_url = 'https://cricsheet.org/downloads/all_json.zip'
        response = requests.get(zip_url)

        if response.status_code == 200:
            zip_filepath = os.path.join(current_dir, 'all_json.zip')
            with open(zip_filepath, 'wb') as zip_file:
                zip_file.write(response.content)

            # Extract the ZIP file
            extract_dir = os.path.join(current_dir, 'extracted')
            os.makedirs(extract_dir, exist_ok=True)
            extract_zip(zip_filepath, extract_dir)

        else:
            print("Download failed", response.status_code)


download_and_extract_data()
