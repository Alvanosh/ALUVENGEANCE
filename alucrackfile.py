import zipfile
from tqdm import tqdm
import os
import time
from termcolor import colored

def banner():
    print(colored("="*50, "green"))
    print(colored("     🔐 ALUCRACKFILE - ZIP BRUTE FORCE TOOL 🔐", "green", attrs=["bold"]))
    print(colored("        BY  ALVANOSH JOJO", "green"))
    print(colored("="*50, "green"))

def crack_zip(zip_path, wordlist_path):
    if not os.path.exists(zip_path):
        print(colored("[!] ZIP file not found!", "red"))
        return

    if not os.path.exists(wordlist_path):
        print(colored("[!] Wordlist file not found!", "red"))
        return

    try:
        zip_file = zipfile.ZipFile(zip_path)
        passwords = open(wordlist_path, 'rb').read().splitlines()

        print(colored(f"[*] Starting brute force on: {zip_path}", "cyan"))
        time.sleep(1)

        for pwd in tqdm(passwords, desc="🔍 Cracking", unit="password"):
            try:
                zip_file.extractall(pwd=pwd)
                print(colored("\n[+] Password Found: " + pwd.decode(), "green", attrs=["bold"]))
                print(colored("💥 YES WE DID IT - BY KORATTYKARAN ALVANOSH JOJO 💥", "green"))
                return
            except:
                continue

        print(colored("\n[-] Password not found in wordlist ❌", "red"))

    except zipfile.BadZipFile:
        print(colored("[!] Not a valid ZIP file!", "red"))

def main():
    banner()
    zip_path = input(colored("[?] Enter path to the password-protected ZIP file: ", "yellow"))
    wordlist_path = input(colored("[?] Enter path to your wordlist (default: rockyou.txt): ", "yellow"))

    if wordlist_path.strip() == "":
        wordlist_path = "rockyou.txt"

    crack_zip(zip_path, wordlist_path)

if __name__ == "__main__":
    main()
