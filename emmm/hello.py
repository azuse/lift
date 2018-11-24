from flask import Flask,jsonify,request
import sqlite3



app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

@app.route('/api/setBinding/<address>/<username>/<tolevel>',methods=['GET'])
def setBinding(address,username,tolevel):
    conn = sqlite3.connect('user.db')
    print("Opened database successfully")
    c = conn.cursor()
    c.execute("INSERT INTO USER (NAME,LEVEL,ADDRESS) \
      VALUES ('%s', %s, '%s' )"%(username,tolevel,address))
    conn.commit()
    conn.close()
    print("%s,%s,%s"%(username,tolevel,address))
    return jsonify({'setBinding': 'ok'})

@app.route('/api/saveRecord/<string:address>/<string:username>/<int:tolevel>',methods=['GET'])
def saveRecord(username,address,tolevel):
    conn = sqlite3.connect('user.db')
    print("Opened database successfully")
    c = conn.cursor()
    c.execute("INSERT INTO LOG (NAME,LEVEL,ADDRESS) \
      VALUES ('%s', %s, '%s' )"%(username,tolevel,address))
    conn.commit()
    conn.close()
    print("%s,%s,%s"%(username,tolevel,address))
    return jsonify({'saveRecord': 'ok'})

@app.route('/api/loadRecord/<string:device_addr>',methods=['GET'])
def loadRecord(device_addr):
    list={"to_level":0}
    conn = sqlite3.connect('user.db')
    print("Opened database successfully")
    c = conn.cursor()
    cursor=c.execute("SELECT LEVEL from user where address='%s'"%device_addr)
    for row in cursor:
        list={"to_level":row[0]}
    conn.close()
    return jsonify(list)

    # device_addr = request.args.get('device_addr')
    # if device_addr == "48:2C:A0:23:29:DA":
    #     return jsonify({'to_level': '3'})
    # elif device_addr == "F4:60:E2:2E:37:1B":
    #     return jsonify({'to_level': '4'})
    # else:
    #     return jsonify({'to_level': '0'})

@app.route('/api/getDeviceList',methods=['GET'])
def getDeviceList():
    list=[]
    conn = sqlite3.connect('user.db')
    print("Opened database successfully")
    c = conn.cursor()
    cursor=c.execute("SELECT * from log order by id limit 0,10")
    for row in cursor:
        list.append({
            "device_addr":row[3],
            "device_name":row[1],
            "to_level":row[2],
        })

    conn.close()
    return jsonify(list)
