#!/usr/bin/env python
import pyesdoc
import pyesdoc.ontologies.cim as cim

org = pyesdoc.create(cim.v2.Party)
org.address = u"201 Forrestal Road, Princeton, NJ, USA"
org.name = "Geophysical Fluid Dynamics Laboratory"
org.organisation = 1
org.url = "www.gfdl.noaa.gov"

org.meta.version = 1

pyesdoc.write(org, "/esdoc/testing/invalid")
