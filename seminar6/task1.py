#Создайте модуль и напишите в нём функцию, 
#которая получает на вход дату в формате DD.MM.YYYY
#Функция возвращает истину, если дата может существовать или ложь, 
#если такая дата невозможна.
#Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
#Весь период (1 января 1 года - 31 декабря 9999 года) 
#действует Григорианский календарь. 
#Проверку года на високосность вынести в отдельную защищённую функцию.
#В модуль с проверкой даты добавьте возможность запуска в терминале 
#с передачей даты на проверку.

from datetime import datetime
from sys import argv

__all__ = ['check_year', 'date_validator']

def _check_leap_year(date: str) -> bool:
    date = int(date.split(".")[2])
    if date % 4 == 0 or date % 100 == 0:
        return True
    return False


def check_year(date: str) -> bool:
    try:
        datetime.strptime(date, "%d.%m.%Y.%H.%M.%S")
    except ValueError:
        return False
    return True

def date_validator(date: str) -> str:
    if check_year(date) == True:
        if _check_leap_year(date):
            return "Дата корректна. Год является високосным."
        else: 
            " Дата корректна. Год Не является высокосным."
    else:
        return "Дата заполнена некорректно"

if __name__ == "__main__":
    print(argv)
    print(date_validator(argv [1]))
