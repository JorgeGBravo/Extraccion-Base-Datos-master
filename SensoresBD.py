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


url = 'http://datos.gob.es/apidata/catalog/dataset' + '/title/{}'.format('sensores')
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

#print(json.dumps(js, indent=4))
lista = list()

for formatos in js['result']['items']:
    #print('items:')
    #print(json.dumps(formatos, indent=4))
    distri = js['result']['items']

for popa in distri:
    abo = popa['distribution']

    for pope in abo:
        #print('pope', json.dumps(pope, indent=4))
        titulo = pope['title']
        accessU = pope['accessURL']
        format = pope['format']
        value = format['value']

        if value == 'application/vnd.geo+json' not in lista:
            print(titulo)
            print(accessU)
            urlgj = urllib.request.urlopen(accessU).read().decode()
            print('****************************************************')
            print(json.dumps(urlgj , indent=4))
            print('****************************************************')

        if value == 'application/json' not in lista:
            print(titulo)
            print(accessU)
            urlj = urllib.request.urlopen(accessU).read().decode()
            print('****************************************************')
            print(json.dumps(urlj , indent=4))
            print('****************************************************')

        # print(lista)
