import requests
import re
import socket
import whois
import dns.resolver
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    print(Fore.GREEN + Style.BRIGHT + "\n")
    print("="*60)
    print("   🔍 ALU DOMAIN HUNTER 🔍".center(60))
    print("   Coded by " \
    " ALVANOSH JOJO".center(60))
    print("="*60 + "\n")

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(Fore.YELLOW + f"[+] IP Address: {ip}")
    except Exception as e:
        print(Fore.RED + f"[-] Failed to get IP: {e}")

def get_whois(domain):
    try:
        info = whois.whois(domain)
        print(Fore.CYAN + "[+] WHOIS Information:")
        for key, val in info.items():
            print(f"{key}: {val}")
    except Exception as e:
        print(Fore.RED + f"[-] Failed to get WHOIS: {e}")

def get_dns(domain):
    try:
        print(Fore.MAGENTA + "\n[+] DNS Records:")
        for rtype in ['A', 'MX', 'NS', 'TXT']:
            try:
                records = dns.resolver.resolve(domain, rtype)
                for record in records:
                    print(f"{rtype}: {record.to_text()}")
            except:
                pass
    except Exception as e:
        print(Fore.RED + f"[-] Failed to get DNS: {e}")

def extract_emails_phones(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()

        emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
        phones = re.findall(r'\+?\d[\d\s().-]{7,}\d', text)

        print(Fore.GREEN + "\n[+] Emails Found:")
        for email in set(emails):
            print(f"   📧 {email}")

        print(Fore.BLUE + "\n[+] Phone Numbers Found:")
        for phone in set(phones):
            print(f"   📞 {phone}")

    except Exception as e:
        print(Fore.RED + f"[-] Error scraping {url}: {e}")

def crawl_and_extract(domain):
    base_url = "http://" + domain if not domain.startswith("http") else domain
    try:
        print(Fore.YELLOW + f"\n[+] Extracting from: {base_url}")
        extract_emails_phones(base_url)
    except Exception as e:
        print(Fore.RED + f"[-] Failed to fetch data: {e}")


    except Exception as e:
        print(Fore.RED + f"[-] Failed to crawl: {e}")

def main():
    banner()
    domain = input(Fore.CYAN + "Enter target domain (e.g., example.com): ").strip()
    print("\n" + "="*60)
    get_ip(domain)
    get_whois(domain)
    get_dns(domain)
    crawl_and_extract(domain)
    print("\n" + "="*60)
    print(Fore.GREEN + Style.BRIGHT + "\n✅ yes we did it by  ALVANOSH JOJO\n")

if __name__ == "__main__":
    main()
