#!/usr/bin/env python
import os
import pyesdoc
import pyesdoc.ontologies.cim as cim

gfdl_url = pyesdoc.create(cim.v2.OnlineResource)
gfdl_url.linkage = "www.gfdl.noaa.gov"
gfdl_url.name = "GFDL web page"
gfdl_url.protocol = "http"

person = pyesdoc.create(cim.v2.Party)
person.name = u"Chris E. Blanton"
person.address = u"201 Forrestal Rd, Princeton, NJ, USA"
person.email = u"chris.blanton@noaa.gov"
person.organisation = 0

org = pyesdoc.create(cim.v2.Party)
org.address = u"201 Forrestal Road, Princeton, NJ, USA"
org.name = "Geophysical Fluid Dynamics Laboratory"
org.organisation = 1
org.url = gfdl_url

person.meta.version = 1
org.meta.version = 1

dir = os.environ['HOME'] + "/esdoc-testing/pyesdoc/responsible_party"
os.system("mkdir -p " + dir)
pyesdoc.write(person, dir)
pyesdoc.write(org, dir)
