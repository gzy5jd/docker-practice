import requests
import json
import datetime

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)

r = response.json()

lon = r['iss_position']['longitude']
lat = r['iss_position']['latitude']
timestamp = r['timestamp']

datetime = datetime.datetime.fromtimestamp(timestamp)
dtime = datetime.strftime('%Y-%m-%d-%H:%M:%S')

print(dtime, lon, lat)

lines = [dtime, '\n', lon, '\n', lat]

with open('/data/output.txt', 'w') as f: # FOLDER DOESN'T EXIST
    f.writelines(lines)

# Container needs a place to write and store output.txt