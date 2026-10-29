# AI Cybersecurity Career Copilot

A student-friendly Flask web app that recommends cybersecurity career paths and creates a starter 8-week roadmap based on a user's interests and experience level.

## Features
- Interest and experience questionnaire
- Top three career-path recommendations
- Role-specific core skills
- Eight-week learning roadmap
- Print / Save as PDF
- Ethical-use reminder

## Important note
This first version uses a transparent rule-based recommender, not a trained AI model. It can be extended with an LLM API, user accounts, progress tracking, quizzes, and curated course links.

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Create and activate a virtual environment (recommended).
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the app:
   ```bash
   python app.py
   ```
6. Visit `http://127.0.0.1:5000` in your browser.

## Project structure
```text
ai_cybersecurity_career_copilot/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── roles.json
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Safe-use guidance
Only test devices, networks, and applications you own or have explicit permission to assess. Use legal training labs and CTFs for hands-on practice.
