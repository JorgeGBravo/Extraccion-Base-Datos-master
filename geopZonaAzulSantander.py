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
    '''SELECT status, modified, latitude, longitude FROM pkazulsantder''')

lista = list()

for i in row:
    lista.append(i)

con2 = sqlite3.connect('geodata.sqlite')
cur2 = con2.cursor()
cur2.execute('''CREATE TABLE IF NOT EXISTS LocatAzulSant (address TEXT UNIQUE, data TEXT)''')

for i in lista:
    lat = str(i[2])
    lon = str(i[3])
    adr = (lat , lon)
    adress = ','.join(adr)
    st = i[0]
    time = i[1]
    if st == 1:
        estado = 'Libre'
    else:
        estado = 'Ocupado'

    dat = (estado , time)

    data = ','.join(dat)

    con2.execute('''INSERT OR REPLACE INTO LocatAzulSant (address, data)
                        VALUES (?, ?)''' ,
                 (adress , data))

    con2.commit()

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM LocatAzulSant')
fhand = codecs.open('whereazul.js' , 'w' , "utf-8")
fhand.write("myData = [\n")
lista = list()

for i in cur:
    where = i[1]
    lt = i[0]
    print(where)
    print(lt)
    if where > str(0):
        output = "[" + str(lt) + ", '" + where + "']"
        lista.append(output)
        # fhand.write(output)if

fhand.write(",\n".join(lista))

fhand.write("\n];\n")

cur.close()
fhand.close()
print("Open wherecoventual.html to view the data in a browser")
