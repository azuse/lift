from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

@app.route('/api/setBinding',methods=['GET'])
def setBinding():
    return jsonify({'setBinding': 'ok',})

@app.route('/api/saveRecord',methods=['GET'])
def saveRecord():
    return jsonify({'saveRecord': 'ok'})

@app.route('/api/loadRecord',methods=['GET'])
def loadRecord():
    device_addr = request.args.get('device_addr')
    if device_addr == "48:2C:A0:23:29:DA":
        return jsonify({'to_level': '3'})
    elif device_addr == "F4:60:E2:2E:37:1B":
        return jsonify({'to_level': '4'})
    else:
        return jsonify({'to_level': '0'})

@app.route('/api/getDeviceList',methods=['GET'])
def getDeviceList():
    return jsonify([{
        "device_addr":"48:2C:A0:23:29:DA",
        "device_name":"李中猫的🔨手机",
        "from_level":1,
        "to_level":3,
    },{
        "device_addr":"F4:60:E2:2E:37:1B",
        "device_name":"王伟国的 iPhone XS Max",
        "from_level":1,
        "to_level":4,
    }])
