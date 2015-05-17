import json
import urllib2

url = 'http://api.openweathermap.org/data/2.5/weather?q=seattle' 
f = urllib2.urlopen(url)
j = json.loads(f.read())
print j.keys()
print j.get('weather')

