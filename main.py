import requests
import ssl
import socket
import urllib3
import bs4
import re
import dns.resolver
import whois
import time
from colorama import Fore, Style, init
from urllib.parse import urljoin, urlparse


init(autoreset=True)

def print_banner():
    banner = """
    ██████╗ ██╗███╗   ██╗
    ██╔══██╗██║████╗  ██║
    ██████╔╝██║██╔██╗ ██║
    ██╔══██╗██║██║╚██╗██║
    ██║  ██║██║██║ ╚████║
    ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ 

    Discord: Goofisdead
    """
    print(Fore.CYAN + banner + Style.RESET_ALL)

def get_ip_location(url):
    try:
        domain = re.findall(r'(?<=://)[^/]+', url)[0]  # Extract domain from URL
        ip_address = socket.gethostbyname(domain)
        location_data = requests.get(f"http://ipinfo.io/{ip_address}/json").json()
        return location_data
    except Exception as e:
        return f"Error: {e}"

def get_ssl_info(url):
    try:
        parsed_url = urllib3.util.parse_url(url)
        context = ssl.create_default_context()
        with urllib3.PoolManager(ssl_context=context) as http:
            response = http.request("GET", parsed_url.host)
            return response.headers.get("Server"), response.headers.get("X-Powered-By")
    except Exception as e:
        return f"Error: {e}"

def get_emails(url):
    try:
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.content, "html.parser")
        email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
        emails = email_pattern.findall(response.text)
        return emails if emails else "Not Found"
    except Exception as e:
        return f"Error: {e}"

def get_phone_numbers(url):
    try:
        response = requests.get(url)
        phone_pattern = re.compile(r"\+?\d[\d -]{8,14}\d")
        phone_numbers = phone_pattern.findall(response.text)
        return phone_numbers if phone_numbers else "Not Found"
    except Exception as e:
        return f"Error: {e}"

def get_security_txt(url):
    try:
        response = requests.get(url + "/.well-known/security.txt")
        if response.status_code == 200:
            return response.text
        else:
            return "Security.txt file not found."
    except Exception as e:
        return f"Error: {e}"

def get_dns_server(domain):
    try:
        resolver = dns.resolver.Resolver()
        answers = resolver.resolve(domain, 'A')
        dns_ips = [answer.to_text() for answer in answers]
        return dns_ips if dns_ips else "DNS records not found."
    except Exception as e:
        return f"Error: {e}"

def get_firewall(url):
    try:
        response = requests.get(url)
        headers = response.headers
        return headers.get("X-Frame-Options", "X-Frame-Options header not found.")
    except Exception as e:
        return f"Error: {e}"

def get_whois_info(domain):
    try:
        whois_info = whois.whois(domain)
        return whois_info
    except Exception as e:
        return f"Error: {e}"

def get_robots_txt(url):
    try:
        response = requests.get(url + "/robots.txt")
        if response.status_code == 200:
            return response.text
        else:
            return "robots.txt file not found."
    except Exception as e:
        return f"Error: {e}"

def get_sitemap(url):
    try:
        response = requests.get(url + "/sitemap.xml")
        if response.status_code == 200:
            return response.url
        else:
            return "Sitemap not found."
    except Exception as e:
        return f"Error: {e}"

def get_txt_records(domain):
    try:
        resolver = dns.resolver.Resolver()
        answers = resolver.resolve(domain, 'TXT')
        txt_records = [answer.to_text() for answer in answers]
        return txt_records if txt_records else "TXT records not found."
    except Exception as e:
        return f"Error: {e}"

def get_linked_pages(url):
    try:
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.content, "html.parser")
        links = set()
        for link in soup.find_all("a", href=True):
            full_link = urljoin(url, link["href"])
            links.add(full_link)
        return links if links else "No links found."
    except Exception as e:
        return f"Error: {e}"

def get_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        return headers
    except Exception as e:
        return f"Error: {e}"

def get_social_tags(url):
    try:
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.content, "html.parser")
        og_tags = {meta.get("property"): meta.get("content") for meta in soup.find_all("meta", property=True) if "og:" in meta.get("property", "")}
        twitter_tags = {meta.get("name"): meta.get("content") for meta in soup.find_all("meta", {"name": True}) if "twitter:" in meta.get("name", "")}
        return {"Open Graph Tags": og_tags, "Twitter Tags": twitter_tags}
    except Exception as e:
        return f"Error: {e}"

def check_hsts(url):
    try:
        response = requests.get(url)
        if "strict-transport-security" in response.headers:
            return response.headers["strict-transport-security"]
        else:
            return "HSTS not enabled."
    except Exception as e:
        return f"Error: {e}"

def check_tls(url):
    try:
        ssl_info = ssl.get_server_certificate((urlparse(url).hostname, 443))
        return "TLS/SSL Certificate is valid."
    except ssl.SSLError as e:
        return f"TLS/SSL Certificate issue: {e}"

def scrape_website(url):
    domain = re.findall(r'(?<=://)[^/]+', url)[0]  
    results = {}
    results["IP Location"] = get_ip_location(url)
    results["SSL Info"] = get_ssl_info(url)
    results["Emails"] = get_emails(url)
    results["Phone Numbers"] = get_phone_numbers(url)
    results["Security.txt"] = get_security_txt(url)
    results["DNS Server"] = get_dns_server(domain)
    results["TXT Records"] = get_txt_records(domain)
    results["Firewall"] = get_firewall(url)
    results["WHOIS Info"] = get_whois_info(domain)
    results["Robots.txt"] = get_robots_txt(url)
    results["Sitemap"] = get_sitemap(url)
    results["Linked Pages"] = get_linked_pages(url)
    results["Headers"] = get_headers(url)
    results["Social Tags"] = get_social_tags(url)
    results["HSTS Check"] = check_hsts(url)
    results["TLS Security"] = check_tls(url)
    return results


def display_results(results):
    print(Fore.CYAN + "Results:" + Style.RESET_ALL)
    for key, value in results.items():
        if isinstance(value, dict): 
            print(f"{Fore.GREEN}{key}:")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key}: {sub_value}")
        else:
            if isinstance(value, list):
                value = ', '.join(value) if value else 'Not Found'
            print(f"{Fore.GREEN}{key}: {Style.RESET_ALL}{value}")
    
print_banner()
url = input(Fore.YELLOW + "Enter the URL to scrape: " + Style.RESET_ALL)
start_time = time.time()
results = scrape_website(url)
end_time = time.time()

display_results(results)

print(Fore.MAGENTA + f"\nTotal scraping time: {end_time - start_time:.2f} seconds" + Style.RESET_ALL)
