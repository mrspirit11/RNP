# https://ofdata.ru/
import requests
import json


class RNP:
    def __init__(self, inn: str):
        self.inn = inn

    def api(self, api_type='ufs') -> dict:
        """if api_type is ufs
        https://ofdata.ru/api/unfair-suppliers"""

        API_KEY = '349olt5ozgTIPD5tLKwI7A'
        URL = 'https://api.ofdata.ru/alpha/json'
        params = {'key': API_KEY,
                  'object': api_type,
                  'inn': self.inn
                  }
        response = requests.get(URL, params=params)
        response_json = json.loads(response.text)
        return response_json


if __name__ == '__main__':
    from pprint import pprint as pp

    test_api = RNP('7813370716').api()
    pp(test_api)
