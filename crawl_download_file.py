import requests
import urllib.request
from bs4 import BeautifulSoup

url = "http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml"

html = requests.get(url).content
soup = BeautifulSoup(html, "lxml")
links = soup.findAll("a")
ready_links = []
for i in links:
    if "2016" in i["href"] or "2017" in i["href"]:
        ready_links.append(i["href"])
# download
# print(ready_links[0])
# print(ready_links[0][43:])
response = urllib.request.urlopen(ready_links[0])
data = response.read()
text = data.decode("utf-8")
urllib.request.urlretrieve(ready_links[0], str(ready_links[0][43:]))
print("done")
# print(ready_links[0][33])
