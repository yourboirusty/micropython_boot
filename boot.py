# This file is executed on every boot (including wake-boot from deepsleep)
import esp
import uos
import gc
import json
import network
import usocket
import random

#uos.dupterm(None, 1) # disable REPL on UART(0)
esp.osdebug(None)



with open('conf/network.conf', 'r') as config_file:
    config = json.load(config_file)


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
hostname = "Shutter_" + hex(random.getrandbits(16))[2:]
wlan.config(dhcp_hostname = "test")
wlan.connect(*config['WLAN'])

if not wlan.isconnected():
    wlan.active(False)
      

if not wlan.active():
    ap = network.WLAN(network.AP_IF)
    ap.config(**config['AP'])
    ap.active(True)    




gc.collect()
