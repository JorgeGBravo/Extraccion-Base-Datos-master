import urllib.request , urllib.parse , urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys
import codecs

# Si tiene una clave de API de Google Places, ingrésela aquí
# api_key = 'AIzaSy___IDByT70'

serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Detalles adicionales para urllib
# http.client.HTTPConnection.debuglevel = 1

conn = sqlite3.connect('sensores.sqlite')
cur = conn.cursor()

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

row = conn.execute(
    '''SELECT num_plaza, tipo_plaza, codigo_estado, time, latitude, longitude tipo_plaza FROM parkingvillser''')

lista = list()

for i in row:
    lista.append(i)

con2 = sqlite3.connect('geodata.sqlite')
cur2 = con2.cursor()
cur2.execute('''CREATE TABLE IF NOT EXISTS Locations (address TEXT UNIQUE, data TEXT)''')

for i in lista:
    lat = str(i[4])
    lon = str(i[5])
    adr = (lat , lon)
    adress = ','.join(adr)

    plaza = str(i[0])
    tipo = i[1]
    st = i[2]
    time = i[3]
    if st == 1:
        estado = 'ocupado'
    else:
        estado = 'libre'

    dat = (plaza , estado , tipo , time)
    print(dat)
    data = ','.join(dat)

    con2.execute('''INSERT OR REPLACE INTO Locations (address, data)
                        VALUES (?, ?)''' ,
                 (adress , data))

    con2.commit()

    # '==================================================================================='
'''
cur.execute('SELECT * FROM Locations')  # seleccionamos en locations
        fhand = codecs.open('where.js' , 'w' , "utf-8")  # variable apertura where.js
        fhand.write("myData = [\n")  # escribimos datos en where.js
        count = 0
        for row in cur:  # en locations
            data = str(row[1].decode())  # variabl decode posición 1 de row
            try:
                js = json.loads(str(data))  # si js carga jsson str tiene data
            except:
                continue  # si no no carga data continua

            if not ('status' in js and js['status'] == 'OK'): continue

            lat = js["results"][0]["geometry"]["location"]["lat"]  # valiables lat y lng de js
            lng = js["results"][0]["geometry"]["location"]["lng"]
            if lat == 0 or lng == 0: continue  # si lon y lat es = 0 continua
            where = js['results'][0]['formatted_address']
            where = where.replace("'" , "")
            try:
                print(where , lat , lng)

                count = count + 1
                if count > 1: fhand.write(",\n")
                output = "[" + str(lat) + "," + str(lng) + ", '" + where + "']"
                fhand.write(output)
            except:
                continue

        fhand.write("\n];\n")
        cur.close()
        fhand.close()
        print(count , "records written to where.js")
        print("Open where.html to view the data in a browser")'''
