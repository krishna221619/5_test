import argparse
import requests

# Define the argument parser
parser = argparse.ArgumentParser(description="Subdomain enumeration")
parser.add_argument("-u", "--url", help="Target domain", required=True)
parser.add_argument("-w", "--wordlist", help="Path to wordlist", required=True)
args = parser.parse_args()

# Read the wordlist into a list
with open(args.wordlist, "r") as f:
    wordlist = [line.strip() for line in f]

# Loop through the wordlist and try each subdomain
for subdomain in wordlist:
    # Construct the URL for the current subdomain
    url = f"http://{subdomain}.{args.url}"

    # Send a GET request to the URL
    try:
        response = requests.get(url, timeout=5)

        # If the response status code is 200, print the URL
        if response.status_code == 200:
            print(url)

    except requests.exceptions.RequestException as e:
        pass
