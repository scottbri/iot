#!venv/bin/python
from flask import Flask

app = Flask(__name__)

logs = []
deviceIds = ['device01', 'device02', 'device03']

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

if __name__ == '__main__':
    app.run(debug=True)

