#Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции - 
#функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.

#Задание No6
#Напишите программу банкомат.
#✔ Начальная сумма равна нулю
#✔ Допустимые действия: пополнить, снять, выйти
#✔ Сумма пополнения и снятия кратны 50 у.е.
#✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
#✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
#✔ Нельзя снять больше, чем на счёте
#✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
#операцией, даже ошибочной
#✔ Любое действие выводит сумму денег


class BankAccount:
    operation_counter = 0
    bank_balance = 0
    def withdrow(total: int):
        if BankAccount.bank_balance == 0:
            return print("Баланс равен нулю. Операция снятия не возможна.")
        if BankAccount.bank_balance - total < 0:
            return print("Недопустимая операция. Баланс не может быть меньше ноля.")
        if total % 50 == 0:
            BankAccount.operation_counter += 1
            res = check_total(total)
            BankAccount.bank_balance -= res
            check_operation_counter()
            print_balance()
            return print("Операция выполнена.")
        else:
            return print("Недопустимая операция. сумма снятия толжна быть кратна 50.")

    def top_up(total:int):
        BankAccount.operation_counter += 1
        es = check_total(total)
        BankAccount.bank_balance -= res
        check_operation_counter()
        print_balance()
        return print("Операция выполнена.")

    def acoount_exit():
        exit()

    def check_total(total):
        """Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е."""
        if total * 0.015 > 600:
            return 600
        if total * 0.015 < 30:
            return 30
        return total * 0.015

    def check_operation_counter():
        """"""
        if BankAccount.operation_counter % 3 = 0:
            BankAccount.bank_balance += BankAccount.bank_balance * 0.03

    def print_balance():
        print(f"Баланс равен {BankAccount.bank_balance}")

    def check_bank_balance(total):
        if BankAccount.bank_balance > 5000000:
            return total * 0.1 


if __name__ == "__main__":
    client1 = BankAccount()
    print(BankAccount.bank_balance)
    client1 = BankAccount.bank_balance = 100
    print(BankAccount.bank_balance)
    BankAccount.withdrow(51)
    print(BankAccount.bank_balance)