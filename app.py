from flask import Flask, jsonify, make_response, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def coronadata():
    url = "https://reqres.in/api/users/2"
    headers = {}
    response = requests.request("GET", url, headers=headers)
    #res = json.dumps(response)
    return(response.text)

@app.route('/dashboard')
def cardsDashboard():
    # url = "https://reqres.in/api/users/2"
    # headers = {}
    # response = requests.request("GET", url, headers=headers)
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
    headers = {
      'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "Enter Your key"
    }
    response = requests.request("GET", url, headers=headers).json()
    headline = "COVID 19 Dashboard!"
    #return response.text
    return render_template('dashboard.html', headline = headline,response=response)

@app.route('/indiaDashboard')
def indiaDashboard():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
    headers = {
      'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "Enter Your key"
    }
    response = requests.request("GET", url, headers=headers).json()
    headline = "COVID 19 India Dashboard!"
    return render_template('indiadashboard.html', headline = headline,response=response)
