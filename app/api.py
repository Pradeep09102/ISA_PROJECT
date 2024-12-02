from flask import Flask, request, jsonify
from llm_integration import load_model, generate_playbook
from database import (
    insert_incident, get_incidents, update_incident, delete_incident,
    insert_playbook, get_playbooks, update_playbook, delete_playbook,
    insert_recovery_action, get_recovery_actions, update_recovery_action, delete_recovery_action,
    insert_crisis_communication, get_crisis_communications, update_crisis_communication, delete_crisis_communication,
    insert_incident_log, get_incident_logs, update_incident_log, delete_incident_log,
    get_related_playbook, get_recovery_actions_for_incident, get_crisis_communications_for_incident, get_logs_for_incident,
    update_incident_status, get_incident_by_id
)

app = Flask(__name__)

# Load the LLM model once when the app starts
model = load_model()

# -------------------- INCIDENTS --------------------#

@app.route('/api/incidents', methods=['POST'])
def add_incident():
    data = request.get_json()
    try:
        insert_incident(data)
        return jsonify({"message": "Incident added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -------------------- PLAYBOOKS --------------------
@app.route("/generate_playbook", methods=["POST"])
def generate_playbook_route():
    """
    API endpoint to generate a playbook for an incident.
    """
    data = request.json
    if "description" not in data or "severity" not in data:
        return jsonify({"error": "Missing required fields: description, severity"}), 400

    # Pass the loaded model to generate_playbook function
    try:
        playbook = generate_playbook(data, model)
        return jsonify({"playbook": playbook}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Print all routes
    print("\nAvailable routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint} - {rule}")
    app.run(host="0.0.0.0", port=5002)
