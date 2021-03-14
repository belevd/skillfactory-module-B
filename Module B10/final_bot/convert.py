from extensions import APIException, Converter


def convert(text):
    try:
        textlist = text.split()
        if len(textlist) > 3:
            raise APIException('Слишком много параметров!')
            return 'Ошибка в запросе! Формат ввода неверный!'
        if len(textlist) < 3:
            raise APIException('Слишком мало параметров!')

        result, base, quote, amount = Converter.get_price(textlist[0], textlist[1], textlist[2])
    except APIException as err:
        return f'Ошибка пользователя.\n{err}'
    except Exception as err:
        return f"Ошибка сервера! Бот не сможет обработать команду. Произошла ошибка:\n{err}"

    return f'Цена {round(amount, 2)} {base} в {quote} - {round(result, 2)}'

