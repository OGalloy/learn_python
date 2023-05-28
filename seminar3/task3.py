#Создайте словарь со списком вещей для похода в качестве ключа 
#и их массой в качестве значения. 
#Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
#Достаточно вернуть один допустимый вариант.



def get_pack(items: dict, backpack_weight: float):
    result = []
    actual_weight = 0
    for key in items:
        actual_weight += items[key]
        if actual_weight > backpack_weight:
            return result
        result.append(items[key])






if __name__ == "__main__":
    items = {"knife": 0.5, "salt": 0.6, "matches": 0.1, "hat": 0.3, "pan": 1, "aidkit": 1.5 }
    backpack_weight = 2
    print(get_pack(items, backpack_weight))





