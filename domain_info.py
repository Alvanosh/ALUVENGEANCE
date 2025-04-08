import nmap
import time
import os
import sys

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[92m" + "="*50)
    print("🛡️  ALVASCANNER - Nmap Powered Network Scanner 🛡️")
    print("         Created by Alvanosh Jojo ")
    print("="*50 + "\033[0m\n")

def get_target():
    print("\n[+] Choose your scan mode:")
    print("1. Scan a single target")
    print("2. Scan a range of IPs")
    choice = input(">> Enter choice (1/2): ").strip()
    
    if choice == "1":
        return input("\n[+] Enter target IP or domain: ").strip()
    elif choice == "2":
        return input("\n[+] Enter IP range (e.g., 192.168.1.1-50): ").strip()
    else:
        print("\n[-] Invalid option. Try again.")
        return get_target()

def get_port_choice():
    print("\n[+] Select Port Scan Type:")
    print("1. Common Ports Scan (Top 1000 ports)")
    print("2. Full Port Scan (All 65535 ports)")
    print("3. Custom Port Range (e.g., 20-100)")
    choice = input(">> Enter choice (1/2/3): ").strip()

    if choice == "1":
        return ""
    elif choice == "2":
        return "-p-"
    elif choice == "3":
        ports = input(">> Enter custom port range: ").strip()
        return f"-p {ports}"
    else:
        print("\n[-] Invalid option. Try again.")
        return get_port_choice()

def get_output_path():
    save = input("\n[?] Do you want to save the scan results? (y/n): ").strip().lower()
    if save == "y":
        filename = input(">> Enter output file name (without extension): ").strip()
        return filename + ".txt"
    return None

def run_scan(target, port_args, output_file):
    scanner = nmap.PortScanner()

    print("\n[~] Starting scan...")
    start_time = time.time()

    try:
        scanner.scan(hosts=target, arguments=f"-sS {port_args} -T4")
    except Exception as e:
        print(f"\n[!] Scan failed: {e}")
        return

    duration = round(time.time() - start_time, 2)
    print(f"\n✅ Scan completed in {duration} seconds.\n")

    output = ""

    for host in scanner.all_hosts():
        output += f"\nHost: {host} ({scanner[host].hostname()})\n"
        output += f"State: {scanner[host].state()}\n"
        if 'tcp' in scanner[host]:
            for port in sorted(scanner[host]['tcp']):
                state = scanner[host]['tcp'][port]['state']
                name = scanner[host]['tcp'][port]['name']
                output += f"  Port: {port}\tState: {state}\tService: {name}\n"
        else:
            output += "No TCP ports found.\n"

    print(output)

    if output_file:
        try:
            with open(output_file, "w") as f:
                f.write(output)
            print(f"\n📁 Scan results saved to: {output_file}")
        except Exception as e:
            print(f"\n[!] Error saving file: {e}")

def main():
    banner()
    target = get_target()
    port_args = get_port_choice()
    output_file = get_output_path()
    run_scan(target, port_args, output_file)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Scan interrupted by user. Exiting...")
        sys.exit(0)
