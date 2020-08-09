#!venv/bin/python

deviceId = 'device01'
sensorData = {} 
fileName = 'dataLog.json'
upstreamNode = '127.0.0.1:5000'
sendUrl = upstreamNode + '/api/v1.0/receive'

@app.route('/api/v1.0/receive', methods=['POST'])
def receiveData():
    if not request.json or not 'deviceId' in request.json:
        abort(400)
    logEntry = {
        'deviceId': request.json['deviceId'],
        'metric': request.json['metric'],
        'data': request.json['data'],
        'timeStamp': '20080805131501'
    }
    if logEntry.deviceId in deviceIds:
        logs.append(logEntry)
        return jsonify({'status': 'ok'}), 201
    else:
        return jsonify({'status': 'unauthorized'}), 401

def readSensor():
    return {
        'metric': 'salinity',
        'data': '3.14159'
    }

def storeData():


if __name__ == '__main__':
    sensorData = readSensor()
    storeData(fileName)
    postData()

