import feedparser
import argparse
import re

# Define the argument parser
parser = argparse.ArgumentParser(description="Check for WordPress vulnerabilities")
parser.add_argument("-u", "--url", help="URL of the website", required=True)
parser.add_argument("-w", "--wordlist", help="Wordlist argument to pass to selected file.")
args = parser.parse_args()

# Construct the URL of the RSS feed
rss_url = "https://"+args.url.rstrip('/') + '/feed/'

# Parse the RSS feed
feed = feedparser.parse(rss_url)

if 'generator' in feed.feed:
    # Extract the generator tag
    generator_tag = feed.feed.generator
    # Use regular expressions to extract the version number from the generator tag
    version_number = re.search(r'\d+(\.\d+)+', generator_tag)
    # Print the version number
    if version_number:
        print(f"WordPress version: {version_number.group(0)}")
        # Check if the version has any vulnerabilities
        cve_url = f"https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=wordpress+{version_number.group(0)}"
        cve_feed = feedparser.parse(cve_url)
        if cve_feed.entries:
            print("The current version has the following vulnerabilities:")
            for entry in cve_feed.entries:
                print(f"\t- {entry.title}")
        else:
            print("The current version does not have any known vulnerabilities.")
    else:
        print("Could not find version number in generator tag.")
else:
    # If the RSS feed does not contain a generator tag, print an error message
    print("Could not find generator tag in RSS feed.")
