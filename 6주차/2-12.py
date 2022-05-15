from bs4 import BeautifulSoup
import requests

url = "http://www.daum.net/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

file = open("2-12.html", "w")
file.write(response.text)
file.close()

print(soup.title)
print(soup.title.string)
print(soup.span)
print(soup.findAll('span'))

#html 안 뜸