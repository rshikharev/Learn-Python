import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')

WEATHER_DEFAULT_CITY = "Cherepovets"
WEATHER_API_KEY = "d901c5ac48c146ed873144744230503"
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'