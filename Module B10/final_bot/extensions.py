import requests
import json

from constants import CURRENCIES, API


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):

        if base == quote:
            raise APIException('Невозможно конвертировать в ту же валюту')

        try:
            base_request = CURRENCIES[base.lower()]
        except KeyError:
            raise APIException(f'Ошибка! Не удалось получить валюту {base}!'
                                      f' Проверьте правильность написания или еще раз ознакомьтесь'
                                      f' со списком по комманде /values')
        try:
            quote_request = CURRENCIES[quote.lower()]
        except KeyError:
            raise APIException(f'Ошибка! Не удалось получить валюту {quote}!'
                                      f' Проверьте правильность написания или еще раз ознакомьтесь'
                                      f' со списком по комманде /values')
        try:
            amount_request = float(amount)
        except ValueError:
            raise APIException(f'Ошибка! Не удалось обработать кол-во {amount}!'
                                      ' Кол-во валюты для конвертации не указано или указано не числом.'
                                      ' Проверьте правильность написания!')

        response = requests.get(f"{API}base={base_request}")
        responsedict = json.loads(response.content)
        result = float(responsedict['rates'][quote_request]) * float(amount_request)
        return [result, base, quote, amount_request]

