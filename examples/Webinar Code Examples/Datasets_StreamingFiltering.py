import os
import requests
import json
import gzip

# Fetch API key from environment variables
api_key = os.getenv("S2_API_KEY")
headers = {
    "x-api-key": api_key  # Corrected to use the variable directly
}

# Define the dataset name you want to download and adjust the file name to include the release date
dataset_name = "abstracts"
filter_field = 'abstract'  # Adjusted to filter based on abstract content
filter_value = 'computer'  # Looking for the word 'computer' regardless of case

# Fetch the ID of the latest release
response_latest_release = requests.get('https://api.semanticscholar.org/datasets/v1/release/latest', headers=headers)
latest_release_id = response_latest_release.json()['release_id']
print(f"Latest Release ID: {latest_release_id}")

# Fetch the download links for the specified dataset in the latest release
response_dataset = requests.get(f'https://api.semanticscholar.org/datasets/v1/release/{latest_release_id}/dataset/{dataset_name}', headers=headers)

if response_dataset.status_code == 200:
    data = response_dataset.json()
    if 'files' in data:
        download_links = data['files']

        # Process each file
        for idx, link in enumerate(download_links, start=1):
            file_path = f'{dataset_name}_{latest_release_id}_part{idx}.jsonl'  # Include the release date in the file name
            print(f"Downloading and filtering part {idx} of {dataset_name} to {file_path}...")
            with requests.get(link, headers=headers, stream=True) as response:
                response.raise_for_status()  # Ensure we notice bad responses
                with gzip.open(response.raw, 'rt', encoding='utf-8') as gz:
                    for line in gz:
                        try:
                            data = json.loads(line)
                            # Apply filter with case insensitivity for 'computer' in the abstract
                            if filter_field in data and filter_value.lower() in data[filter_field].lower():
                                with open(file_path, 'a') as f_out:
                                    json.dump(data, f_out)
                                    f_out.write('\n')
                        except json.JSONDecodeung_error as e:
                            print(f"Error decoding JSON: {e}")
            print(f"Filtered part {idx} downloaded and saved to {file_path}.")
        print("All parts downloaded and filtered.")
    else:
        print("No files found for the specified dataset in the latest release.")
else:
    print(f"Failed to fetch data for {dataset_name} in the latest release. HTTP status code: {response_dataset.status_code}")
