#!venv/bin/python
from flask import Flask, request
import os

app = Flask(__name__)

logs = []
deviceIds = ['device01', 'device02', 'device03']

@app.route('/api/v1.0/receive', methods=['POST'])
def receiveData():
    # get the file from client
    uploaded_file = request.files['file']
    fileName = uploaded_file.filename

    # if client filename not empty
    if fileName != '':
        # parse the filename from the extension
        file_deviceID = os.path.splitext(fileName)[0]
        # filename porttion should be a deviceId
        if file_deviceID not in deviceIds:
            abort(400)
        else:
            # finally success.  deal with the incoming file
            # TODO perhaps crack open the file and add timestamps?
            # TODO change the save directory or filename before saving?
            uploaded_file.save(fileName)
            # TODO return the proper success status
            return(200)
    else:
        # filename was empty string.  bail out
        abort(400)

if __name__ == '__main__':
    app.run(debug=True)

