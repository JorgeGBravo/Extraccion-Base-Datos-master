import json
import urllib.request
import urllib.parse
import urllib.error
import ssl
import random
import sqlite3


def create_sensor_parking(feature, cur):
    geo = feature['geometry']
    prop = feature['properties']

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

    cur.execute('''INSERT OR REPLACE INTO parkingvillser
                                    (id, nombre_parking, num_plaza, codigo_estado, tipo_plaza, time, latitude, longitude)
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                (num_plaza, nombre, num_plaza, cod_estado, tipo_plaza, date, lat, long))


def create_sensor_medioambiante(resource, cur):
    type = resource['ayto:type']
    identifier = resource['dc:identifier']
    noise = resource['ayto:noise']
    temperature = resource['ayto:temperature']
    light = resource['ayto:light']
    battery = resource['ayto:battery']
    time = resource['dc:modified']
    lat = resource['ayto:latitude']
    long = resource['ayto:longitude']
    uri = resource['uri']

    cur.execute('''INSERT OR REPLACE INTO smedioambientalsantder
                                     (id, type, identifier, noise, temperature, light, battery, modified, latitude,
                                     longitude, uri)
                                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (identifier, type, identifier, noise, temperature, light, battery, time,
                 lat, long, uri))


def create_sensor_zona_azul(resource, cur):
    type = resource['ayto:type']
    identifier = resource['dc:identifier']
    status = resource['ayto:status']
    time = resource['dc:modified']
    lat = resource['ayto:latitude']
    long = resource['ayto:longitude']
    uri = resource['uri']

    cur.execute('''INSERT OR REPLACE INTO pkazulsantder
                                    (id, type, identifier, status, modified, latitude, longitude, uri)
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                (identifier, type, identifier, status, time, lat, long, uri))


def create_sensor_riego(resource, cur):
    type = resource['ayto:type']
    identifier = resource['dc:identifier']
    soilmosturet = resource['ayto:soilMoistureTension']
    temperature = resource['ayto:temperature']
    winddirection = resource['ayto:windDirection']
    rainfall = resource['ayto:rainfall']
    radiationpar = resource['ayto:radiationPAR']
    solarradiation = resource['ayto:solarRadiation']
    windspeed = resource['ayto:windSpeed']
    groundtemp = resource['ayto:groundTemperature']
    atmpress = resource['ayto:atmosphericPressure']
    relathumid = resource['ayto:relativeHumidity']
    battery = resource['ayto:battery']
    time = resource['dc:modified']
    lat = resource['ayto:latitude']
    long = resource['ayto:longitude']
    uri = resource['uri']

    cur.execute('''INSERT OR REPLACE INTO irrigacion
                                    (id, type, identifier, soilmoisturetension,
                                    temperature, winddirection, rainfall, radiationpar,
                                    solarradiation, windspeed, groudtemperature, atmosphericpreassure,
                                    relativehumidity, battery, modified, latitude, longitude, uri)
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (identifier, type, identifier, soilmosturet, temperature, winddirection,
                 rainfall, radiationpar, solarradiation, windspeed, groundtemp, atmpress,
                 relathumid,
                 battery, time, lat, long, uri))


def create_sensor_mobile_medioambiente(resource, cur):
    type = resource['ayto:type']
    identifier = resource['dc:identifier']
    particles = resource['ayto:particles']
    no2 = resource['ayto:NO2']
    temperature = resource['ayto:temperature']
    altitude = resource['ayto:altitude']
    speed = resource['ayto:speed']
    co = resource['ayto:CO']
    odometer = resource['ayto:odometer']
    course = resource['ayto:course']
    ozone = resource['ayto:ozone']
    time = resource['dc:modified']
    lat = resource['ayto:latitude']
    long = resource['ayto:longitude']
    uri = resource['uri']

    cur.execute('''INSERT OR REPLACE INTO movambientalsantder
                                    (id, type, identifier, particles, NO2, temperature, altitude, speed,
                                    CO, odometer, course, ozone, modified, latitude, longitude, uri)
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (identifier, type, identifier, particles, no2, temperature, altitude,
                 speed, co, odometer, course, ozone, time, lat, long, uri))


def initialize_database(cur):
    # Sensores Parking Superficie - Zona Azul- Santander

    cur.execute('''CREATE TABLE IF NOT EXISTS pkazulsantder
                        (id INTEGER PRIMARY KEY UNIQUE, 
                        type TEXT, identifier INTERGER UNIQUE, status INTERGER,
                        modified TIMESTAMP, latitude FLOAT, longitude FLOAT,
                        uri TEXT)''')

    # Sensores Medioambientales

    cur.execute('''CREATE TABLE IF NOT EXISTS smedioambientalsantder
                        (id INTEGER PRIMARY KEY UNIQUE,
                        type TEXT, identifier INTERGER UNIQUE, noise FLOAT, temperature FLOAT,
                        light FLOAT, battery FLOAT, modified TIMESTAMP, latitude FLOAT,
                        longitude FLOAT, uri TEXT)''')

    # Sensores de Riego

    cur.execute('''CREATE TABLE IF NOT EXISTS irrigacion
                        (id INTEGER PRIMARY KEY UNIQUE,
                        type TEXT, identifier INTERGER UNIQUE, soilmoisturetension FLOAT,
                        temperature FLOAT, winddirection FLOAT, rainfall FLOAT, radiationpar FLOAT,
                        solarradiation FLOAT, windspeed FLOAT, groudtemperature FLOAT, atmosphericpreassure FLOAT,
                        relativehumidity FLOAT, battery FLOAT, modified TIMESTAMP, latitude FLOAT, longitude FLOAT,
                        uri TEXT) ''')

    # Sensores Moviles Medioambientales - Santander -

    cur.execute('''CREATE TABLE IF NOT EXISTS movambientalsantder
                        (id INTEGER PRIMARY KEY UNIQUE,
                        type TEXT, identifier INTERGER UNIQUE, particles FLOAT, NO2 FLOAT, temperature FLOAT,
                        altitude FLOAT, speed FLOAT, CO FLOAT, odometer FLOAT, course FLOAT, ozone FLOAT,
                        modified TIMESTAMP, latitude FLOAT, longitude FLOAT,
                        uri TEXT)''')

    # Sensores Parking - Villanueva de la Serena - Badajoz -

    cur.execute('''CREATE TABLE IF NOT EXISTS parkingvillser
                        (id INTEGER PRIMARY KEY UNIQUE,
                        nombre_parking TEXT, num_plaza INTERGER UNIQUE, codigo_estado INTERGER, tipo_plaza TEXT, time TIMESTAMP,
                        latitude FLOAT, longitude FLOAT)''')


def get_initial_data(url):
    print(url)
    urlimp = urllib.request.urlopen(url)
    print('URL     :', urlimp.geturl())
    headers = urlimp.info()
    date = headers['date']
    print('DATE    :', headers['date'])
    print('HEADERS :')
    print('---------')
    print(headers)
    data = urlimp.read().decode()
    print('LENGTH  :', len(data))

    try:
        js = json.loads(str(data))
    except:
        js = None

    return js, date



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

comm = sqlite3.connect('sensores.sqlite')
cur = comm.cursor()
initialize_database(cur)

url = 'http://datos.gob.es/apidata/catalog/dataset' + '/title/{}'.format('sensores')
js, date = get_initial_data(url)


for popa in js['result']['items']:
    abo = popa['distribution']

    for pope in abo:
        if not isinstance(pope , dict): continue

        titulo = pope['title']
        accessU = pope['accessURL']
        format = pope['format']
        value = format['value']

        if value == 'application/vnd.geo+json':
            elements_key = 'features'
        elif value == 'application/json':
            elements_key = 'resources'
        else:
            continue

        urlsa = urllib.request.urlopen(accessU)
        datasa = urlsa.read().decode()
        try:
            js = json.loads(str(datasa))
        except:
            js = None

        resources = js[elements_key]

        for r in resources:

            if titulo == 'Sensores del parking':
                create_sensor_parking(r, cur)
            elif titulo == 'Sensores ambientales':
                create_sensor_medioambiante(r, cur)
            elif titulo == 'Sensores Parking de Superficie':
                create_sensor_zona_azul(r, cur)
            elif titulo == 'Sensores de riego':
                create_sensor_riego(r, cur)
            elif titulo == 'Sensores móviles':
                create_sensor_mobile_medioambiente(r, cur)

        comm.commit()
