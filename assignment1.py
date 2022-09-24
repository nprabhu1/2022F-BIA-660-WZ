import bs4
import requests

text = str("Tim Berners-Lee")
url = str('https://google.com/search?q=' + text)

request_result = requests.get(url)

print("Section A:")
soup = bs4.BeautifulSoup(request_result.text,"html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))

#print("Section B:")
#post=requests.post("https://apple.com")
#print(post.status)
#print(post.contents)
#print(post.text)