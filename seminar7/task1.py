
#Напишите функцию группового переименования файлов. Она должна:
#принимать параметр желаемое конечное имя файлов. 
#При переименовании в конце имени добавляется порядковый номер.
#принимать параметр количество цифр в порядковом номере.
#принимать параметр расширение исходного файла. 
#Переименование должно работать только для этих файлов внутри каталога.
#принимать параметр расширение конечного файла.
#принимать диапазон сохраняемого оригинального имени. 
#Например для диапазона [3, 6] берутся буквы с 3 по 6 
#из исходного имени файла. 
#К ним прибавляется желаемое конечное имя, если оно передано. 
#Далее счётчик файлов и расширение.

from random import choices, randint
from string import ascii_letters, digits


def make_files(extension: str, min_name: int = 6, max_name: int = 30,
               min_size: int = 256, max_size: int = 4096, count: int = 42):
    for _ in range(count):
        name = ''.join(choices(ascii_letters + digits, k=randint(min_name, max_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{extension}', 'wb') as f:
            f.write(data)
