import requests
import sys
import argparse
parameter=input("Enter Parameter: ")
# Define function to check if website is vulnerable to SQL injection
def check_sql_injection(url, payloads):
    # Loop through each payload and test the website
    for payload in payloads:
        # Send an HTTP request with the payload included in the URL parameter
        response = requests.get(url + "?"+parameter+"=" + payload)

        # Check the response for the payload and a corresponding error message
        if "error" in response.text.lower() and payload in response.text:
            print("The website may be vulnerable to SQL injection with payload:", payload)
        else:
            print("The website does not appear to be vulnerable to SQL injection with payload:", payload)

# Define the argument parser
parser = argparse.ArgumentParser(description="Test website for SQL injection vulnerability")
parser.add_argument("-u", "--url", help="URL of the website", required=True)
parser.add_argument("-w", "--wordlist", help="Filename of payload wordlist", required=True)
args = parser.parse_args()

# Check if the user passed the -h argument for help
if "-h" in sys.argv:
    print("Usage: python sql_tester.py -u [URL] -w [payload_file]")
    print("Example: python sql_tester.py -u https://www.example.com -w payloads.txt")
    sys.exit()

# Get the URL of the website and the filename of the payload file from command line arguments
url = "http://"+args.url
payload_file = args.wordlist

# Read the payloads from the specified file
with open(payload_file) as f:
    payloads = f.read().splitlines()

# Call the check_sql_injection function to test the website for SQL injection vulnerabilities
check_sql_injection(url, payloads)
