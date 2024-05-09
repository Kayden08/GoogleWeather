from datetime import datetime
import requests
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
    # city_name = data['city']['name']
    # city_population = data['city']['population']
    # print('city_name')
    # print('city_population')



    forecast_list = data['list']
    index = 0
    forecast_data = []
    while index < len(forecast_list):

        dt_txt = forecast_list[index]['dt_txt']
        temp = forecast_list[index]['main']['temp']
        icon = forecast_list[index]['weather'][0]['icon']
        description = forecast_list[index]['weather'][0]['description']
        index += 8

        # Convert the string to a datetime object
        date_object = datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S')
        # Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
        day_of_week = date_object.weekday()
        print(day_of_week)
        # You can also get the day name
        day_name = date_object.strftime('%A')
        print(day_name)
        # Added dictionary to store dt_txt. day_name, temp etc
        thisdict = {
            'dt_txt': dt_txt,
            'day_of_week': day_name,
            'temp': temp,
            'icon': 'http://openweathermap.org/img/w/' + icon + '.png',
            'description': description
        }

        forecast_data.append(thisdict)
        print(forecast_data)

        return render_template('home.html', forecast_data=forecast_data)


if __name__ == '__main__':
    app.run(debug=True)
