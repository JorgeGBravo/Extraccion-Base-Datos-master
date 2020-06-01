import json
import urllib.request
import urllib.parse
import urllib.error
import ssl
import random
import sqlite3

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://datos.gob.es/apidata/catalog/dataset' + '/title/{}'.format('sensores')
print(url)

urlimp = urllib.request.urlopen(url)

comm = sqlite3.connect('sensores.sqlite')
cur = comm.cursor()

# Sensores Parking Superficie - Zona Azul- Santander

cur.execute('''CREATE TABLE IF NOT EXISTS pkazulsantder
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    type TEXT UNIQUE, identifier INTERGER UNIQUE, status INTERGER,
                    modified TIMESTAMP, latitude FLOAT, longitude FLOAT,
                    uri TEXT)''')

# Sensores Medioambientales

cur.execute('''CREATE TABLE IF NOT EXISTS smedioambientalsantder
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    type TEXT UNIQUE, identifier INTERGER UNIQUE, noise FLOAT, temperature FLOAT,
                    light FLOAT, battery FLOAT, modified TIMESTAMP, latitude FLOAT,
                    longitude FLOAT, uri TEXT)''')

# Sensores de Riego

cur.execute('''CREATE TABLE IF NOT EXISTS irrigacion
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    type TEXT UNIQUE, identifier INTERGER UNIQUE, soilmoisturetension FLOAT,
                    temperature FLOAT, winddirection FLOAT, rainfall FLOAT, radiationpar FLOAT,
                    solarradiation FLOAT, windspeed FLOAT, groudtemperature FLOAT, atmosphericpreassure FLOAT,
                    relativehumidity FLOAT, battery FLOAT, modified TIMESTAMP, latitude FLOAT, longitude FLOAT,
                    uri TEXT) ''')

# Sensores Moviles Medioambientales - Santander -

cur.execute('''CREATE TABLE IF NOT EXISTS movambientalsantder
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    type TEXT UNIQUE, identifier INTERGER UNIQUE, particles FLOAT, NO2 FLOAT, temperature FLOAT,
                    altitude FLOAT, speed FLOAT, CO FLOAT, odometer FLOAT, course FLOAT, ozone FLOAT,
                    modified TIMESTAMP, latitude FLOAT, longitude FLOAT,
                    uri TEXT)''')

# Sensores Parking - Villanueva de la Serena - Badajoz -

cur.execute('''CREATE TABLE IF NOT EXISTS parkingvillser
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_parking TEXT UNIQUE, num_plaza INTERGER UNIQUE, codigo_estado INTERGER, tipo_plaza TEXT,
                    latitude FLOAT, longitude FLOAT)''')

print('URL     :' , urlimp.geturl())

headers = urlimp.info()
print('DATE    :' , headers['date'])
print('HEADERS :')
print('---------')
print(headers)

data = urlimp.read().decode()
print('LENGTH  :', len(data))

try:
    js = json.loads(str(data))
except:
    js = None

#print(json.dumps(js, indent=4))

for formatos in js['result']['items']:
    distri = js['result']['items']

for popa in distri:
    abo = popa['distribution']

    for pope in abo:
        titulo = pope['title']
        accessU = pope['accessURL']
        format = pope['format']
        value = format['value']

        if value == 'application/vnd.geo+json':

            if titulo == 'Sensores del parking':
                print(titulo)
                print(accessU)
                urlsp = urllib.request.urlopen(accessU)

                datasp = urlsp.read().decode()

                print(json.dumps(datasp , indent=4))

                try:
                    js = json.loads(str(datasp))
                except:
                    js = None

                feature = js['features']
                for i in feature:
                    geo = i['geometry']
                    prop = i['properties']

                    for g in geo:
                        coor = geo['coordinates']
                        lat = geo['coordinates'][1]
                        long = geo['coordinates'][0]

                    for p in prop:
                        num_plaza = prop['num_plaza']
                        cod_estado = prop['cod_estado']
                        estado = prop['estado']
                        tipo_plaza = prop['tipo_plaza']
                        print(tipo_plaza)

            if titulo == 'Sensores de EESystem':
                print(titulo)
                print(accessU)
                urlsee = urllib.request.urlopen(accessU).read().decode()
                print(json.dumps(urlsee , indent=4))

        if value == 'application/json':
            if titulo == 'Sensores ambientales':
                print(titulo)
                print(accessU)
                urlsa = urllib.request.urlopen(accessU).read().decode()
                print(json.dumps(urlsa , indent=4))

            if titulo == 'Sensores Parking de Superficie':
                print(titulo)
                print(accessU)
                urlsps = urllib.request.urlopen(accessU).read().decode()
                print(json.dumps(urlsps , indent=4))

            if titulo == 'Sensores de riego':
                print(titulo)
                print(accessU)
                urlsr = urllib.request.urlopen(accessU).read().decode()
                print(json.dumps(urlsr , indent=4))

            if titulo == 'Sensores móviles':
                print(titulo)
                print(accessU)
                urlsm = urllib.request.urlopen(accessU).read().decode()
                print(json.dumps(urlsm , indent=4))
