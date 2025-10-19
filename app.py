from flask import Flask, jsonify #importing the neccessory libaries
from datetime import datetime
import requests
import os

app = Flask(__name__)

@app.route("/me", methods= ['GET'])
def get_profile():
    
    time = datetime.now() #To get get the current datetime
    
    
    try:
        result = requests.get("https://catfact.ninja/fact", timeout=5)
        result.raise_for_status()
        cat_data = result.json()
        cat_fact = cat_data.get("fact", "Currently, there's no available fact.")
    except requests.exceptions.RequestException:
        cat_fact = "Can't get a Cat Fact at the moment. Please try again later."
    
    
    profile = {
  "status": "success",
  "user": {
    "email": "<ezinneaniugbo@gmail.com>",
    "name": "<Aniugbo Queen-Esther Ezinne>",
    "stack": "<Python/Flask>"
  },
  "timestamp": time.isoformat(),
  "fact": cat_fact
}
    return jsonify(profile), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
