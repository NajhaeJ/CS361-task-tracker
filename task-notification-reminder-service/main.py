from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/generate_reminder", methods=["POST"])
def handle_generate_reminder():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "POST body could not be parsed as json"}), 400

    if "task_name" not in data:
        return jsonify({"error": "request has no task_name"}), 400

    if "due_date" not in data:
        return jsonify({"error": "request has no due_date"}), 400

    if "completed" not in data:
        return jsonify({"error": "request has no completed status"}), 400

    if data["completed"] == True:
        return jsonify({"message": "Task is already completed. No reminder generated."}), 200

    reminder = f"Reminder: {data['task_name']} is due on {data['due_date']}."

    return jsonify({
        "message": "Reminder generated successfully",
        "reminder": reminder
    }), 200


if __name__ == "__main__":
    app.run(debug=True, port=5001)