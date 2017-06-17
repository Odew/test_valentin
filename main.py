# -*- coding: utf-8 -*-
import urllib2
import json

url = 'https://api.irail.be/liveboard/?station=Yvoir&fast=true&format=json'

# Récupération des données via urllib2
req = urllib2.Request(url)
handle = urllib2.urlopen(req)
res = handle.read()

# Transformation des données au format json en un dictionaire python
res = json.loads(res)

# Boucle sur les départs
data = []
for depart in res.get('departures').get('departure'):
        data.append({'departures': depart.get('station'), 'delay': depart.get('delay'), 'platform': depart.get('platform')})

print json.dumps(data)
