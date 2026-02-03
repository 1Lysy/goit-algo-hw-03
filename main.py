from datetime import datetime


def get_days_from_today(date):
    
    today = datetime.today().date()
    try:
        str_to_date = datetime.strptime(date, '%Y-%m-%d').date()

        difference = (today - str_to_date).days
        return difference
    except ValueError:
        print('Формат дати не співпадає! Потрібний формат: "РРРР-ММ-ДД"')
        
result = get_days_from_today('2021-10-09')
print('Різниця в днях: ', result)