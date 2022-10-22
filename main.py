import requests
from pprint import pprint
from datetime import datetime
import psycopg2

parameters = {
    'appid': '137d62f3c460fac41edca5930e84af7c',
    'units': 'metric',
    'lang': 'ru'
}

while True:
    city = input('Введите город: ')
    parameters['q'] = city
    try:
        data = requests.get('https://api.openweathermap.org/data/2.5/weather', params=parameters).json()
        pprint(data)
        city_name = data['name']
        temp = data['main']['temp']
        wind = data['wind']['speed']
        description = data['weather'][0]['description']
        timezone = data['timezone']
        dt = datetime.fromtimestamp(data['dt']).strftime('%H:%M:%S')
        sunrise = datetime.fromtimestamp(data['sys']['sunrise'] - 18000 + timezone ).strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(data['sys']['sunset'] - 18000 + timezone  ).strftime('%H:%M:%S')

        text = f'''{dt}
В городе \033[31m{city_name}\033[0m сейчас {description}
Температура: {temp} °C
Скорость ветра: {wind} м/с
Раccвет: {sunrise}
Закат: {sunset}'''
        print(text)
        database = psycopg2.connect(
            database='ls4',
            host='localhost',
            user='postgres',
            password='123456'
        )
        cursor = database.cursor()

        cursor.execute(f'''
        INSERT INTO weather(city, temp, wind, sunrice, sunset) VALUES
        (%s, %s, %s, %s, %s);
        ''', (city_name, temp, wind, sunrise, sunset))
        database.commit()
        database.close()
    except:
        text = '''Нет такого города. Попробуйте снова'''
        print(text)


