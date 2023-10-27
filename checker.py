from flask import Flask, request, render_template
import requests

# how to use flask?
app = Flask(__name__)

@app.route("/analyze", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        
        response = requests.post("https://api.sapling.ai/api/v1/aidetect", json={
            "key": "OGE1TGHIQLUHAABHHHZ84NVZ5RUIMGPQ",
            "text": text
        })
        
        data = response.json()
        return render_template("Checker.html", data=data)

    return render_template("Checker.html")