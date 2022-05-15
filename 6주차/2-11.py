import requests
from bs4 import BeautifulSoup

url = "http://www.daum.net/"
response = requests.get(url)
# print(response.text)

#soup = BeautifulSoup(response.text, 'html.parser')
#span이 안 뜰 때
soup = BeautifulSoup(response.content, 'html.parser', from_encoding='cp949')
response.encoding = 'utf-8'

print(soup.title)
print(soup.title.string)
print(soup.span)
print(soup.findAll('span'))

#span안 뜸