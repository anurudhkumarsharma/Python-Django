import requests
import bs4
r=requests.get("https://en.wikipedia.org/wiki/Arijit_Singh")
(r.text)  
soup= bs4.BeautifulSoup(r.text,"lxml")
t=soup.select("title")
print(t[0].getText())