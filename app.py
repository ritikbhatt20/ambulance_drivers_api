from flask import Flask, request, jsonify

app = Flask(__name__)

ambulances_list = [{"ambulanceID": 1, "driverName": "Akshay Singh", "latitude": "28.759705", "longitude": "77.500977",
                    "availability": "true", "phoneNo": "6397386678",
                    "walletAddress": "0x62524CCFa73835b4E138caE54984B236454Bac62"},
                   {"ambulanceID": 2, "driverName": "Eeshwar Pandey", "latitude": "28.922418", "longitude": "77.651076",
                    "availability": "true", "phoneNo": "9656354456",
                    "walletAddress": "0x62524CCFa73835b4E138caE54984B236454Bac62"},
                   {"ambulanceID": 3, "driverName": "Shrey Dixit", "latitude": "28.923248", "longitude": "77.641081",
                    "availability": "true", "phoneNo": "9223411297",
                    "walletAddress": "0x62524CCFa73835b4E138caE54984B236454Bac62"}]


@app.route('/')
def home():
    return "Hello World here"


@app.route('/ambulances', methods=['GET', 'POST'])
def ambulances():
    if request.method == 'GET':
        if len(ambulances_list) > 0:
            return jsonify(ambulances_list)
        else:
            'Nothing found', 404

    if request.method == 'POST':
        new_driverName = request.form['driverName']
        new_latitude = request.form['latitude']
        new_longitude = request.form['longitude']
        new_availability = request.form['availability']
        new_phoneNo = request.form['phoneNo']
        ambulanceID = ambulances_list[-1]['ambulanceID'] + 1
        new_walletAddress = request.form['walletAddress']

        new_obj = {
            'ambulanceID': ambulanceID,
            'driverName': new_driverName,
            'latitude': new_latitude,
            'longitude': new_longitude,
            'availability': new_availability,
            'phoneNo': new_phoneNo,
            'walletAddress': new_walletAddress
        }
        ambulances_list.append(new_obj)
        return jsonify(ambulances_list), 201


if __name__ == '__main__':
    app.run(debug=True)
