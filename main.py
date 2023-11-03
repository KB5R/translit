print('Вводите ФИO которое надо перевести ')
print('Пример ввода: Колесников Илья Александрович')
print('Вывод: Kolesnikov.I.A')
print('Если хотите создать почты введите Y')
print('Если хотите сократить имя X')
mail = input()



def transliterate(name):

    slovar = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
              'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
              'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
              'ц': 'c', 'ч': 'cz', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e',
              'ю': 'yu', 'я': 'ya', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
              'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
              'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
              'Ц': 'C', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch', 'Ъ': '', 'Ы': 'y', 'Ь': '', 'Э': 'E',
              'Ю': 'Yu', 'Я': 'Ya', ',': '', '?': '', ' ': '_', '~': '', '!': '', '@': '', '#': '',
              '$': '', '%': '', '^': '', '&': '', '*': '', '(': '', ')': '', '-': '', '=': '', '+': '',
              ':': '', ';': '', '<': '', '>': '', '\'': '', '"': '', '\\': '', '/': '', '№': '',
              '[': '', ']': '', '{': '', '}': '', 'ґ': '', 'ї': '', 'є': '', 'Ґ': 'g', 'Ї': 'i',
              'Є': 'e', '—': ''}

    # Циклически заменяем все буквы в строке
    for key in slovar:
        name = name.replace(key, slovar[key])
    return name
if mail == 'X':

    words = ''
    while words != 'STOP':
        words = input().split()
        name1 = words[0]
        name2 = words[1]
        name3 = words[2]
        x = name1.lower() + '.' + name2[:1].lower() + '.' + name3[:1].lower()
        x = transliterate(x)

        with open("output.txt", "a") as file:
            file.write(x + "\n")
elif mail == 'Y':
    print('Введите доменное имя')
    print('Пример доменного имени: @yandex.ru')
    mmmail = input()
    words = ''
    while words != 'STOP':
        words = input().split()
        name1 = words[0]
        name2 = words[1]
        name3 = words[2]

        x = (name1.lower() + '.' + name2[:1].lower() + '.' + name3[:1].lower())
        x = transliterate(x)
        q = x + mmmail
        with open("output.txt", "a") as file:
            file.write(q + "\n")
