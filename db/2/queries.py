from model import Salary

from sqlalchemy.sql import func

from db import db_session
from sqlalchemy import desc


def top_salary(num_rows):
    top_salary = Salary.query.order_by(Salary.salary.desc()).limit(num_rows)
    for salary in top_salary:
        print(f'З/п {salary.salary}')


def salary_by_city(city_name):
    top_salary = Salary.query.filter(Salary.city == city_name)\
        .order_by(Salary.salary.desc())
    print(city_name)
    for salary in top_salary:
        print(f'З/п {salary.salary}')

def top_salary_by_email_domain(domain_name, num_rows):
    top_salary = Salary.query.filter(Salary.email.like(f"%{domain_name}"))\
        .order_by(Salary.salary.desc()).limit(num_rows)
    print(domain_name)
    for salary in top_salary:
        print(f'З/п {salary.salary}')

def average_salary():
    result = db_session.query(func.avg(Salary.salary)).scalar()
    print(f"Средняя зарплата {result:.2f}")

def distinct_cities():
    cities_count = db_session.query(Salary.city).group_by(Salary.city).count()
    print(f"В базе {cities_count} городов")

def top_average_salary_by_city(num_rows):
    avg_salary = db_session.query(
        Salary.city,
        func.avg(Salary.salary).label('avg_salary')
    ).group_by(Salary.city).order_by(desc('avg_salary')).limit(num_rows)
    for city, salary in avg_salary:
        print(f"Город: {city}, средняя з/п: {salary:.f}")

if __name__ == '__main__':
    top_average_salary_by_city(10)