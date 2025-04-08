import dns.resolver
import threading
from colorama import Fore, Style, init

init(autoreset=True)

# ✅ Default wordlist
wordlist = [
    "www", "mail", "ftp", "cpanel", "webmail", "admin", "test", "dev",
    "api", "vpn", "ns1", "ns2", "portal", "db", "server", "login"
]

# ✅ Result list
found_subdomains = []

# ✅ Print ALU badge
def banner():
    print(Fore.GREEN + "=" * 60)
    print(Fore.GREEN + "🛡️  ALU_SUBBUSTER - Subdomain Hunter Tool")
    print(Fore.GREEN + "👑 Created by: ALVANOSH JOJO")
    print(Fore.GREEN + "=" * 60 + "\n")

# ✅ DNS resolver function
def resolve_subdomain(subdomain, domain):
    try:
        full_sub = f"{subdomain}.{domain}"
        answers = dns.resolver.resolve(full_sub, "A")
        for rdata in answers:
            print(Fore.CYAN + f"[+] Found: {full_sub} --> {rdata}")
            found_subdomains.append(f"{full_sub} --> {rdata}")
    except:
        pass  # Silent fail for nonexistent subdomains

# ✅ Main function
def main():
    banner()
    domain = input(Fore.YELLOW + "[?] Enter the domain name (example.com): ").strip()

    print(Fore.MAGENTA + f"\n[~] Scanning subdomains for: {domain}\n")

    threads = []

    for sub in wordlist:
        t = threading.Thread(target=resolve_subdomain, args=(sub, domain))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    print(Fore.GREEN + "\n✅ Scan completed.")
    print(Fore.GREEN + f"📊 Total found: {len(found_subdomains)}")

    # Optionally save
    save = input(Fore.YELLOW + "\n[?] Save results to file? (y/n): ").lower()
    if save == 'y':
        filename = f"subs_{domain.replace('.', '_')}.txt"
        with open(filename, "w") as f:
            for sub in found_subdomains:
                f.write(sub + "\n")
        print(Fore.GREEN + f"[+] Saved to {filename}")

    print(Fore.GREEN + "\n✅ YES WE DID IT MAN!! 💪")

if __name__ == "__main__":
    main()
