import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich import print

console = Console()

def banner():
    banner_art = """
[bold blue]
╭───────────────────────────────────────────────────────────────────────────────────────────────────────╮  
│                                                                                                       │  
│      █████╗ ██╗     ██╗   ██╗██╗   ██╗███████╗███╗   ██╗ ██████╗  ██████╗ ███╗   ██╗ ██████╗ ███████╗ │  
│     ██╔══██╗██║     ██║   ██║██║   ██║██╔════╝████╗  ██║██╔════╝ ██╔═══╗  ████╗  ██║██╔═══╗  ██╔════╝ │  
│     ███████║██║     ██║   ██║██║   ██║█████╗  ██╔██╗ ██║██║  ███╗██║██╔   ██╗ ██║██║██       ██╗   │  
│     ██╔══██║██║     ██║   ██║██║   ██║██╔══╝  ██║╚██╗██║██║   ██║██║     ║██║╚██╗██║██║      ██╔══╝   │  
│     ██║  ██║███████╗╚██████╔╝╚██████╔╝███████╗██║ ╚████║╚██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝███████╗ │  
│     ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝ │  
│                                                                                                       │  
│       ⚔️  Welcome to **ALUVENGEANCE** – The Ultimate Cyber Arsenal by **ALVANOSH JOJO** ⚔️       │
│                                                                                                       │  
╰───────────────────────────────────────────────────────────────────────────────────────────────────────╯

[/bold blue]
"""
    print(banner_art)

def list_tools():
    tools = [
        "alu_domainhunter.py",
        "alu_mailgrab.py",
        "alu_portscanner.py",
        "alu_subbust.py",
        "AluBlast.py",
        "alucrackfile.py",
        "AlvaScanner.py",
        "domain_info.py",
        "alu_wordlist_maker.py"
    ]

    for idx, tool in enumerate(tools, 1):
        print(f"[cyan]{idx}.[/cyan] {tool}")

    print("[cyan]0.[/cyan] Exit")

def menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        banner()
        console.print("[bold yellow]Choose a tool to execute:[/bold yellow]")
        list_tools()

        try:
            choice = input("\nEnter your choice ").strip()

            if choice == "0":
                console.print("[bold red]Exiting...[/bold red]")
                sys.exit()

            tool_files = [
                "alu_domainhunter.py",
                "alu_mailgrab.py",
                "alu_portscanner.py",
                "alu_subbuster.py",
                "AluBlast.py",
                "alucrackfile.py",
                "AlvaScanner.py",
                "domain_info.py",
                "alu_wordlist_maker.py"
            ]

            index = int(choice) - 1
            if 0 <= index < len(tool_files):
                selected_tool = tool_files[index]
                console.print(f"Running {selected_tool}...")
                os.system(f"python {selected_tool}")
                input("\n[bold yellow]Press Enter to return to the main menu...[/bold yellow]")
            else:
                console.print("Invalid option. Try again]")
                input("")

        except KeyboardInterrupt:
            console.print("\nInterrupted by user. Exiting...")
            sys.exit()
        except Exception as e:
            console.print(f"Error {e}")
            input("")

if __name__ == "__main__":
    menu()
