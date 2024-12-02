from flask import Flask, request, jsonify
from app.llm_integration import load_model, generate_playbook

app = Flask(__name__)

# Load the model at startup
model = load_model()

@app.route("/generate_playbook", methods=["POST"])
def generate_playbook_route():
    """
    API endpoint to generate a playbook for an incident.
    """
    data = request.json
    if "description" not in data or "severity" not in data:
        return jsonify({"error": "Missing required fields: description, severity"}), 400

    # Generate playbook
    playbook = generate_playbook(data, model)
    return jsonify({"playbook": playbook})
