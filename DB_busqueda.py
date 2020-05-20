import json
import urllib.request
import urllib.parse
import urllib.error
import ssl
import random

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


palabra = input('Palabra clave:  ')
print(palabra)

urlimp = urllib.request.urlopen('http://datos.gob.es/apidata/catalog/dataset'+ palabra)#.read().decode()


print('URL     :', urlimp.geturl())

headers = urlimp.info()
print('DATE    :', headers['date'])
print('HEADERS :')
print('---------')
print(headers)

data = urlimp.read().decode()
print('LENGTH  :', len(data))
#print('DATA    :')
print('---------')
#print(data)

try:
    js = json.loads(str(data))
except:
    js = None

#print(json.dumps(js, indent=4))


print('******************************************')
#5 primeros datos a recuperar

title0 = js['result']['items'][0]['title']
about0 = js['result']['items'][0]['_about']

title1 = js['result']['items'][1]['title']
about1 = js['result']['items'][1]['_about']

title2 = js['result']['items'][2]['title']
about2 = js['result']['items'][2]['_about']

title3 = js['result']['items'][3]['title']
about3 = js['result']['items'][3]['_about']

title4= js['result']['items'][4]['title']
about4 = js['result']['items'][4]['_about']


print('******************************************')

print(about0)
print(title0)
print(about1)
print(title1)
print(about2)
print(title2)
print(about3)
print(title3)
print(about4)
print(title4)