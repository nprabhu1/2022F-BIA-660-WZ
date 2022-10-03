import bs4
import requests
import re


wiki_url = str('https://en.m.wikipedia.org/wiki/List_of_Internet_top-level_domains')
table_class = "wikitable.sortable.jquery-tablesorter"
request1 = requests.get(wiki_url)

soup = bs4.BeautifulSoup(request1.text, 'html.parser')
domain_table = soup.find('tbody').find_all('tr')


for d in domain_table:
    name = d.find('td').a.text
    domain = re.search(r'\.\w', name)
    print(domain)
