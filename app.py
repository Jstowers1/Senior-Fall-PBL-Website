from flask import Flask, request, render_template
import requests

# how to use flask?
app = Flask(__name__, template_folder='templates')

@app.route("/analyze", methods=['GET'])
def display_form():
  return render_template('Input.html')

@app.route('/analyze', methods=["POST"])
def analyze_text():
    try:
        if request.method == "POST":
            # text = request.form["text"]
            text = "This is hardcoded text that shows that I am properly working."
            
            response = requests.post("https://api.sapling.ai/api/v1/aidetect", json={
                "key": "OGE1TGHIQLUHAABHHHZ84NVZ5RUIMGPQ",
                "text": text
            })
            print(response.json())
            data = response.json()
            return render_template("Checker.html", data=data)
    except:
        print("Error!!!!")
        return "Error"

    return render_template("Checker.html")