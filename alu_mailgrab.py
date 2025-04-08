import requests
from bs4 import BeautifulSoup
import re
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    print(Fore.GREEN + Style.BRIGHT + """
 █████╗ ██╗     ██╗   ██╗    ███╗   ███╗ █████╗ ██╗██╗      ██████╗  █████╗ ██████╗ 
██╔══██╗██║     ██║   ██║    ████╗ ████║██╔══██╗██║██║     ██╔════╝ ██╔══██╗██╔══██╗
███████║██║     ██║   ██║    ██╔████╔██║███████║██║██║     ██║  ███╗███████║██████╔╝
██╔══██║██║     ██║   ██║    ██║╚██╔╝██║██╔══██║██║██║     ██║   ██║██╔══██║██╔═══╝ 
██║  ██║███████╗╚██████╔╝    ██║ ╚═╝ ██║██║  ██║██║███████╗╚██████╔╝██║  ██║██║     
╚═╝  ╚═╝╚══════╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     
                                                                                  
                   📧 alu_mailgrab - Email Harvester by ALVANOSH JOJO 🚀
""")

def extract_emails(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()
            email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
            emails = re.findall(email_pattern, text)
            return list(set(emails))  # remove duplicates
        else:
            print(Fore.RED + f"[-] Failed to fetch the page. Status code: {response.status_code}")
            return []
    except Exception as e:
        print(Fore.RED + f"[-] Error: {e}")
        return []

def main():
    banner()
    url = input(Fore.CYAN + "[+] Enter the full URL (e.g. https://example.com): ")
    print(Fore.YELLOW + "[*] Collecting emails...")

    emails = extract_emails(url)

    if emails:
        print(Fore.GREEN + f"[+] Found {len(emails)} email(s):")
        for email in emails:
            print(Fore.LIGHTWHITE_EX + "   ➤ " + email)
        with open("emails_found.txt", "w") as f:
            for email in emails:
                f.write(email + "\n")
        print(Fore.GREEN + "\n[✓] Emails saved to emails_found.txt")
    else:
        print(Fore.RED + "[-] No emails found on the page.")

    print(Fore.LIGHTGREEN_EX + "\n✅ YES WE DID IT BY  ALVANOSH JOJO 💚🔥")

if __name__ == "__main__":
    main()
