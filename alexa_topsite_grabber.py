# Jeffrey Gray
# alexa_topsite_grabber.py
# takes user input to determine number of sites to rip from Alexa website [http://www.alexa.com/topsites/global]

import urllib.request
import re
from math import ceil

# relevant data determined by user input
n = int(input('Number of sites to load: '))
pages_to_load = int(ceil(n/25.0))

raw_url = str('http://www.alexa.com/topsites/global;')  # url to eventually be concatenated with pages_to_load

# loop iterates through each needed page and produces relevant url
for current_page in range(0, pages_to_load):
    current_url = str(raw_url + str(current_page))
    with urllib.request.urlopen(current_url) as page_scrape:
        for line in page_scrape:
            lineStr = str(line, encoding='utf8')
            if "site-listing" in lineStr:   # determines relevance of line from the raw HTML
                # tags from HTML that indicate presence of needed information
                count_number_pattern = str('count">(.+)</div')
                site_name_pattern = str('siteinfo/(.+)"')
                count = re.search(count_number_pattern, lineStr)
                # only continue this branch if more page ranks must be outputted
                if int(count.group(1)) <= n:
                    site_name = re.search(site_name_pattern, lineStr)
                    print("[Rank " + count.group(1) + ": " + site_name.group(1) + "]")

# notify user if all desired values were not presented
if n > 500:
    print("\nError: Unable to return all " + str(n) + " desired elements.\n(This page only lists the Top 500 Sites)")

