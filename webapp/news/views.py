from webapp.news.models import News
from flask import Blueprint, current_app,  render_template

from webapp.weather import weather_by_city
blueprint = Blueprint('news', __name__)

@blueprint.route('/')
def index():
    weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    page_title = 'Новости Python'
    news_list = News.query.order_by(News.published.desc()).all()
    return render_template('news/index.html', page_title=page_title, weather=weather, news_list=news_list)
    