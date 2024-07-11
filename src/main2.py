import requests
import json

access_token = "BQBTjjPJPOH7yWsu6dgtH1rG9EMMvBnSFyJAMVw6Xk-XEB2J82JWbOgNYd1IFqhM6NIv0m3jdYDlbRmg7c55iNQNY3CQ-XFCPUvDRsuMz9vThu42_Yw"

# Define the URL and headers
url = "https://api.spotify.com/v1/albums/5rcMJNWebtl2r2S18Je1A0?market=BR"
headers = {
    "Authorization": f"Bearer {access_token}"# Replace with your actual token
}

# Perform the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Print the JSON response
    data = response.json()
    print(json.dumps(data, indent=3, sort_keys=True))
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)  # Print the error message if available
