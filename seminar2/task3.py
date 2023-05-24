#task3
#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
#Программа должна возвращать сумму и произведение* дробей. 
#Для проверки своего кода используйте модуль fractions.

from fractions import Fraction
from decimal import *


if __name__ == "__main__":
    print("Эта программа для расчёта произведения и суммы двух дробных чисел.")
    print("Формат вводимых данных: \"a/b\"")
    while True:
        num1 = input("Введите первое число: ")
        num2 = input("Введите второе число: ")
        summary = Fraction(num1) + Fraction(num2)
        multiply = Fraction(num1) * Fraction(num2)
        print("Результаты вычислений:")
        print(f"{num1} + {num2} = {summary}")
        print(f"{num1} * {num2} = {multiply}")


