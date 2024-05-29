import os
import requests

# Fetch API key from environment variables
api_key = os.getenv("S2_API_KEY")
headers = {
    "x-api-key": api_key
}

# Define the dataset name you want to download
dataset_name = "s2orc"

# Fetch the ID of the latest release
response_latest_release = requests.get('https://api.semanticscholar.org/datasets/v1/release/latest', headers=headers)
latest_release_id = response_latest_release.json()['release_id']
print(f"Latest Releas ID: {latest_release_id}")

# Fetch the download links for the specified dataset in the latest release
response_dataset = requests.get(f'https://api.semanticscholar.org/datasets/v1/release/{latest_release_id}/dataset/{dataset_name}', headers=headers)

# Check if the request was successful
if response_dataset.status_code == 200:
    data = response_dataset.json()
    # Check if the 'files' key exists in the response
    if 'files' in data:
        download_links = data['files']

        # Download the dataset
        # Note: Datasets might be split into multiple parts. Loop through each part and download.
        for idx, link in enumerate(download_links, start=1):
            response = requests.get(link, headers=headers)
            with open(f'{dataset_name}_part{idx}.zip', 'wb') as f:
                f.write(response.content)
            print(f"Downloaded part {idx} of the {dataset_name} dataset.")
        
        print("Download completed!")
    else:
        print("No files found for the specified dataset in the latest release.")
else:
    print(f"Failed to fetch data for the {dataset_name} dataset in the latest release. HTTP status code: {response_dataset.status_code}")
