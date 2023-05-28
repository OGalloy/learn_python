#В большой текстовой строке подсчитать количество встречаемых слов 
#и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. 
#За основу возьмите любую статью из википедии или из документации к языку.



def count_words(raw_string: str):
    return len(raw_string.split(" "))

def get_words_set(raw_string: str):
    words_dict = {}
    words = raw_string.split(" ")
    for word in words:
        if word in words_dict.keys():
            words_dict[word] +=1
        else:
            words_dict[word] = 1
    words = []
    for key in words_dict:
        if words_dict[key] > 10:
            words.append(key)
    return  words



if __name__ == "__main__":
    raw_string = "hello hello end"
    print(count_words(new_string))
    print(get_words_set(new_string))