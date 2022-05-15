import requests

url = "http://www.naver.com"
response = requests.get(url)
#200=성공
#print(response.text)

#print(response.url)
#url주소
#print(response.content)
#html
#print(response.encoding)
#UTF-8(인코딩방식)
#print(response.headers)
#서버관련?
#print(response.json)
#?
#print(response.links)
#{}
#print(response.ok)
#True
#print(response.status_code)
#200 (성공이라는 뜻?)