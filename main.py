# API = 'd39e0e39d9f7fa075616a590965fe979'
import requests
from pprint import pprint
import json
from datetime import datetime

parametrs = {
    'appid': 'd39e0e39d9f7fa075616a590965fe979',
    'units': 'metric',
    'lang': 'ru'
}
json_data = []


def weather_forecat(city):
    while True:
        parametrs['q'] = city
        code_to_smile = {
            'Clear': 'Ясно 🌞',
            'Clouds': 'Облачно ⛅',
            'Rain': 'Дождь 🌧',
            'Dreezle': 'Дождь ☔🚿🌧',
            'Thunderstorm': 'Гроза 🌩',
            'Snow': 'Снег 🌨❄',
            'Mist': 'Туман 🌫😖'

        }
        if city == 'stop':
            with open('weather.json', mode='w', encoding='UTF-8') as file:
                json.dump(json_data, file, ensure_ascii=False, indent=4)
            break
        try:
            data = requests.get('https://api.openweathermap.org/data/2.5/weather', params=parametrs).json()
            # pprint(data)

            temperatura = data['main']['temp']
            humidity = data['main']['humidity']
            country = data['sys']['country']
            weather = data['weather'][0]['main']
            wind = data['wind']['deg']
            wind_speed = data['wind']['speed']
            timezone = data['timezone']
            sunrise = datetime.utcfromtimestamp(int(data['sys']['sunrise']) + int(timezone)).strftime(
                '%d-%m-%Y %H:%M:%S')
            sunset = datetime.utcfromtimestamp(int(data['sys']['sunset']) + int(timezone)).strftime('%d-%m-%Y %H:%M:%S')

            if weather in code_to_smile:
                wd = code_to_smile[weather]
            else:
                wd = 'Надо будет самому псомотреть что там! 😅'

            return (f'''
            страна: {country}, часовой пояс - {datetime.utcfromtimestamp(int(data['timezone'])).strftime('%H:%M:%S')},
            температра в городе: {city} - {temperatura} градусов по цельсию,
            погода -  {wd},
            влажность - {humidity} %,
            ветер - {wind_speed} м/с, в направлении {wind} градусов относительно севера,
            восход - {sunrise},
            закат - {sunset}
        ''')
            json_data.append({
                'страна': country,
                'город': city,
                'часовой пояс': timezone,
                'температра в городе': temperatura,
                'погода': weather,
                'влажность': humidity,
                'ветер': wind_speed,
                'направление ветра': wind,
                'восход': sunrise,
                'закат': sunset,
            })

        except:
            return ('Вы ввели не верный город, повторите снова!')
