import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    api_key = "b12703d2df47873eaf71613c74db92a2"
    city = "Adelaide"
    url = 'https://api.openweathermap.org/data/2.5/forecast?q=' + city + "&appid=" + api_key
    print(url)
    response = requests.get(url)
    data = response.json()
    return render_template("home.html")




    #'description': data['weather'][0]['description'],

# forcast_list = response['list'[0]]
# for forecast is forcast_list:
#     timestamp


if __name__ == '__main__':
    app.run(debug=True)
