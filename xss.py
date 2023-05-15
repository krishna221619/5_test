import requests
import argparse
parameter=input("Enter Parameter: ")
# Define the argument parser
parser = argparse.ArgumentParser(description="Test a website for XSS vulnerability using payloads from a file")
parser.add_argument("-u", "--url", help="URL of the website", required=True)
parser.add_argument("-w", "--wordlist", help="File containing XSS payloads", required=True)
args = parser.parse_args()

# Get the URL of the website from the command line argument
url = "http://"+args.url

# Read the payloads from the file specified in the command line argument
with open(args.wordlist) as f:
    payloads = f.read().splitlines()

# Loop through each payload and test the website
for payload in payloads:
    # Send an HTTP request with the payload included in the URL parameter
    response = requests.get(url + "/?"+parameter+"=" + payload)

    # Check the response for the payload and a corresponding alert box
    if payload in response.text and "<script>" + payload + "</script>" in response.text:
        print("The website may be vulnerable to XSS with payload:", payload)
    else:
        print("The website does not appear to be vulnerable to XSS with payload:", payload)
