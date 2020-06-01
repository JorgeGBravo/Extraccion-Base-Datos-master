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
# ===================================================Sensores Parking Coventual Villanueva de la Serena==================
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
                        # coor = geo['coordinates']
                        lat = geo['coordinates'][1]
                        long = geo['coordinates'][0]

                    for p in prop:
                        num_plaza = prop['num_plaza']
                        cod_estado = prop['cod_estado']
                        estado = prop['estado']
                        tipo_plaza = prop['tipo_plaza']
                        nombre = prop['nombre_parking']

        # =========================================Sensores Eficiencia Energetica - EESystem-====================================
        # if titulo == 'Sensores de EESystem':
        # print(titulo)
        # print(accessU)
        # urlsee = urllib.request.urlopen(accessU)
        # print(json.dumps(urlsee , indent=4))

        # datasee = urlsee.read().decode()

        # print(json.dumps(datasee , indent=4))

        # try:
        #    js = json.loads(str(datasee))
        # except:
        #    js = None
        # =========================================Sensores Medioambientales -Santander-=========================================

        if value == 'application/json':
            if titulo == 'Sensores ambientales':
                print(titulo)
                print(accessU)
                urlsa = urllib.request.urlopen(accessU)
                datasa = urlsa.read().decode()
                # print(json.dumps(datasa , indent=4))
                try:
                    js = json.loads(str(datasa))
                except:
                    js = None

                resources = js['resources']

                for r in resources:
                    type = r['ayto:type']
                    identifier = r['dc:identifier']
                    noise = r['ayto:noise']
                    temperature = r['ayto:temperature']
                    light = r['ayto:light']
                    battery = r['ayto:battery']
                    time = r['dc:modified']
                    lat = r['ayto:latitude']
                    long = r['ayto:longitude']
                    uri = r['uri']

            # ====================================================Sensores Zona Azul -Santander-=====================================

            if titulo == 'Sensores Parking de Superficie':
                print(titulo)
                print(accessU)
                urlsps = urllib.request.urlopen(accessU)
                # print(json.dumps(urlsps , indent=4))
                datasps = urlsps.read().decode()
                # print(json.dumps(datasa , indent=4))
                try:
                    js = json.loads(str(datasps))
                except:
                    js = None

                resources = js['resources']

                for r in resources:
                    type = r['ayto:type']
                    identifier = r['dc:identifier']
                    status = r['ayto:status']
                    time = r['dc:modified']
                    lat = r['ayto:latitude']
                    long = r['ayto:longitude']
                    uri = r['uri']

            # =================================================Sensores de Riego -Santander-=========================================

            if titulo == 'Sensores de riego':
                print(titulo)
                print(accessU)
                urlsr = urllib.request.urlopen(accessU)
                datasr = urlsr.read().decode()
                # print(json.dumps(datasa , indent=4))
                try:
                    js = json.loads(str(datasr))
                except:
                    js = None

                resources = js['resources']

                for r in resources:
                    type = r['ayto:type']
                    identifier = r['dc:identifier']
                    soilmosturet = r['ayto:soilMoistureTension']
                    temperature = r['ayto:temperature']
                    winddirection = r['ayto:windDirection']
                    rainfall = r['ayto:rainfall']
                    radiationpar = r['ayto:radiationPAR']
                    solarradiation = r['ayto:solarRadiation']
                    windspeed = r['ayto:windSpeed']
                    groundtemp = r['ayto:groundTemperature']
                    atmpress = r['ayto:atmosphericPressure']
                    relathumid = r['ayto:relativeHumidity']
                    battery = r['ayto:battery']
                    time = r['dc:modified']
                    lat = r['ayto:latitude']
                    long = r['ayto:longitude']
                    uri = r['uri']
            # =================================================Sensores Moviles Medioambientales -Santander-=========================
            if titulo == 'Sensores móviles':
                print(titulo)
                print(accessU)
                urlsmm = urllib.request.urlopen(accessU)
                datasmm = urlsmm.read().decode()
                # print(json.dumps(datasa , indent=4))
                try:
                    js = json.loads(str(datasmm))
                except:
                    js = None

                resources = js['resources']

                for r in resources:
                    type = r['ayto:type']
                    identifier = r['dc:identifier']
                    particles = r['ayto:particles']
                    no2 = r['ayto:particles']
                    temperature = r['ayto:temperature']
                    altitude = r['ayto:altitude']
                    speed = r['ayto:speed']
                    co = r['ayto:CO']
                    odometer = r['ayto:odometer']
                    course = r['ayto:course']
                    ozone = r['ayto:ozone']
                    time = r['dc:modified']
                    lat = r['ayto:latitude']
                    long = r['ayto:longitude']
                    uri = r['uri']
                    print(uri)
