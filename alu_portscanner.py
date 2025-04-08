# alu_portscanner.py

import socket
import threading
from datetime import datetime
from termcolor import colored

open_ports = []
lock = threading.Lock()

def print_banner():
    print(colored("╔══════════════════════════════════════╗", "green"))
    print(colored("║         🔥 ALU PORT SCANNER 🔥       ║", "green"))
    print(colored("║          Created by:ALVANOSH JOJO    ║", "green"))
    print(colored("╚══════════════════════════════════════╝\n", "green"))

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            try:
                sock.send(b'HEAD / HTTP/1.0\r\n\r\n')
                banner_data = sock.recv(1024).decode(errors='ignore').strip()
            except:
                banner_data = "No Banner"

            with lock:
                open_ports.append((port, service, banner_data))
                print(colored(f"[OPEN] Port {port} ({service}) - Banner: {banner_data}", "green"))
        sock.close()
    except:
        pass

def start_scan(ip, ports_to_scan):
    threads = []
    for port in ports_to_scan:
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def main():
    print_banner()
    target = input(colored("[+] Enter domain or IP to scan: ", "cyan"))

    try:
        ip = socket.gethostbyname(target)
        print(colored(f"[✓] IP address resolved: {ip}\n", "yellow"))
    except:
        print(colored("[!] Invalid domain or IP", "red"))
        return

    print(colored("Choose scan type:\n1. Fast (Common ports)\n2. Full (1-1024)\n3. Custom range", "blue"))
    choice = input(colored("Enter choice (1/2/3): ", "magenta"))

    if choice == '1':
        ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3306, 8080, 8443]
    elif choice == '2':
        ports_to_scan = list(range(1, 1025))
    elif choice == '3':
        start = int(input(colored("Start port: ", "cyan")))
        end = int(input(colored("End port: ", "cyan")))
        ports_to_scan = list(range(start, end + 1))
    else:
        print(colored("[!] Invalid choice. Exiting.", "red"))
        return

    print(colored(f"\n[+] Starting scan on {ip} ...", "yellow"))
    start_time = datetime.now()
    start_scan(ip, ports_to_scan)
    end_time = datetime.now()
    duration = end_time - start_time
    print(colored(f"\n[✓] Scan complete in {duration}", "cyan"))

    if open_ports:
        save = input(colored("\nDo you want to save the results to a file? (y/n): ", "magenta"))
        if save.lower() == 'y':
            filename = f"scan_report_{target.replace('.', '_')}.txt"
            with open(filename, 'w') as file:
                file.write(f"Scan report for {target} ({ip})\n")
                file.write(f"Scanned on: {datetime.now()}\n\n")
                for port, service, banner in open_ports:
                    file.write(f"Port {port} ({service}) - Banner: {banner}\n")
            print(colored(f"[✓] Results saved to {filename}", "green"))
    else:
        print(colored("[!] No open ports found.", "red"))

    print(colored("\n✅ Yes, we did it! by ALVANOSH JOJO 💪", "green"))

if __name__ == "__main__":
    main()
