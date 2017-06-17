import urllib2
import json

url = 'https://api.irail.be/liveboard/?station=Yvoir&fast=true&format=json'

req = urllib2.Request(url)
handle = urllib2.urlopen(req)

res = handle.read()
res = json.loads(res)

data = []
for depart in res.get('departures').get('departure'):
        # print "{0} {1}".format(depart.get('station'), depart.get('delay'), depart.get('platform'))    
        data.append({'departures': depart.get('station'), 'delay': depart.get('delay'), 'platform': depart.get('platform')})

print json.dumps(data)
