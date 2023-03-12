from flask import Flask, render_template
from weather import weather_by_city

from python_org_news import get_python_news

app = Flask(__name__)

@app.route('/')
def index():
    weather = weather_by_city('Cherepovets')
    page_title = 'Новости Python'

    news_list = get_python_news()
    print(news_list)

    return render_template('index.html', page_title=page_title, weather=weather, news_list=news_list)
if __name__ == "__main__":
    app.run(debug=True)