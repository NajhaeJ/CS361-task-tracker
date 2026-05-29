from flask import Flask, request, jsonify

app = Flask(__name__)

user_records = dict()

@app.route("/send_user_data", methods=["POST"])
def handle_send_user_data():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "POST body could not be parsed as json"}), 400
    if "key" not in data:
        return jsonify({"error": "request has no key"}), 400
    if "data" not in data:
        return jsonify({"error": "request has no data"}), 400

    user_records[data["key"]] = data["data"]

    return jsonify({"message": "Data sent successfully"}), 200

@app.route("/get_user_data", methods=["POST"])
def handle_get_user_data():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "POST body could not be parsed as json"}), 400

    if "key" not in data:
        return jsonify({"error": "request has no key"}), 400

    if data["key"] not in user_records:
        return jsonify({"error": "key not found"}), 404

    return jsonify({
        "message": "Data retrieved successfully",
        "data": user_records[data["key"]]
    }), 200


if __name__ == '__main__':
    app.run(debug=True)