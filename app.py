from flask import Flask, render_template, request
from ai_agent import generate_resume

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    user_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "phone": request.form["phone"],
        "location": request.form["location"],
        "linkedin": request.form["linkedin"],
        "github": request.form["github"],
        "education": request.form["education"],
        "skills": request.form["skills"],
        "projects": request.form["projects"],
        "experience": request.form["experience"],
        "certifications": request.form["certifications"],
        "languages": request.form["languages"],
        "objective": request.form["objective"]
    }

    resume = generate_resume(user_data)

    return render_template(
        "result.html",
        resume=resume
    )


if __name__ == "__main__":

  from flask import Flask, render_template, request
  from ai_agent import generate_resume

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    user_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "phone": request.form["phone"],
        "location": request.form["location"],
        "linkedin": request.form["linkedin"],
        "github": request.form["github"],
        "education": request.form["education"],
        "skills": request.form["skills"],
        "projects": request.form["projects"],
        "experience": request.form["experience"],
        "certifications": request.form["certifications"],
        "languages": request.form["languages"],
        "objective": request.form["objective"]
    }

    resume = generate_resume(user_data)

    return render_template(
        "result.html",
        resume=resume
    )


if __name__ == "__main__":

    app.run(debug=True)