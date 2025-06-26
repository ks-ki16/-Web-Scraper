import requests
from bs4 import BeautifulSoup

# Target URL (can be modified to any public news site)
URL = 'https://www.bbc.com/news'
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def fetch_html(url):
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.text

def parse_headlines(html):
    soup = BeautifulSoup(html, 'html.parser')
    # BBC typically uses <h3> for headlines, but adjust based on the site
    headlines = soup.find_all(['h1', 'h2', 'h3'])
    clean_headlines = [tag.get_text(strip=True) for tag in headlines if tag.get_text(strip=True)]
    return clean_headlines

def save_to_txt(headlines, filename="headlines.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for line in headlines:
            f.write(line + "\n")
    print(f"[+] Saved {len(headlines)} headlines to {filename}")

def main():
    print("[*] Fetching HTML...")
    html = fetch_html(URL)
    print("[*] Parsing headlines...")
    headlines = parse_headlines(html)
    print("[*] Saving headlines to file...")
    save_to_txt(headlines)

if __name__ == "__main__":
    main()
