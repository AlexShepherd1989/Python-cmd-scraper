# Web Scraper

This project is a simple Python web scraper that fetches the HTML code of specified websites and saves it to local files.

## Features
- Fetches HTML pages from configured websites.
- Saves each page as a separate HTML file in the `source` folder.
- Handles connection errors and timeouts.
- Supports proxy usage.

## Project Structure
```
project/
│
├─ Modules/
│  ├─ FileCreator.py       # Function to create HTML files
│  └─ Scraper.py           # Function to scrape websites
│
├─ Config/
│  └─ ScrapConfig.py       # List of websites and proxies
│
├─ source/                 # Folder for saved HTML files
│
└─ main.py                 # Main script to run the scraper
```

## Installation

1. Clone the repository:
```bash
git clone <repository>
cd <project-folder>
```

2. Install dependencies:
```bash
pip install requests
```

## Configuration

- Add website URLs to the `sites` list in `Config/ScrapConfig.py`.
- Optionally, set proxies in the `proxies` dictionary.

```python
sites = [
    "https://example.com",
    "https://example2.com"
]

proxies = {
    "http": "http://user:password@proxyserver:port",
    "https": "http://user:password@proxyserver:port"
}
```

## Usage

Run the main script:
```bash
python main.py
```

After running, HTML pages will be saved in the `source` folder as `index1.html`, `index2.html`, etc.

## Error Handling
- Proxy error: `Proxy failed for <url>, skipping...`
- Connection timeout: `Connection timed out for <url>, skipping`
- Other request errors are printed with details.
