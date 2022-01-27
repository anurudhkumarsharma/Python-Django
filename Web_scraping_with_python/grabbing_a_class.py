import requests
import bs4
r=requests.get("https://www.flipkart.com/")
soup=bs4.BeautifulSoup(r.text,"lxml")
s=soup.select("p")
for i in s:
    print(i)
    
