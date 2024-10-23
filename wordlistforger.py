import itertools
from datetime import datetime
from tqdm import tqdm  # For progress indicators
import sys
import random
import colorama  # For colored terminal text
from colorama import Fore
import pyfiglet  # For ASCII art
import inquirer  # For interactive prompts
import os        # For file operations
import math
import gc        # For garbage collection

# Initialize colorama
colorama.init(autoreset=True)

# Ensure Unicode support
sys.stdout.reconfigure(encoding='utf-8')

# Leet substitutions with essential characters
leet_substitutions = {
    'a': ['a', '@', '4'],
    'e': ['e', '3'],
    'i': ['i', '1', '!'],
    'o': ['o', '0'],
    's': ['s', '$', '5'],
    't': ['t', '7'],
    'g': ['g', '9'],
    'b': ['b', '8'],
    'z': ['z', '2'],
    'l': ['l', '1', '|'],
    'n': ['n'],
    'c': ['c'],
    'u': ['u'],
    'm': ['m'],
}

def leet_variations(word):
    letters = [leet_substitutions.get(char.lower(), [char]) for char in word]
    # Use a generator expression instead of a list
    return (''.join(combo) for combo in itertools.product(*letters))

def apply_variations(word):
    """
    Apply leet substitutions first, then case variations using generators.
    """
    variations = set()
    # Generate leet substitutions
    leet_words = leet_variations(word)
    # Apply case variations to each leet word
    for leet_word in leet_words:
        variations.update({
            leet_word,
            leet_word.lower(),
            leet_word.upper(),
            leet_word.capitalize()
        })
    return variations  # Return a set directly

def generate_numbers_from_date_range(start_year, end_year):
    """
    Generate numbers based on a date range.
    """
    return [str(year) for year in range(start_year, end_year + 1)]

def generate_passwords_with_patterns(words, numbers, special_chars, patterns, min_length, max_length, custom_charset=None, wordlist=set()):
    elements = {
        'W': words or [''],
        'N': numbers or [''],
        'S': special_chars or [''],
        'C': custom_charset or ['']
    }

    total_patterns = len(patterns)
    MAX_COMBINATIONS = 1_000_000  # Adjust as needed

    for pattern in patterns:
        pattern = pattern.strip()
        pattern_sequence = []
        i = 0
        while i < len(pattern):
            if pattern[i] == '{':
                end = pattern.find('}', i)
                if end == -1:
                    print(f"{Fore.RED}Invalid pattern detected: {pattern}")
                    break
                key = pattern[i+1:end].strip()
                if key not in elements:
                    print(f"{Fore.RED}Invalid placeholder '{key}' in pattern: {pattern}")
                    break
                pattern_sequence.append(elements[key])
                i = end + 1
            else:
                pattern_sequence.append([pattern[i]])
                i += 1
        else:
            if not pattern_sequence:
                continue
            try:
                total_combinations = math.prod(len(seq) for seq in pattern_sequence)
            except OverflowError:
                print(f"{Fore.YELLOW}Skipping pattern '{pattern}' due to excessive combinations.")
                continue
            if total_combinations > MAX_COMBINATIONS:
                print(f"{Fore.YELLOW}Skipping pattern '{pattern}' due to excessive combinations ({total_combinations}).")
                continue
            # Use a generator expression to avoid storing all combinations in memory
            combinations = itertools.product(*pattern_sequence)
            for combo in combinations:
                password = ''.join(combo)
                if min_length <= len(password) <= max_length:
                    wordlist.add(password)
    return wordlist

def save_wordlist(wordlist, filename="wordlist.txt"):
    with open(filename, "w", encoding='utf-8') as f:
        for word in sorted(wordlist):
            f.write(f"{word}\n")
    print(f"{Fore.GREEN}Wordlist saved to {filename}")

def create_wordlist():
    # ASCII Art for Welcome Message using pyfiglet
    ascii_banner = pyfiglet.figlet_format("Wordlist Forger", font="slant")
    print(f"{Fore.CYAN}{ascii_banner}")
    print(f"{Fore.YELLOW}Wordlist Forger - A Powerful Tool for Cybersecurity Professionals")
    print(f"{Fore.MAGENTA}Version: 1.0.0")
    print(f"{Fore.MAGENTA}Author: Dennis Sepede (Cybersecurity Specialist)")
    print(f"{Fore.MAGENTA}GitHub: https://github.com/Den-Sec")
    print(f"{Fore.MAGENTA}Contact: dennisepede@proton.me\n")
    print(f"{Fore.CYAN}This tool generates highly customizable and efficient wordlists for use in password cracking techniques,")
    print(f"such as dictionary attacks and advanced scenarios requiring custom patterns.")
    print(f"It supports features like leet speak variations, special character combinations,")
    print(f"and efficient processing to handle large-scale wordlist creation.\n")
    print(f"{Fore.RED}DISCLAIMER:")
    print(f"This tool is intended for educational purposes and authorized penetration testing only.")
    print(f"Unauthorized use of this tool is prohibited. The author is not responsible for any misuse,")
    print(f"illegal activity, or damage caused by this tool. Ensure you have explicit permission to test")
    print(f"any system you use this tool on.\n")
    print(f"{Fore.GREEN}By using this tool, you agree to use it responsibly and abide by all applicable laws and regulations.\n")
    print(f"{Fore.YELLOW}Note: Use this tool ethically and with caution.\n")

    # Gather user input
    wordlist = set()
    flat_words, numbers, special_chars, patterns, min_length, max_length, custom_charset = gather_user_input()

    # Generate passwords
    print(f"\n{Fore.YELLOW}Generating passwords, please wait...")
    wordlist = generate_passwords_with_patterns(
        flat_words,
        numbers,
        special_chars,
        patterns,
        min_length,
        max_length,
        custom_charset,
        wordlist=wordlist
    )

    print(f"\n{Fore.GREEN}Total generated passwords: {len(wordlist)}")

    save_choice = inquirer.prompt([
        inquirer.List('save', message="Do you want to save this wordlist to a file?", choices=['Yes', 'No'])
    ])['save']

    if save_choice == "Yes":
        filename = input(f"{Fore.CYAN}Enter the filename (default is wordlist.txt): ").strip()
        if not filename:
            filename = "wordlist.txt"
        save_wordlist(wordlist, filename)
    else:
        print(f"{Fore.YELLOW}Wordlist generation complete without saving.")

    # Release memory by deleting large variables and invoking garbage collector
    del wordlist
    del flat_words
    del numbers
    del special_chars
    del patterns
    del custom_charset
    gc.collect()

def gather_user_input():
    # Gather user input with interactive prompts
    responses = inquirer.prompt([
        inquirer.Text('inputs', message="Enter basic words (separated by spaces):"),
        inquirer.Text('special_chars', message="Enter special characters (separated by spaces):"),
        inquirer.Text('numbers', message="Enter numbers (separated by spaces):"),
        inquirer.Confirm('date_range_choice', message="Do you want to generate numbers based on a date range?", default=False)
    ])

    inputs = responses['inputs'].split()
    special_chars = responses['special_chars'].split()
    numbers = responses['numbers'].split()

    if responses['date_range_choice']:
        date_range_responses = inquirer.prompt([
            inquirer.Text('start_year', message="Enter the start year (e.g., 1980):"),
            inquirer.Text('end_year', message="Enter the end year (e.g., 2025):")
        ])
        start_year = int(date_range_responses['start_year'])
        end_year = int(date_range_responses['end_year'])
        date_range_numbers = generate_numbers_from_date_range(start_year, end_year)
        numbers.extend(date_range_numbers)
        print(f"{Fore.GREEN}Added years from {start_year} to {end_year} to numbers.")

    length_responses = inquirer.prompt([
        inquirer.Text('min_length', message="Specify minimum password length:"),
        inquirer.Text('max_length', message="Specify maximum password length:")
    ])
    min_length = int(length_responses['min_length'])
    max_length = int(length_responses['max_length'])

    charset_choice = inquirer.prompt([
        inquirer.Confirm('charset_choice', message="Do you want to specify a custom character set?", default=False)
    ])['charset_choice']

    custom_charset = None
    if charset_choice:
        custom_charset = list(inquirer.prompt([
            inquirer.Text('custom_charset', message="Enter the characters (e.g., abcdef123):")
        ])['custom_charset'])

    # Include current date components
    current_year = str(datetime.now().year)
    current_month = f"{datetime.now():%m}"
    current_day = f"{datetime.now():%d}"
    numbers.extend([current_year, current_month, current_day])

    # Apply variations to input words
    words_with_variations = set()
    for word in tqdm(inputs, desc="Applying variations to words"):
        words_with_variations.update(apply_variations(word))
    flat_words = list(words_with_variations)

    # Only include placeholders with non-empty elements
    placeholders = []
    if flat_words:
        placeholders.append('W')
    if numbers:
        placeholders.append('N')
    if special_chars:
        placeholders.append('S')
    if custom_charset:
        placeholders.append('C')

    if not placeholders:
        print(f"{Fore.RED}No valid placeholders available. Exiting.")
        sys.exit(1)

    max_pattern_length = int(inquirer.prompt([
        inquirer.Text('max_pattern_length', message="Enter maximum pattern length (number of placeholders to combine):")
    ])['max_pattern_length'])

    # Generate patterns
    patterns = []
    for length in range(1, max_pattern_length + 1):
        for combo in itertools.product(placeholders, repeat=length):
            # Avoid patterns that could cause excessive combinations
            if combo.count('W') <= 1:
                patterns.append(''.join(f'{{{p}}}' for p in combo))

    print(f"{Fore.GREEN}Generated {len(patterns)} patterns automatically.")

    return flat_words, numbers, special_chars, patterns, min_length, max_length, custom_charset

if __name__ == "__main__":
    try:
        create_wordlist()
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"{Fore.RED}An error occurred: {e}")
        sys.exit(1)
