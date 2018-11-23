import requests
import bluetooth
import os, time
import urllib3
import json
import lift

write_path = "/home/pi/pipe.out"

if os.path.exists(write_path):
    os.remove(write_path)

os.mkfifo(write_path)

wf = os.open(write_path, os.O_SYNC | os.O_CREAT | os.O_RDWR | os.O_NONBLOCK)

blue_addr = ['48:2C:A0:23:29:DA','F4:60:E2:2E:37:1B','34:D7:12:9F:42:CD','94:65:2D:B2:BA:0C']
blue_name = ['yoooo','赵泽浩的小米手机','坚果 R1',"ZjeuhPiung's OnePlus5"]

now_level = 0

def loadRecord(addr):
    http = urllib3.PoolManager()
    try:
    	r = http.request('GET', 'http://192.168.43.128:5000/api/loadRecord?device_addr='+ addr)
    	print(r.data)
    	jsondata = json.loads(r.data.decode('utf-8'))
    	return int(jsondata['to_level'])
    except:
        print('network error')
        return 0

def write_new_device(device):
    s = "NULL"
    try :
        s = os.read(wf, 256)
    except  :
        print(s)
    else :
        print(s)
    os.write(wf, bytes(json.dumps(device), encoding = "utf8"))     ##写入目前的蓝牙列表


print("looking for nearby devices...")
j = 0
nearby_devices = []
while 1:    
    print("scan "+ str(j) +" times")
    nearby_devices.append(bluetooth.discover_devices(duration=1, lookup_names = True))
    print("found %d devices" % len(nearby_devices))
    
    new_device_count = 0
    new_device = []
    for device in nearby_devices[j]:
        if not device in nearby_devices[j-1]:
            new_device.append(device)
            new_device_count += 1
    j += 1

    if (new_device_count == 0):
        continue

    print("有新设备进入电梯")
    for device in new_device:
        if(not device[0] in blue_addr):
            continue
        print(device[0] + " " + device[1])
        write_new_device(device)
        to_level = loadRecord(device[0])
        if to_level == 0 :
            print("不去任何楼层")
            continue
        print("前往楼层 " + str(to_level))
        print(lift.goto(to_level))
        ###调用电梯控制接口
        





        
