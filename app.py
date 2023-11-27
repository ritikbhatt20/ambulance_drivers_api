from flask import Flask, request, jsonify

app = Flask(__name__)

ambulances_list = [{"ambulanceID": 1, "driverName": "John Doe", "latitude": "37.7749", "longitude": "-122.4194",
                    "availability": "true", "phoneNo": "6397386678"},
                   {"ambulanceID": 2, "driverName": "John Doe", "latitude": "37.7749", "longitude": "-122.4194",
                    "availability": "true", "phoneNo": "6397386678"},
                   {"ambulanceID": 3, "driverName": "John Doe", "latitude": "37.7749", "longitude": "-122.4194",
                    "availability": "true", "phoneNo": "6397386678"}]


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
        ambulanceID = ambulances_list[-1]['ambulanceID']+1

        new_obj = {
            'ambulanceID': ambulanceID,
            'driverName': new_driverName,
            'latitude': new_latitude,
            'longitude': new_longitude,
            'availability': new_availability,
            'phoneNo': new_phoneNo
        }
        ambulances_list.append(new_obj)
        return jsonify(ambulances_list),201


if __name__ == '__main__':
    app.run(debug=True)
