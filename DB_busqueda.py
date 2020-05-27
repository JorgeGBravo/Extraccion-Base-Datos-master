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


palabras = input('Palabra clave:  ')
pb = len(palabras)
print(pb)
#if pb < 1:
   # palabras = palabras.split()
   # palabra1 = palabras[0]
  #  palabra2 = palabras[1]
 #   print(palabra1, palabra2)

#    url = 'http://datos.gob.es/apidata/catalog/dataset'

#if pb > 1 and pb < 1:
url = 'http://datos.gob.es/apidata/catalog/dataset' + '/title/{}'.format(palabras)



#url = 'http://datos.gob.es/apidata/catalog/dataset/keyword/espatial/{}/{}'.format(palabra1, palabra2)
print(url)

urlimp = urllib.request.urlopen(url)


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

print(json.dumps(js, indent=4))


print('******************************************')
#5 primeros datos a recuperar

title0 = js['result']['items'][0]['title']
about0 = js['result']['items'][0]['distribution'][4]['accessURL']
print(about0)
print(title0)

title1 = js['result']['items'][1]['title']
about1 = js['result']['items'][1]['distribution'][4]['accessURL']
print(about1)
print(title1)

title2 = js['result']['items'][2]['title']
about2 = js['result']['items'][2]['distribution'][4]['accessURL']
print(about2)
print(title2)

title3 = js['result']['items'][3]['title']
about3 = js['result']['items'][3]['distribution'][4]['accessURL']
print(about3)
print(title3)

title4 = js['result']['items'][4]['title']
about4 = js['result']['items'][4]['distribution'][4]['accessURL']
print(about4)
print(title4)

title5 = js['result']['items'][5]['title']
about5 = js['result']['items'][5]['distribution'][4]['accessURL']
print(about5)
print(title5)

title6 = js['result']['items'][6]['title']
about6 = js['result']['items'][6]['distribution'][1]['accessURL']
print(about6)
print(title6)

title7 = js['result']['items'][7]['title']
about7 = js['result']['items'][7]['distribution'][4]['accessURL']
print(about7)
print(title7)

title8 = js['result']['items'][8]['title']
about8 = js['result']['items'][8]['distribution'][4]['accessURL']
print(about8)
print(title8)

title9 = js['result']['items'][9]['title']
about9 = js['result']['items'][9]['distribution'][4]['accessURL']
print(title9)
print(about9)





abrir = urllib.request.urlopen(about0)
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
dataabrir = abrir.read().decode()

print(dataabrir)