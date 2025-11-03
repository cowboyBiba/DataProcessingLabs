def read_txt_file(file_name):
    try:
        file = open(file_name, "r")
        content = file.readlines()
        for l in range(len(content)-1):
            content[l] = content[l][:-1]
        return content
    except Exception as e:
        print(e)
        return None

def write_txt_file(file_name, str_data):
    if type(str_data) == list:
        str_data = "".join(str_data)
    else:
        str_data = str(str_data)
    try:
        file = open(file_name, "w")
        file.write(str_data)
    except Exception as e:
        print(e)

def replace_pattern(str_data, substring, replacement, times=0, direction="left"):
    # ожидаем, что придёт список в str_data
    for l in range(len(str_data)):
        line = str_data[l]
        if times > 0:
            cnt = line.count(substring)
            str_data[l] = str_data[l].replace(substring, replacement, times)
            times -= cnt
            if times <= 0:
                break
        else:
            str_data[l] = str_data[l].replace(substring, replacement)
    return str_data

def split_str(str_data, line, separator, new_separator=None):
    l = str_data[line].split(sep=separator)
    return_l = []
    for el in range(len(l)):
        if l[el] != "":
            return_l.append(l[el])
    if new_separator:
        str_data[line] = new_separator.join(return_l)
        return str_data
    else:
        return return_l
def contains_digits(str_data, line):
    l = str_data[line]
    flag = False
    for i in range(len(l)):
        if l[i].isdigit():
            print("Элемент {0} - число. Номер элемента - {1}.".format(l[i], i))
            flag = True
    if not flag:
        print("Строка не содержит цифр.")

def contains_letters(str_data, line):
    l = str_data[line]
    flag = False
    for i in range(len(l)):
        if l[i].isalpha():
            print("Элемент {0} - буква. Номер элемента - {1}.".format(l[i], i))
            flag = True
    if not flag:
        print("Строка не содержит букв.")

def lines_to_dict_by_first_word(str_data, separator):
    lines_dict = {}
    for i in range(len(str_data)):
        line_list = split_str(str_data, i, separator)
        first_word = line_list[0]
        if first_word not in lines_dict.keys():
            lines_dict[first_word] = [line_list]
        else:
            lines_dict[first_word].append(line_list)
    print(lines_dict)
    return lines_dict
def sort_by_row_length(str_data, direction="asc", apply=False):
    # сортировка пузырьком
    if direction == "asc":
        for j in range(len(str_data)):
            flag = False
            for i in range(0, len(str_data) - 1 - j):
                if len(str_data[i]) > len(str_data[i+1]):
                    flag = True
                    str_data[i], str_data[i+1] = str_data[i+1], str_data[i]
            if not flag:
                break
    else:
        for j in range(len(str_data)):
            flag = False
            for i in range(0, len(str_data) - 1 - j):
                if len(str_data[i]) < len(str_data[i+1]):
                    flag = True
                    str_data[i], str_data[i+1] = str_data[i+1], str_data[i]
            if not flag:
                break
    print("Отсортированное по длине строки содержимое файла:")
    for i in str_data:
        print(i)
def lines_to_dict_by_first_letter(str_data):
    lines_dict = {}
    for line in str_data:
        first_letter = line[0]
        if first_letter not in lines_dict.keys():
            lines_dict[first_letter] = [line]
        else:
            lines_dict[first_letter].append(line)
    print(lines_dict)
    return lines_dict

def main():
    str_data = None
    lines_dict = None
    while True:
        print("---Главное меню.---")
        print("1. Прочитать файл.")
        print("2. Записать в файл.")
        print("3. Вывести текущий вариант текстовых данных.")
        print("4. Заменить подстроку(ки) по шаблону.")
        print("5. Разбить строку на слова.")
        print("6. Проверка на буквы.")
        print("7. Проверка на цифры.")
        print("8. Составить словарь из строк. Ключ - 1-ое слово.")
        print("9. Отсортировать строки по длине.")
        print("10. Составить словарь из строк. Ключ - 1-ая буква.")
        print("11. Поиск по словарю.")
        print("12. Выход.")

        print("------")
        print()
        main_choice = input("Выберите пункт: ")
        if main_choice == "1":
             file_name = input("Введите имя файла. Оставьте пустым, чтобы вернуться в меню: ")
             if file_name != "":
                 str_data = read_txt_file(file_name)
        elif main_choice == "2":
            if str_data:
                file_name = input("Введите имя файла. Оставьте пустым, чтобы вернуться в меню: ")
                if file_name != "":
                    write_txt_file(file_name, str_data)
            else:
                print("Строковых данных нет!")
        elif main_choice == "3":
            if str_data:
                print("---Строковые данные:---")
                for line in str_data:
                    print(line)
                print("---Конец данных---")
            else:
                print("---Строковых данных нет---")
            if lines_dict:
                print("---Словарь строк---")
                print(lines_dict)
            else:
                print("---Словарь не создан")
        elif main_choice == "4":
            substring = input("Введите подстроку для замены. Оставьте пустым, чтобы вернуться в меню: ")
            if substring != "":
                while True:
                    replacement = input("Введите замену для подстроки: ")
                    times = input("Введите количество подстрок, которые будут заменены. Оставьте пустым для замены всех подстрок: ")
                    if times == "":
                        str_data = replace_pattern(str_data, substring, replacement)
                        break
                    elif times.isdigit():
                        if int(times) > 0:
                            try:
                                str_data = replace_pattern(str_data, substring, replacement, int(times))
                            except TypeError:
                                print("В памяти нет строковых данных. Прочитайте файл!")
                            break
                        else:
                            print("Введите целое число >= 0")
                    else:
                        print("Введите целое число >= 0")
        elif main_choice == "5":
            while True:
                err_flag = False
                try:
                    line_num = int(input("Введите номер строки (нумерация с 0): "))
                    if line_num < 0:
                        print("Введите корректное число - целое, неотрицательное!")
                        err_flag = True
                    if line_num > len(str_data)-1:
                        print("Ошибка! В исходном тексте строк - {0}, введеный номер строки - {1}.")
                        err_flag = True
                except TypeError:
                    print("Введите корректное число - целое, неотрицательное!")
                    err_flag = True
                if not err_flag:
                    break
            separator = input("Введите разделитель для разбивки строки: ")
            try:
                print(split_str(str_data, line_num, separator))
            except TypeError:
                print("В памяти нет строковых данных. Прочитайте файл!")
        elif main_choice == "6":
            if str_data:
                while True:
                    err_flag = False
                    try:
                        line_num = int(input("Введите номер строки (нумерация с 0): "))
                        if line_num < 0:
                            print("Введите корректное число - целое, неотрицательное!")
                            err_flag = True
                        if line_num > len(str_data)-1:
                            print("Ошибка! В исходном тексте строк - {0}, введеный номер строки - {1}.")
                            err_flag = True
                    except TypeError:
                        print("Введите корректное число - целое, неотрицательное!")
                        err_flag = True
                    if not err_flag:
                        break
                try:
                    contains_letters(str_data, line_num)
                except TypeError:
                    print("В памяти нет строковых данных. Прочитайте файл!")
            else:
                print("В памяти нет строковых данных. Прочитайте файл!")
        elif main_choice == "7":
            if str_data:
                while True:
                    err_flag = False
                    try:
                        line_num = int(input("Введите номер строки (нумерация с 0): "))
                        if line_num < 0:
                            print("Введите корректное число - целое, неотрицательное!")
                            err_flag = True
                        if line_num > len(str_data)-1:
                            print("Ошибка! В исходном тексте строк - {0}, введеный номер строки - {1}.")
                    except TypeError:
                        print("Введите корректное число - целое, неотрицательное!")
                        err_flag = True
                    if not err_flag:
                        break
                try:
                    contains_digits(str_data, line_num)
                except TypeError:
                    print("В памяти нет строковых данных. Прочитайте файл!")
            else:
                print("В памяти нет строковых данных. Прочитайте файл!")
        elif main_choice == "8":
            separator = input("Введите разделитель для разбивки слов: ")
            try:
                lines_dict = lines_to_dict_by_first_word(str_data, separator)
            except TypeError:
                print("В памяти нет строковых данных. Прочитайте файл!")
        elif main_choice == "9":
            while True:
                direction = input("Выберите направление сортировки (1 - возрастающий, 2 - убывающий):")
                if direction in ["1", "2"]:
                    break
                print("Ошибка! Доступные варианты: 1 и 2.")
            dir_list = {"1": "asc", "2": "des"}
            try:
                sort_by_row_length(str_data, dir_list[direction])
            except TypeError:
                print("В памяти нет строковых данных. Прочитайте файл!")
        elif main_choice == "10":
            try:
                lines_dict = lines_to_dict_by_first_letter(str_data)
            except TypeError:
                print("В памяти нет строковых данных. Прочитайте файл!")
        elif main_choice == "11":
            key = input("Введите ключ для поиска по словарю:")
            try:
                print(lines_dict[key])
            except KeyError:
                print("Такого ключа нет в словаре.")
            except TypeError:
                print("Словарь ещё не создан")
        elif main_choice == "12":
            break
        else:
            print("Такого пункта нет. Введите число от 1 до 12.")

main()