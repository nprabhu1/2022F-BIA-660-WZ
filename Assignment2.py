from typing import TextIO

import requests
from bs4 import BeautifulSoup
import re
import csv

print("************** Step 1 **************")
url = "https://en.m.wikipedia.org/wiki/List_of_Internet_top-level_domains"
r = requests.get(url)
print("Step 1 Status Code: " + str(r.status_code))

print("************** Step 2 **************")
soup = BeautifulSoup(r.content, "html.parser")
match = "\.[a-z]{2,}"

tld = re.findall(match, soup.get_text())
tld_list = list(sorted(set(tld)))
print("Top Level Domains are: ", tld_list)

print("************** Step 3 **************")
url_list = []
# top_domain_converted = []
for x in tld_list:
    url2 = "http://www.example" + x
    url_list.append(url2)
print(url_list)

url_result = []

for i in url_list:
    try:
        print("Trying...." + i)
        p = str('"' + str(i) + '"')
        r2 = requests.get(p).status_code
        if r2 == 200:
            result = "Valid"
            url_result.append(result)
        else:
            result = "InValid"
            url_result.append(result)
    except:
        result = "Error"
        url_result.append(result)


with open('validation_results.csv', 'w') as f:
    wr = csv.writer(f)
    wr.writerows(zip(url_list,url_result))
