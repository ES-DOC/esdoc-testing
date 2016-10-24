#!/usr/bin/env python
import pyesdoc
import pyesdoc.ontologies.cim as cim

gfdl_url = pyesdoc.create(cim.v2.OnlineResource)
gfdl_url.linkage = "www.gfdl.noaa.gov"
gfdl_url.name = "GFDL web page"
gfdl_url.protocol = "http"

person = pyesdoc.create(cim.v2.Party)
person.name = u"Chris E. Blanton"
person.address = u"201 Forrestal Rd, Princeton, NJ, United States"
person.email = u"chris.blanton@noaa.gov"
person.organisation = 0

org = pyesdoc.create(cim.v2.Party)
org.address = u"201 Forrestal Road, Princeton, NJ, United States"
org.name = "Geophysical Fluid Dynamics Laboratory"
org.organisation = 1
#org.url = "www.gfdl.noaa.gov"
org.url = gfdl_url

person.meta.version = 2
org.meta.version = 2

pyesdoc.write(person, "/esdoc/testing/valid")
pyesdoc.write(org, "/esdoc/testing/valid")
