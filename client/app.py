#!venv/bin/python
import csv, requests, os

deviceId = 'device01'
fileName = deviceId + '.csv'
upstreamNode = 'http://127.0.0.1:5000'
sendUrl = upstreamNode + '/api/v1.0/receive'

#@app.route('/api/v1.0/receive', methods=['POST'])
#        abort(400)
#        return jsonify({'status': 'ok'}), 201
#        return jsonify({'status': 'unauthorized'}), 401

def readSensor(deviceId):
    salinityData = '45%'
    tempData = '3.14159'
    return [deviceId, salinityData, tempData]

def storeData(fileName, sensorData):
    with open(fileName, 'a', newline='') as csvfile:
        #logWriter = csv.writer(csvfile, delimiter=',', quotechar='', quoting=csv.QUOTE_MINIMAL)
        logWriter = csv.writer(csvfile, delimiter=',')
        logWriter.writerow(sensorData)

def postData(fileName, sendUrl):
    files = {'file': (fileName, open(fileName, 'rb'))}
    r = requests.post(sendUrl, files=files)
    if r.status_code == requests.codes.ok:
        prevFile = 'prev' + fileName
        os.remove(prevFile)
        os.rename(fileName, prevFile)

if __name__ == '__main__':
    storeData(fileName, readSensor(deviceId))
    postData(fileName, sendUrl)
