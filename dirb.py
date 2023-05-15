import argparse
import requests

# Define the argument parser
parser = argparse.ArgumentParser(description="Directory buster")
parser.add_argument("-u", "--url", help="Target URL", required=True)
parser.add_argument("-w", "--wordlist", help="Path to wordlist", required=True)
args = parser.parse_args()

# Read the wordlist into a list
with open(args.wordlist, "r") as f:
    wordlist = [line.strip() for line in f]

# Check if the URL ends with a slash, and remove it if it does
url = "https://"+args.url.rstrip("/")

# Loop through the wordlist and try each directory
for directory in wordlist:
    # Construct the URL for the current directory
    directory_url = f"{url}/{directory}"

    # Send a GET request to the directory URL
    response = requests.get(directory_url)

    # If the response status code is 200, print the URL and status code
    if response.status_code == 200:
        print(f"{response.status_code}: {directory_url}")
