# ProfileFact API Project
## A simple RESTful API endpoint that returns your profile information along with a random cat fact

### Features
- Dynamic `/me` endpoint that returns JSON data
- Includes:
  - Status
  - User information (name, email, stack)
  - Current UTC timestamp (ISO 8601 format)
  - Random cat fact (fetched live from https://catfact.ninja/fact)

  ### My Stack
- Python
- Flask

## How to Run Locally

-Clone this repository

git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>


-Create a virtual environment (recommended)

python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


-Install dependencies

pip install -r requirements.txt


-Run the Flask app

python app.py


-or if your file is named something else (like profile_endpoint.py):

python profile_endpoint.py


-Access the app
-Open your browser and go to 👉🏽 http://127.0.0.1:5000/me
