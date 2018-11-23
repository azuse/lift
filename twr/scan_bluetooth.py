import bluetooth
import os, time
import urllib3
import json
import lift

nearby_devices = bluetooth.discover_devices(duration=20, lookup_names = True)
for addr,name in nearby_devices:
    print(addr + name)
