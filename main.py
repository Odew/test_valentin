import urllib2
import json

url = 'https://api.irail.be/liveboard/?station=Yvoir&fast=true&format=json'

req = urllib.Request(url)
handle = urllib2.urlopen(req)

res = handle.read()
res = json.loads(res)

print "Station - Retard - Quai"
for depart in res.get('departures').get('departure'):
        print "{0} {1} {2}".format(depart.get('station'), depart.get('delay'), depart.get('platform'))
        
