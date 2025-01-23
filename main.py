from flask import Flask, request, jsonify
from utils.storage import Storage
from agents.details import DietFitnessAgent
from agents.diet import GeminiAPIAgent
from agents.yt import YouTubeRecommenderAgent
from agents.tracker import TrackerAnalyzerAgent

# Initialize Flask app
app = Flask(__name__)

# Initialize Custom Storage
storage = Storage()

# Helper function to load or create user profile
def get_or_create_user_profile(user_id):
    user_data = storage.load(f"{user_id}_profile.json")
    if not user_data:
        diet_agent = DietFitnessAgent()
        user_data = diet_agent.collect_user_inputs()
        user_data["user_id"] = user_id
        storage.save(f"{user_id}_profile.json", user_data)

        # Generate diet plan
        gemini_agent = GeminiAPIAgent()
        diet_plan = gemini_agent.generate_diet_plan(user_data)
        user_data["diet_plan"] = diet_plan
        storage.save(f"{user_id}_profile.json", user_data)
    return user_data

# API Endpoint: User Login/Profile Creation
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user_id = data.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    user_data = get_or_create_user_profile(user_id)
    return jsonify({"message": f"Welcome back, {user_id}!", "user_data": user_data})

# API Endpoint: View Diet Plan
@app.route('/diet-plan', methods=['GET'])
def view_diet_plan():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    user_data = storage.load(f"{user_id}_profile.json")
    if not user_data:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"diet_plan": user_data.get("diet_plan", "No diet plan found.")})

# API Endpoint: Track Daily Logs
@app.route('/track-logs', methods=['POST'])
def track_logs():
    data = request.json
    user_id = data.get("user_id")
    logs_data = data.get("logs")  # Get logs data from the request

    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    user_data = storage.load(f"{user_id}_profile.json")
    if not user_data:
        return jsonify({"error": "User not found"}), 404

    tracker_agent = TrackerAnalyzerAgent()
    logs = tracker_agent.collect_daily_logs(logs_data)  # Pass logs data

    if not logs:
        return jsonify({"message": "No logs provided. Please enter today's logs."}), 400

    # Initialize logs as a list if it doesn't exist
    if "logs" not in user_data:
        user_data["logs"] = []

    # Append the new log to the logs list
    user_data["logs"].append(logs)
    storage.save(f"{user_id}_profile.json", user_data)

    # Analyze progress
    analysis_result = tracker_agent.analyze_progress(logs, user_data)

    return jsonify({
        "message": "Daily logs saved successfully!",
        "logs": logs,
        "analysis": analysis_result
    })

# API Endpoint: Get Exercise Recommendations
@app.route('/exercise-recommendations', methods=['GET'])
def get_exercise_recommendations():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    user_data = storage.load(f"{user_id}_profile.json")
    if not user_data:
        return jsonify({"error": "User not found"}), 404

    youtube_agent = YouTubeRecommenderAgent()
    videos = youtube_agent.recommend_videos(user_data)  # Pass user_data (a dictionary)
    return jsonify({"videos": videos})

# API Endpoint: View Weekly Progress Report
@app.route('/weekly-report', methods=['GET'])
def view_weekly_report():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    user_data = storage.load(f"{user_id}_profile.json")
    if not user_data:
        return jsonify({"error": "User not found"}), 404

    tracker_agent = TrackerAnalyzerAgent()
    report = tracker_agent.generate_weekly_report(user_data)

    return jsonify({"weekly_report": report})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=5001)