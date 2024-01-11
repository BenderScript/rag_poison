# GenAI RAG Poison URL Safety Check Program

## Overview
This Python program checks URLs for safety using a few techniques:

* the Google Safe Browsing API
* Abuse.ch database

For demo purposes it fetches the top 100 URLs from Wikipedia and evaluates each for threats like malware, social engineering, unwanted software, and potentially harmful applications.


## Features
- Integration with Google Safe Browsing API.
- Extraction of URLs from an HTML table.
- Assessment of URLs for various threat types.
- Reporting on potential threats or confirming safety.

## Prerequisites
- Python 3.11

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/BenderScript/rag_poison
   ```
2. Navigate to the cloned directory:
   ```bash
   cd rag_poison
   ```
3. Install required packages using `pip3`:
   ```bash
   pip3 install -r requirements.txt
   ```

## Configuration
1. Obtain a Google Safe Browsing API key and place it in a `.env` file as `GOOGLE_SAFE_BROWSING_API_KEY`.

## Usage
Run the program with Python 3:
```bash
python3 main.py
```

## Function Descriptions
- `check_url_with_google_safe_browsing(url, api_key)`: Checks a URL against Google's Safe Browsing API and returns matches.
- `run()`: Main function for URL extraction, API key loading, and URL safety checking.

## Error Handling
- Manages non-200 responses from the API.
- Catches exceptions from request failures.

## Contributing
Feel free to contribute! Open an issue or submit a pull request on GitHub.

## License
This project is licensed under the Apache License.

---

