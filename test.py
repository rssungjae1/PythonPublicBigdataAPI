import urllib.request
import xml.dom.minidom

encodingKey = "{인코딩키}"
decodingKey = "{디코딩키}"

print("[START]")

url = "http://apis.data.go.kr/B551182/hospAsmRstInfoService/getHospAsmGrdCrtrList?ServiceKey=" + encodingKey + "&numOfRows=10&pageNo=1&asmItmCd=26"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

dom = xml.dom.minidom.parseString(response_body.decode('utf-8'))
pretty_xml_as_string = dom.toprettyxml()
print(pretty_xml_as_string)

print("[END]")