import requests

def weather_by_city(city_name: str):
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'

    params = {
        'key': 'd901c5ac48c146ed873144744230503',
        'q': city_name,
        'format': 'json',
        'num_of_days': '1',
        'lang': 'ru'
    }

    try:
        result = requests.get(weather_url, params=params)
        result.raise_for_status()
        weather = result.json()

        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except IndexError: 
                    return False
    except(requests.RequestException, ValueError):
        print('Connection error')
        return False
    return False

if __name__ == "__main__":
    w = weather_by_city('Cherepovets')
    print(w)