import requests
from bs4 import BeautifulSoup
import random
import argparse
import os
from pyfiglet import Figlet
from termcolor import colored

def print_welcome_text():
    figlet = Figlet(font='slant')
    banner_text = figlet.renderText('GoobPasta')
    print(colored(banner_text, 'green'))
    print(colored("Copypasta grabber by: GoobSec\n", 'green'))
    print(colored("Shoutout to my Goobs on X(Twitter) @Mad_PicSnaps @Psy_ware @hornruna_\n", 'red'))
def get_random_copypastas(num):
    # Fetch the webpage
    url = "https://c.r74n.com/copypastas"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
    except requests.RequestException as e:
        return [f"Error fetching webpage: {str(e)}"]
    
    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all copypasta elements (they're in <textarea> tags)
    copypastas = soup.find_all('textarea')
    
    # Select random copypastas
    if copypastas:
        num = min(num, len(copypastas))  # Ensure we don't request more than available
        selected_copypastas = random.sample([cp.text.strip() for cp in copypastas], num)
        return selected_copypastas
    else:
        return ["No copypastas found on the page."]

def save_to_file(copypastas, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for i, copypasta in enumerate(copypastas, 1):
                f.write(f"Copypasta {i}:\n")
                f.write(copypasta)
                f.write("\n\n" + "="*50 + "\n\n")
        print(f"\nSaved {len(copypastas)} copypasta(s) to {filename}")
    except Exception as e:
        print(f"Error saving to file: {str(e)}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Fetch random copypastas from c.r74n.com",
        epilog="Example: python3 GoobPasta.py --number 2 --output pastas.txt"
    )
    parser.add_argument('--number', type=int, default=1, choices=[1, 2, 3],
                        help="Number of copypastas to fetch (1-3, default: 1)")
    parser.add_argument('--output', type=str,
                        help="File to save the copypastas to (e.g., copypastas.txt)")
    
    args = parser.parse_args()

    # Print welcome text
    print_welcome_text()

    # Fetch copypastas
    try:
        copypastas = get_random_copypastas(args.number)
        
        # Print copypastas
        for i, copypasta in enumerate(copypastas, 1):
            print(f"\nCopypasta {i}:\n")
            print(copypasta)
            print("\n" + "="*50)

        # Save to file if output is specified
        if args.output:
            save_to_file(copypastas, args.output)
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()