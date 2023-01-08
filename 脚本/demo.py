import requests


{"CityCode":"511700","cityName":"达州市","cityNameEn":"DZS"}

url = "http://www.591mf.top/home/Electric"

body = {"w":"4100789182","type":"江苏"}
header = {"Content-Type":"application/x-www-form-urlencoded","C0ntent-Length":"131413"}
res = requests.post(url=url,data=body,headers=header)
print(res.text)