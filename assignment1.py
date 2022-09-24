import bs4
import requests

text = str("Tim Berners-Lee")
url = str('https://google.com/search?q=' + text)

request1 = requests.get(url)

print("********** Section A: **********")
print("Status Code is:", request1.status_code)
print("Body is:" , request1.content)
print("Headers are:" , request1.headers)

soup = bs4.BeautifulSoup(request1.text,"html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))

print("********** Section B: **********")
request2 = requests.post("https://postman-echo.com/post")
print("Status Code is:", request2.status_code)
print("Body is:" , request2.content)
print("Headers are:" , request2.headers)

print("********** Section C: **********")
request3 = requests.get("https://alibabaaa.com/")
print("Status Code is:", request3.status_code)
print("Body is:" , request3.content)
print("Headers are:" , request3.headers)
