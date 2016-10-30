#!/usr/bin/env python
import os
import pyesdoc
import pyesdoc.ontologies.cim as cim

org = pyesdoc.create(cim.v2.Party)
org.address = u"201 Forrestal Road, Princeton, NJ, USA"
org.name = "Geophysical Fluid Dynamics Laboratory"
org.organisation = 1

# URL must be a cim.v2.OnlineResource not a string
org.url = "www.gfdl.noaa.gov"

org.meta.version = 1

dir = os.environ['HOME'] + "/esdoc-testing/pyesdoc/responsible_party"
os.system("mkdir -p " + dir)
pyesdoc.write(org, dir)
