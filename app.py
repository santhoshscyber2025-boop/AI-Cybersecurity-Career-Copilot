from flask import Flask, render_template, request
from pathlib import Path
import json

app = Flask(__name__)
DATA_FILE = Path(__file__).parent / "data" / "roles.json"

with open(DATA_FILE, encoding="utf-8") as f:
    ROLES = json.load(f)

SKILLS = {
    "Networking": ["TCP/IP", "DNS", "HTTP/HTTPS", "subnetting", "Wireshark"],
    "Linux": ["Linux CLI", "permissions", "processes", "logs", "bash basics"],
    "Programming": ["Python basics", "Git", "scripting", "JSON", "debugging"],
    "Security": ["CIA triad", "authentication", "MFA", "least privilege", "threat modeling"],
    "Web Security": ["HTTP requests", "cookies/sessions", "OWASP Top 10", "input validation"],
    "SOC": ["SIEM basics", "log analysis", "alert triage", "incident reports"],
    "Cloud": ["IAM", "security groups", "logging", "shared responsibility"],
}

def recommend_role(interests, level):
    scored = []
    for role in ROLES:
        score = sum(1 for interest in interests if interest in role["interests"])
        if level == role["level"] or level == "Any":
            score += 1
        scored.append((score, role))
    return sorted(scored, key=lambda item: item[0], reverse=True)[:3]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        interests = request.form.getlist("interests")
        level = request.form.get("level", "Beginner")
        goal = request.form.get("goal", "").strip()
        recommendations = recommend_role(interests, level)
        role_names = [role["name"] for _, role in recommendations]
        suggested_skills = []
        for role in recommendations:
            for skill in role[1]["skills"]:
                if skill not in suggested_skills:
                    suggested_skills.append(skill)
        result = {
            "goal": goal,
            "recommendations": [role for _, role in recommendations],
            "skills": suggested_skills[:8],
            "roadmap": [
                {"week": "Weeks 1–2", "title": "Build foundations", "task": "Study networking, Linux commands, and basic security concepts. Keep short notes."},
                {"week": "Weeks 3–4", "title": "Practice safely", "task": "Use legal labs such as beginner CTFs or a local virtual lab. Never test systems without permission."},
                {"week": "Weeks 5–6", "title": "Create a portfolio", "task": "Publish a small lab write-up, a log-analysis exercise, or a Python defensive script."},
                {"week": "Weeks 7–8", "title": "Prepare for opportunities", "task": "Update your resume, practice explaining projects, and apply for beginner-friendly internships."}
            ]
        }
    return render_template("index.html", result=result, skill_groups=SKILLS)

if __name__ == "__main__":
    app.run(debug=True)
