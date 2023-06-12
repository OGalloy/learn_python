#Напишите функцию, которая принимает на вход строку - 
#абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: 
#путь, имя файла, расширение файла.

def split_path( absolute_path: str, delimiter: str):
	*path, file = absolute_path.split(delimiter)
	file_name, extension = file.split(".")
	return delimiter.join(path), file_name, extension

if __name__ == "__main__":
	path, file_name, extension = split_path("~/prog/newfile.py", "/")
	print(f"Path: {path}\nFileName: {file_name}; Extension: {extension}")
