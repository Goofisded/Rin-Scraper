# Rin Scraper

A Python-based web scraper that gathers essential information from websites, including SSL/TLS data, DNS, WHOIS info, robots.txt, social media tags, security.txt, phone numbers, emails, and more!

## Features

- Retrieves **IP Location**, **DNS Records**, and **TXT Records**
- Extracts **Emails**, **Phone Numbers**, and **Social Tags**
- Fetches **robots.txt** and **sitemap.xml**
- **SSL Info** and **TLS Security Check**
- Verifies **HSTS** (HTTP Strict Transport Security) status
- Displays **WHOIS Information** and **Firewall** headers
- Checks **security.txt** and finds **Linked Pages**

## Requirements

Before using the scraper, ensure the following packages are installed:

```bash
requests
beautifulsoup4
urllib3
dnspython
whois
colorama
```

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/web-scraper.git
cd web-scraper
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the scraper

```bash
python main.py
```

## How to Use

1. **Enter the URL**: When prompted, input the URL of the website you want to scrape.
2. **View Results**: The scraper will return detailed information, including DNS servers, emails, phone numbers, security.txt, headers, and more.
3. **Save or Analyze**: Use output for analysis or further development.

## Screenshot

![Capture](https://github.com/user-attachments/assets/fa3c3dad-2b0c-4f3f-85b4-839e0e383391)

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any improvements or bugs you encounter.

## License

This project is licensed under the MIT License.

