import requests
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():

    api_key = 'b12703d2df47873eaf71613c74db92a2'
    city = 'Adelaide'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q=' + city + '&APPID=' + api_key
    print(url)
    response = requests.get(url)
    data = response.json()
    city_name = data['city']['name']
    city_population = data['city']['population']
    print('city_name')
    print('city_population')

    #'description': data['weather'][0]['description'],

    forecast_list = data['list']
    index = 0
    forecast_list = []
    while index < len(forecast_list):
        dt_txt = (forecast_list[index]['dt_txt'])
        temp = (forecast_list[index]['main']('temp'))
        icon = (forecast_list[index]['weather'][0]('icon'))
        description = (forecast_list[index]['weather'][0]('description'))
        index += 8

        today = datetime.datetime(2017, 10, 20)
        today.get_weekday()

        thisdict = {
            'dt_txt': dt_txt,
            'temp': temp,
            'icon': icon,
            'description': description
        }

        forecast_list.append(thisdict)
    print(forecast_list)


    forecast_list = ''
    return render_template('home.html', forecast_list=forecast_list)

today = datetime.datetime



if __name__ == '__main__':
    app.run(debug=True)
