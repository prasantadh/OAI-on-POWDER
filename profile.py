#!/usr/bin/python

"""Profile to run OAI-5G-NR code on two lab radios

Instructions:
    Wait for the profile to be instantiated.
    SSH via the given ports.
    We will update the instructions with scripts to be run once finalized.
"""

# The following code is inspired by and based on
# https://gitlab.flux.utah.edu/powder-profiles/ota_srslte/-/tree/master

# import the portal object
import geni.portal as portal
import geni.rspec.pg as rspec
import geni.rspec.emulab.pnext as pn
import geni.rspec.igext as ig
# import geni.rspec.emulab.spectrum as spectrum


class GLOBALS:
    SRSLTE_IMG = "urn:publicid:IDN+emulab.net+image+PowderTeam:U18LL-SRSLTE:N"
    DLHIFREQ = 2630.0
    DLLOFREQ = 2620.0
    ULHIFREQ = 2510.0
    ULLOFREQ = 2500.0

pc = portal.Context()
pc.verifyParameters()

# create a request object to start building the RSpec
request = portal.context.makeRequestRSpec()

# request the gnb
gnb = request.RawPC("node")
gnb.disk_image = GLOBALS.SRSLTE_IMG

# write the RSpec file
portal.context.printRequestRSpec()
