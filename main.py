import argparse
import os

# Define the argument parser
parser = argparse.ArgumentParser(description="Execute one of five files with passed arguments.")
parser.add_argument("-u", "--url", help="URL argument to pass to selected file.")
parser.add_argument("-w", "--wordlist", help="Wordlist argument to pass to selected file.")
args = parser.parse_args()

# Define a dictionary to map user input to file paths
file_map = {
    1: "sql.py",
    2: "xss.py",
    3: "wp.py",
    4: "subdomainenum.py",
    5: "dirb.py"
}

# Define a function to execute the selected file with passed arguments
def execute_file(file_path, url, wordlist):
    os.system(f"python {file_path} -u {url} -w {wordlist}")

# Display a menu of options and get user input
print("Select a file to execute:")
print("1. SQL Injection")
print("2. Xss ")
print("3. Wordpress Scanner")
print("4. Subdomain Enumeration")
print("5. Directory Busting")
choice = int(input("> "))

# Execute the selected file with passed arguments
if choice in file_map:
    file_path = file_map[choice]
    execute_file(file_path, args.url, args.wordlist)
else:
    print("Invalid choice.")
