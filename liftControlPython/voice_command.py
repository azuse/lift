import requests
import bluetooth
import os, time
import urllib3
import json
import sys
import lift

nowLevel = 0

def saveRecord(addr, name, fromLevel, toLevel):
    http = urllib3.PoolManager()
    try:
    	r = http.request('GET', "http://192.168.43.128:5000/api/saveRecord?device_addr=%s&device_name=%s&fromLevel=%d&toLevel=%d" % (addr,name,fromLevel,toLevel))
    	print(r.data)
    	return r.data
    except:
        print('network error')
        return -1

toLevel = int(sys.argv[1].encode('utf-8'))

print("前往" + str(toLevel) + "层")

### 调用电梯操作api ###
###     未实现     ###
#nowLevel = lift.getNowLevel()
print(lift.goto(int(toLevel)))
######################

read_path = "/home/pi/pipe.out"

rf = os.open(read_path, os.O_RDONLY | os.O_NONBLOCK)

try:
    device_new_data = os.read(rf, 256)
except:
    print(device_new_data)
else:
    print(device_new_data)
if device_new_data != b'' :
    device_new = json.loads(device_new_data.decode("utf-8"))
    print("新设备"+device_new[0]+device_new[1])
    saveRecord(device_new[0], device_new[1], nowLevel, toLevel)





