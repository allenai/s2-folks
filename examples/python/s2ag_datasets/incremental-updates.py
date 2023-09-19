import requests
import urllib
import os

# Fetch information about the differences in a dataset between two releases
diff_info = requests.get("http://api.semanticscholar.org/datasets/v1/diffs/2023-09-05/to/latest/papers",
                      headers={'X-API-KEY':os.getenv("S2_API_KEY")}).json()
print(f"Differences between {diff_info['start_release']} and {diff_info['end_release']}")


# Process the increments between two releases
for increment in diff_info['diffs']:
    from_release = increment['from_release']
    to_release = increment['to_release']
    update_files = increment['update_files']
    delete_files = increment['delete_files']
    print(f"Increment {from_release} to {to_release} has {len(update_files)} updates files and {len(delete_files)} delete files")
    
    # Download the incremental updates
    urllib.request.urlretrieve(update_files[0], "papers-update-part0.jsonl.gz")
    # etc...
