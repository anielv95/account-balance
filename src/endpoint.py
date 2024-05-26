from flask import Flask
from flask import request
from flask import jsonify
import processing as p

app = Flask("processing")


@app.route("/processing", methods=["POST"])
def predict():
    customer = request.get_json()

    result = p.calculate_values(customer["account"], customer["email"], customer["df"])

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
