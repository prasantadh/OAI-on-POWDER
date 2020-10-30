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
import geni.urn as URN
# import geni.rspec.emulab.spectrum as spectrum


class GLOBALS:
    SRSLTE_IMG = "urn:publicid:IDN+emulab.net+image+PowderTeam:U18LL-SRSLTE:N"
    HW_TYPE = "d430"
    DLHIFREQ = 2630.0
    DLLOFREQ = 2620.0
    ULHIFREQ = 2510.0
    ULLOFREQ = 2500.0

pc = portal.Context()
pc.verifyParameters()

# create a request object to start building the RSpec
request = portal.context.makeRequestRSpec()

# request the SDR for gnb
gnb_sdr = request.RawPC( "gnb_sdr" )
gnb_sdr.hardware_type = "sdr"
# for now leaving the image to be the default image set by mapping algo
# usrp_gnb.disk_image = URN.Image(PN.PNDEFS.PNET_AM, "emulab-ops:GENERICDEV-NOVLANS")
if_gnb_sdr_to_compute = gnb_sdr.addInterface("sdr_compute")
if_gnb_sdr_to_compute.addAddress( rspec.IPv4Address( "192.168.30.2", "255.255.255.0" ) )

# request the computational node for gnb
gnb_compute = request.RawPC("gnb_compute")
gnb_compute.hardware_type = "d430"
gnb_compute.disk_image = GLOBALS.SRSLTE_IMG
if_gnb_compute_to_sdr = gnb_compute.addInterface("compute_nuc")
if_gnb_compute_to_sdr.addAddress(rspec.IPv4Address("192.168.30.1", "255.255.255.0"))

# add the communication link gnb <-> gnb-compute
link_gnb_sdr = request.Link("sdr-gnb")
link_gnb_sdr.addInterface(if_gnb_sdr_to_compute)
link_gnb_sdr.addInterface(if_gnb_compute_to_sdr)

# write the RSpec file
portal.context.printRequestRSpec()
