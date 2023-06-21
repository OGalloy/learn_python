import csv
import json
import pickle
import os
from pathlib import Path

def csv_to_json(file_out: Path, file_in: Path) -> None:
    json_list = []
    with open(file_out, 'r+', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            json_dict = {}
            level, user_id, name = row
            json_dict['level'] = int(level)
            json_dict['id'] = user_id.zfill(10)  # .zfill(10) заполняет строку нулями слева до указанной длины
            json_dict['name'] = name.title()  # Метод title() возвращает строку с заглавной первой буквой
            json_dict['hash'] = hash(
                f'{user_id}{name}')  # Функция hash() возвращает хеш-значение объекта, если оно есть
            json_list.append(json_dict)

    with open(file_in, 'w', encoding='utf-8') as f:
        json.dump(json_list, f, indent=2, ensure_ascii=False)

def reader_csv(file: Path) -> str:
    with open(file, 'r', encoding='utf-8') as f_csv:
        return f_csv.read()


def print_pickle(file_csv: str) -> None:
    print(pickle.dumps(file_csv))


def csv_to_pickle(file_csv: Path):
    print_pickle(reader_csv(file_csv))

## json to csv
def reader_json(file: Path) -> dict[str, str, str]:
    json_file = {}
    if os.path.isfile(file):
        with open(file, 'r', encoding='utf-8') as js:
            if os.path.getsize(file) > 0:
                json_file = json.load(js)
    return json_file

def write_csv(json_file: dict, file_out: Path) -> None:
    rows = []
    for level, value in json_file.items():
        for id, name in value.items():
            rows.append({'level': level, 'user_id': id, 'name': name})

    with open(file_out, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['level', 'user_id', 'name']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def json_to_csv(file_in: Path, file_out: Path) -> None:
    write_csv(reader_json(file_in), file_out)


### json to pickle
def get_pickle(name: dict, json_data: Path) -> None:
    with open(json_data, 'wb') as f_pic:
        pickle.dump(name, f_pic)

def reader_json(file: Path) -> dict[str, str, str]:
    with open(file, 'r', encoding='utf-8') as f_js:
        json_file = json.load(f_js)
    return json_file

def json_to_pickle(file_in: Path, file_out: Path) -> None:
    get_pickle(reader_json(file_in), file_out)

###pickle to csv
def read_pickle(fail: Path) -> list[dict]:
    with open(fail, 'rb') as f_pkl:
        data_lst = pickle.load(f_pkl, encoding='utf-8')
    print(data_lst)
    return data_lst


def form_lst(data_lst: list[dict]) -> list[list[str]]:
    out_lst = [[i_key for i_key in data_lst[0].keys()]]
    for dct in data_lst:
        out_lst.append([*dct.values()])
    return out_lst


def write_csv(pkl_file: list[list[str]], file_out: Path) -> None:
    with open(file_out, 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f, dialect='excel')
        csv_writer.writerows(pkl_file)


def pickle_to_csv(fail_in: Path, fail_out: Path) -> None:
    write_csv(form_lst(read_pickle(fail_in)), fail_out)