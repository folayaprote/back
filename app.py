import os
import json
from urllib import response
from flask import Flask, render_template, jsonify, make_response
from bs4 import BeautifulSoup as bs
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/data')
def scraping():
    # username = "guiralesperez"
    # password = "Sakradevanam26"
    # sauce = requests.get("https://www.instagram.com/didiercorreal/followers/", auth=(username, password))
    # sauce = sauce.content
    # soup = bs.BeautifulSoup(sauce, "html.parser")

    url = 'https://social-prote-app.herokuapp.com/'
    myobj = {
        "afi_hash2": {
            "nombre": "Didier Correa",
            "correo": "correalondon@gmail.com",
            "ciudad": "Medellin"
        }
    }

    x = requests.post(url, json=myobj)

    # Base URL for the CREATE endpoint
    BASE_URL = "https://api.humantic.ai/v1/user-profile/create"
    headers = {
        'Content-Type': 'application/json'
    }
    # API Key: required; get the API key from the environment variable or substitute it directly
    API_KEY = "chrexec_4a8836340d45a9d291d69d46611ee98e"
    # Analysis ID: required; User profile link from LinkedIn or, User Email ID
    # or, for document or text, use any unique identifier. We suggest using a value that helps you identify the analysis easily.
    USER_ID = "https://co.linkedin.com/in/didier-correa-londo%C3%B1o-194a4a17b"
    url = f"{BASE_URL}?apikey={API_KEY}&id={USER_ID}"
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    # # print(response.status_code, response.text)
    data = json.loads(response.text)
    print(json.dumps(data, indent=4))

    # Base URL for the FETCH endpoint
    BASE_URL = "https://api.humantic.ai/v1/user-profile"
    headers = {
        'Content-Type': 'application/json'
    }
    # API Key: required; get the API key from the environment variable or substitute it directly
    API_KEY = "chrexec_4a8836340d45a9d291d69d46611ee98e"
    # Analysis ID: required; should be same as the id used to create the analysis
    # or, any unique identifier
    USER_ID = "https://co.linkedin.com/in/didier-correa-londo%C3%B1o-194a4a17b"
    # https://www.linkedin.com/in/camilo-valencia-165993212/en
    # Persona: optional; possible values: "sales", "hiring"
    PERSONA = "sales"
    url = f"{BASE_URL}?apikey={API_KEY}&id={USER_ID}&persona={PERSONA}"
    response = requests.request("GET", url, headers=headers)
    # print(response.status_code, response.text)
    data = json.loads(response.text)
    # d =json.dumps(x, indent=2)
    d2 =json.dumps(data, indent=4)
    return make_response(jsonify(d2), 200)

if __name__ == '__main__':
    app.run( host = os.environ.get('FLASK_IP'))