import time

from bybit_api_trade.utils.bybit import place_order_limit_mult, place_order_market_mult
from bybit_api_trade.utils.bybit import sell_order_limit_mult, sell_order_market_mult
from bybit_api_trade.utils.bybit import get_balance


def get_user_choice():
    user = input("-----------Bybit Trading Pro V4-----------"
          "\nВыберите действие"
          "\n1. Посмотреть баланс"
          "\n2. Купить по маркету"
          "\n3. Купить по лимиту"
          "\n4. Продать ордер маркет"
          "\n4. Продать ордер лимит"
          "\n5. Выход"
          "\nВыбор:")
    if user == "1":
        get_balance()
        return time.sleep(3), get_user_choice()
    if user == "2":
        symbol = input("Введите символ (например, BTCUSDT): ")
        qty = input("Введите количество: ")
        try:
            qty = float(qty)
            response = place_order_market_mult(symbol, qty)
        except ValueError:
            print("Ошибка: количество должно быть числом.")
            return time.sleep(3), get_user_choice()
        return get_user_choice()
    if user == "3":
        symbol = input("Введите символ (например, BTCUSDT): ")
        qty = input("Введите количество: ")
        price = input("Введите цену: ")
        try:
            qty = float(qty)
            response = place_order_limit_mult(symbol, qty, price)
        except ValueError:
            print("Ошибка: количество должно быть числом.")
            return time.sleep(3), get_user_choice()
        return get_user_choice()
    if user == "4":
        symbol = input("Введите символ который нужно продать (например, BTCUSDT): ")
        qty = input("Введите количество для продажи: ")
        try:
            qty = float(qty)
            response = sell_order_market_mult(symbol, qty)
        except ValueError:
            print("Ошибка: количество должно быть числом.")
            return time.sleep(3), get_user_choice()
        return get_user_choice()
    if user == "5":
        symbol = input("Введите символ для продажи (например, BTCUSDT): ")
        qty = input("Введите количество для продажи: ")
        price = input("Введите цену для продажи: ")
        try:
            qty = float(qty)
            response = sell_order_limit_mult(symbol, qty, price)
        except ValueError:
            print("Ошибка: количество должно быть числом.")
            return time.sleep(3), get_user_choice()
        return get_user_choice()
    if user == "6":
        return get_user_choice()

if __name__ == "__main__":
    get_user_choice()