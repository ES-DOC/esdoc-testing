#!/usr/bin/env python
import argparse
import os
import pprint

import requests

import pyesdoc

#_URL = "http://localhost:5000"
_URL = "http://lvm-000009.gfdl.noaa.gov:5000"
# next 2 lines should work but don't
#_URL_GET = "{}/2/document/retrieve".format(_URL)
#_URL_GET_PARAMS = "?encoding={}&project=BETA-TEST&document_id={}&document_version={}"
_URL_GET = "{}/2/document/search-id".format(_URL)
_URL_GET_PARAMS = "?client=ESDOC-SEARCH&encoding=json&project=BETA-TEST&id={}&version=latest"
_URL_PUT = "{}/2/document/update".format(_URL)

parser = argparse.ArgumentParser()
parser.add_argument("UID", help="UID of ResponsibleParty document to update")
args = parser.parse_args()

params = _URL_GET_PARAMS.format(args.UID)
params.format('json', args.UID)
url = "{}{}".format(_URL_GET, params)
print "url", url

pp = pprint.PrettyPrinter(indent=4)
response = requests.get(url)
#print "response", response

doc = pyesdoc.decode(response.text, 'json')
pp.pprint(doc)
doc.name += ', updated'
doc.meta.version += 1

data = pyesdoc.encode(doc, 'json')
headers = {'Content-Type': 'application/json'}
url = _URL_PUT
print "url", url
response = requests.put(url, data=data, headers=headers)
print "response", response
