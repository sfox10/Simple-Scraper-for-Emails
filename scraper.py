# Simple Website Scraper for Emails

import urllib.request, urllib.parse, urllib.error, re

url = input('Please enter url to scrape: \n')
fhand = urllib.request.urlopen(url)
for line in fhand:
    lines = line.decode().strip()
    emailscrape = re.findall('\S+@\S+', lines)
    # Later want to add that if regex doesn't match above criteria the if statement begins
    if len(emailscrape) < 0:
        print('No emails found')
        break
    else:
        print(emailscrape)
