# https://ofdata.ru/
import requests
import json


class OrgInfo:
    def __init__(self, inn: str):
        self.inn = inn

    def api_rnp(self, api_type='ufs') -> dict:
        """if api_type is ufs: https://ofdata.ru/api/unfair-suppliers"""
        API_KEY = '349olt5ozgTIPD5tLKwI7A'
        URL = 'https://api.ofdata.ru/alpha/json'
        params = {'key': API_KEY,
                  'object': api_type,
                  'inn': self.inn
                  }
        response = requests.get(URL, params=params)
        response_json = json.loads(response.text)
        return response_json

    def api_egrul(self) -> dict:
        """https://dadata.ru/api/find-party/#usage"""
        API_key = '019d0fea60b1e57c7d0b41d817b47864d0a9697b'
        SERV_URL = 'https://suggestions.dadata.ru/'
        API_URL = 'suggestions/api/4_1/rs/findById/party'
        URL = SERV_URL + API_URL
        headers = {"Authorization": "Token " + API_key}
        params = {'query': self.inn,
                  'count': 10,
                  'kpp': None,
                  'branch_type': 'MAIN',
                  'type': None
                  }
        response = requests.get(URL, headers=headers, params=params)
        response_json = json.loads(response.text)['suggestions'][0]['data']
        return response_json

    def rss_parser(self):
        pass


if __name__ == '__main__':
    from pprint import pprint as pp
    test_api = OrgInfo('7813370716').api_egrul()
    pp(test_api)
