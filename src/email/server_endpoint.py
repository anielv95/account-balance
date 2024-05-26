from flask import Flask
from flask import request
from flask import jsonify
import server as s

app = Flask("email")


@app.route("/send-email", methods=["POST"])
def predict():
    customer = request.get_json()

    result = s.send_email(customer)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
