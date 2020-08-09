#!venv/bin/python
import csv, requests, os

deviceId = 'device01'
localFileName = 'local-data-log.csv'
remoteFileName = deviceId + '.csv'
upstreamNode = 'http://127.0.0.1:5000'
sendUrl = upstreamNode + '/api/v1.0/receive'
DEBUG = True

#@app.route('/api/v1.0/receive', methods=['POST'])
#        abort(400)
#        return jsonify({'status': 'ok'}), 201
#        return jsonify({'status': 'unauthorized'}), 401

def readSensor(deviceId):
    salinityData = '45%'
    tempData = '3.14159'
    logData = [deviceId, salinityData, tempData]

    if DEBUG: print(logData) 
    return logData

def storeData(localFileName, sensorData):
    with open(localFileName, 'a', newline='') as csvfile:
        #logWriter = csv.writer(csvfile, delimiter=',', quotechar='', quoting=csv.QUOTE_MINIMAL)
        logWriter = csv.writer(csvfile, delimiter=',')
        logWriter.writerow(sensorData)
    
    if DEBUG: print('Wrote ' + str(sensorData) + " to " + localFileName)

def postData(localFileName, remoteFileName, sendUrl):
    files = {'file': (remoteFileName, open(localFileName, 'rb'))}
    r = requests.post(sendUrl, files=files)

    if DEBUG: print('POST status code ' + str(r.status_code))
    if r.status_code == requests.codes.ok:
        prevFile = 'prev-' + localFileName
        os.remove(prevFile)
        os.rename(localFileName, prevFile)

if __name__ == '__main__':
    storeData(localFileName, readSensor(deviceId))
    postData(localFileName, remoteFileName, sendUrl)
