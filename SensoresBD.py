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


for formatos in js['result']['items']:
    #print('items:')
    #print(json.dumps(formatos, indent=4))
    distri = js['result']['items']

for popa in distri:
    abo = popa['distribution']

    for pope in abo:
        print('pope', json.dumps(pope, indent=4))
        accessU = pope['accessURL']
        format = pope['format']

        for popi in format:
            print('++++++++++++++++++++++++++++++++')
            print('popi', json.dumps(popi, indent=4))
            print('++++++++++++++++++++++++++++++++')
            print(popi['value'])                            #en este punto no me muestra value,  necesito value para confirmar formato

