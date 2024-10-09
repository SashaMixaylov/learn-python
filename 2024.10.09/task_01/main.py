# Напишите функцию, которая получает на вход строку,
# сепаратор и возвращает список строк, которые получены из исходной делением по сепаратору.

def text(r: str, separator: str) -> list:
    return r.split(separator)

if __name__ == '__main__':
    s1 = str(input("Введите r"))
    s2 = str(input("Введите separator"))
    print(text(s1, s2))