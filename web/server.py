from flask import Flask
from weather import weather_by_city

app = Flask(__name__)

@app.route('/')
def index():
    weather = weather_by_city('Cherepovets')
    return f"Погода: {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"

if __name__ == "__main__":
    app.run()