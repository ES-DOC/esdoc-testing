#!/usr/bin/env python
import argparse
import os
import pprint

import requests

import pyesdoc

_URL = "http://localhost:5000"
_URL_DELETE = "{}/2/document/delete".format(_URL)
_URL_DELETE_PARAMS = "?document_id={}&document_version={}"

parser = argparse.ArgumentParser()
parser.add_argument("UID", help="UID of ResponsibleParty document to unpublish")
args = parser.parse_args()

params = _URL_DELETE_PARAMS.format(args.UID, 'latest')
url = "{}{}".format(_URL_DELETE, params)
print 'url', url

response = requests.delete(url)
print "response", response
