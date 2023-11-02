import os
import requests
import json

def main():
    # Fetch API key from environment variables
    api_key = os.getenv("S2_API_KEY")
    if not api_key:
        print("S2_API_KEY environment variable not set.")
        return

    headers = {
        "x-api-key": api_key
    }

    # Fetch the ID of the latest release
    response_latest_release = requests.get('https://api.semanticscholar.org/datasets/v1/release/latest', headers=headers)
    if response_latest_release.status_code == 200:
        latest_release_id = response_latest_release.json()['release_id']
        print(f"Latest Release ID: {latest_release_id}")

        # Define the dataset name you want to download
        dataset_name = "s2orc"
        
        # Fetch the download links for the specified dataset in the latest release
        response_dataset = requests.get(f'https://api.semanticscholar.org/datasets/v1/release/{latest_release_id}/dataset/{dataset_name}', headers=headers)
        if response_dataset.status_code == 200:
            dataset_info = response_dataset.json()
            print(json.dumps(dataset_info, indent=2))  # This will print out the full response body
            
            download_links = dataset_info.get('download_links', [])
            if download_links:
                print("Download Links:")
                for link in download_links:
                    print(link['url'])
            else:
                print("No download links found for the dataset. Here's the response content for debugging:")
                print(json.dumps(dataset_info, indent=2))  # Print the whole JSON response for debugging
        else:
            print(f"Failed to get download links for the dataset. Status Code: {response_dataset.status_code}")
            print("Response:", response_dataset.text)
    else:
        print(f"Failed to fetch latest release ID. Status Code: {response_latest_release.status_code}")
        print("Response:", response_latest_release.text)

if __name__ == "__main__":
    main()
