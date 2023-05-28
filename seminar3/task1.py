#Дан список повторяющихся элементов. 
#Вернуть список с дублирующимися элементами. 
#В результирующем списке не должно быть дубликатов.

def check_dups(nums: list):
    dups = []
    for x in nums:
        if x in dups:
            continue
        if nums.count(x) > 1:
            dups.append(x)
    return dups

if __name__ == "__main__":
    new_list = [1, 45, 34, 23, 54, 23, 56, 23, 56, 45, 1]
    dups = check_dups(new_list)
    print(dups)