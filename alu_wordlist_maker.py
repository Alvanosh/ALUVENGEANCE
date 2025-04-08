import itertools
import os

def leet_speak(word):
    leet_map = {'a': '@', 'A': '@', 'e': '3', 'E': '3', 'i': '1', 'I': '1', 'o': '0', 'O': '0', 's': '$', 'S': '$'}
    return ''.join(leet_map.get(char, char) for char in word)

def generate_custom_wordlist(keywords, use_numbers, use_symbols, smart_mode, filename):
    mutations = []

    symbols = ['!', '@', '#', '$', '%']
    numbers = ['123', '1234', '2025', '007']

    for word in keywords:
        mutations.append(word)
        mutations.append(word.lower())
        mutations.append(word.upper())
        mutations.append(word.capitalize())
        if smart_mode:
            mutations.append(leet_speak(word))
    
    final_list = set()

    for word in mutations:
        final_list.add(word)
        if use_numbers:
            for n in numbers:
                final_list.add(word + n)
                final_list.add(n + word)
        if use_symbols:
            for s in symbols:
                final_list.add(word + s)
                final_list.add(s + word)

    # Combine two keywords too
    for a, b in itertools.permutations(mutations, 2):
        combined = a + b
        final_list.add(combined)
        if use_numbers:
            for n in numbers:
                final_list.add(combined + n)
        if use_symbols:
            for s in symbols:
                final_list.add(combined + s)

    with open(filename, 'w') as f:
        for item in final_list:
            f.write(item + '\n')
    
    print(f"\n✅ Wordlist created with {len(final_list)} entries! Saved to: {os.path.abspath(filename)}\n")

def banner():
    print("""
   █████╗ ██╗     ██╗   ██╗    ██╗    ██╗ ██████╗ ██████╗ ██╗     
  ██╔══██╗██║     ██║   ██║    ██║    ██║██╔═══██╗██╔══██╗██║     
  ███████║██║     ██║   ██║    ██║ █╗ ██║██║   ██║██████╔╝██║     
  ██╔══██║██║     ██║   ██║    ██║███╗██║██║   ██║██╔═══╝ ██║     
  ██║  ██║███████╗╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║     ███████╗
  ╚═╝  ╚═╝╚══════╝ ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝     ╚══════╝
          🔒 alu_wordlist_maker.py by KORATTYKARAN ALVANOSH JOJO 🔒
    """)

def main():
    banner()

    print("🔧 CUSTOM WORDLIST MAKER v1.0 🔧\n")

    keywords = input("Enter target keywords (comma-separated): ").split(',')
    keywords = [k.strip() for k in keywords if k.strip() != '']

    use_numbers = input("Include common numbers? (1 = yes, 0 = no): ") == '1'
    use_symbols = input("Include symbols? (1 = yes, 0 = no): ") == '1'
    smart_mode = input("Enable smart leet mode? (1 = yes, 0 = no): ") == '1'
    filename = input("Enter filename to save (e.g., wordlist.txt): ").strip()
    if filename == "":
        filename = "alu_wordlist.txt"

    generate_custom_wordlist(keywords, use_numbers, use_symbols, smart_mode, filename)

if __name__ == "__main__":
    main()
