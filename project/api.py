import requests
from datetime import datetime

class API:
    def __init__(self, token):
        self.TOKEN = token

    def get_rooms(self):
        """
            Аудитории компании
        """
        headers = {"x-access-token": self.access_token}
        response = self.session.get('https://api.moyklass.com/v1/company/rooms',
                                    headers=headers).json()
        print(f'---------{datetime.now()}')
        return response

    def get_lessons(self, date_from, date_to):
        """
            Возвращает список занятий
            date_from, date_to: Формат даты %Y-%m-%d 2022-09-12
        """
        headers = {"x-access-token": self.access_token}
        response = self.session.get(f'https://api.moyklass.com/v1/company/lessons?date={date_from}&date={date_to}',
                                    headers=headers).json()['lessons']
        return response
    
    def __enter__(self):
        """
            Получаем токен
        """
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})
        self.access_token = self.session.post('https://api.moyklass.com/v1/company/auth/getToken',
                            json={"apiKey": self.TOKEN}).json()['accessToken']
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
            Удаляем access_token
        """
        headers = {"x-access-token": self.access_token}
        response = self.session.post('https://api.moyklass.com/v1/company/auth/revokeToken', headers=headers)
        print(response.status_code)


def time_in_range(start, end, current_from, current_to):
    """
        Интервал времени между датами start и end
    """
    res = start <= current_from < end or start < current_to <= end
    return res

def datetime_format(_datetime):
    """
        Формат даты %Y-%m-%d %H:%M
    """
    return datetime.strptime(_datetime, '%Y-%m-%d %H:%M')


