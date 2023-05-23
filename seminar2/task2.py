#Напишите программу, которая получает целое число
#и возвращает его шестнадцатеричное строковое представление.
#Функцию hex используйте для проверки своего результата.

hex_numbers = {0: "0",  1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",\
                10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}

def int_to_hex(number: int):
    hex_number = ""
    while number != 0:
        hex_number += hex_numbers[number % 16]
        number //= 16
    return "0x" + hex_number[::-1]

if __name__ == "__main__":
    test_decimal_numbers = [143, 2345, 15983, 902834]
    print("Тестирование программы преобразования decimal числа в hex формат")
    for n in test_decimal_numbers:
        print(int_to_hex(n) + " сравниваем с " + hex(n))
        print("результат: " + str(int_to_hex(n) == hex(n)))
