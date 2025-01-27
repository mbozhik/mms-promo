import requests
import time
import random
import string

# URL API для отправки промо-кодов
url = "https://www.mms-promo.ru/backend/api/registerCode"

# Заголовки запроса
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ru,en;q=0.9,ro;q=0.8",
    "connection": "keep-alive",
    "content-type": "application/json; charset=UTF-8",
    "cookie": "PHPSESSID=46c6088bffe0793e78b1994921f1ce81; source=62cd48e2438eb9523d89f623e0e68e5a7a5865402db8cfd804a1f2c2dc3a2be3a%3A2%3A%7Bi%3A0%3Bs%3A6%3A%22source%22%3Bi%3A1%3Bs%3A2%3A%22vk%22%3B%7D; _identity=6026ef8237cc3966ca1bb0ff74d913fb361c9d2165cb1ed75a040dca0b0cbc4ba%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A50%3A%22%5B10446%2C%22wRYw1pnNjJh6lRZq-c6Ej0z3NoHVqi0L%22%2C2592000%5D%22%3B%7D; _csrf=8701f9c4bdb7df82121845c2baec9068be5fb14efa32490adacff838a7daf0c0a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22bkC2V5dmrse4q2aD0FdjSD4CLEkfMAwk%22%3B%7D",
    "host": "www.mms-promo.ru",
    "origin": "https://www.mms-promo.ru",
    "referer": "https://www.mms-promo.ru/",
    "sec-ch-ua": '"Chromium";v="130", "YaBrowser";v="24.12", "Not?A_Brand";v="99", "Yowser";v="2.5"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36",
    "x-auth-token": "wRYw1pnNjJh6lRZq-c6Ej0z3NoHVqi0L"
}

# Функция для генерации случайного промо-кода
def generate_promo_code(length=12):
    # Используем буквы (верхний регистр) и цифры
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Функция для отправки промо-кода
def send_promo_code(code):
    # Тело запроса с промо-кодом
    data = {"code": code}
    try:
        # Отправка POST-запроса
        response = requests.post(url, headers=headers, json=data)
        # Возвращаем статус код и ответ сервера
        return response.status_code, response.json()
    except requests.exceptions.RequestException as e:
        # Обработка ошибок (например, проблемы с сетью)
        return None, str(e)

# Основной код
if __name__ == "__main__":
    while True:
        # Генерация нового промо-кода
        promo_code = generate_promo_code()
        print(f"Проверяем промо-код: {promo_code}")

        # Отправка промо-кода и получение ответа
        status_code, response_data = send_promo_code(promo_code)
        if status_code == 200:
            print(f"Промо-код: {promo_code}, Статус: {status_code}, Ответ: {response_data}")
        else:
            print(f"Промо-код: {promo_code}, Ошибка: {status_code}, Ответ: {response_data}")

        # Задержка в 10 секунд перед следующим запросом
        time.sleep(10)