import os

import requests
from dotenv import load_dotenv
from top_100.extract_urls import ExtractUrls


def check_url_with_google_safe_browsing(url, api_key):
    payload = {
        'client': {
            'clientId': "URL Checking",
            'clientVersion': "1.5.2"
        },
        'threatInfo': {
            'threatTypes': ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
            'platformTypes': ["WINDOWS"],
            'threatEntryTypes': ["URL"],
            'threatEntries': [{'url': url}]
        }
    }

    try:
        response = requests.post(
            f'https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}',
            json=payload
        )

        if response.status_code == 200:
            return response.json()  # Return the JSON response if status is 200
        else:
            # Handle non-200 responses
            print(f"Error: Received status code {response.status_code}")
            print("Response content:", response.text)
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


def run():
    # Use the function
    extract = ExtractUrls()
    extract.html_table_to_list()

    load_dotenv(override=True, dotenv_path=".env")  # take environment variables from .env.
    api_key = os.getenv("GOOGLE_SAFE_BROWSING_API_KEY")
    for u in extract.data_list:
        url = u.get('Domainname')
        # url = "http://malware.testing.google.test/testing/malware/"
        resp = check_url_with_google_safe_browsing(url, api_key)
        if resp is None:
            print(f"{url} : Communication error")
        elif not resp:
            print(f"{url} : No threat found")
        else:
            print(f"{url} : {resp.get('matches')[0].get('threatType')}")



run()
