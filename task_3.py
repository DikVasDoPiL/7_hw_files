def new_file(old_files):
    # прочитаем содержиое файлов в общий словарь
    def read_files(file_names):
        files = {}
        for name in file_names:
            files[name] = [i
                           for i in open(name, 'r', encoding='utf8').readlines()]
        return files

    # Инвертируем ключи и значения, для сортировки по ключам.
    def reverse_dict(files):
        reverse = {}
        for i in files.keys():
            x = len(files[i])
            if x not in reverse.keys():  # если несколько файлов с одним кол-вом строк, учтем это
                reverse[x] = [i]
            else:
                reverse[x] += [i]
        return reverse

    # Генерируем файл для последующей записи
    def create_new(reverse_dict, old_files):
        keys = [i for i in reverse_dict.keys()]
        keys.sort()
        result = []
        count = 0
        for i in keys:
            if count > 0:
                result += ['\n']
            count += 1
            for j in reverse_dict[i]:
                result += [(j + '\n')]
                result += [str(i) + '\n']
                for string in old_files[j]:
                    result += [string]
        return result

    # выполнение основной функции
    files = read_files(old_files)
    return create_new(reverse_dict(files), files)


# Исходные данные
names = ['1.txt', '2.txt', '3.txt']
target = 'result.txt'

# Записываем результат в целевой файл
with open(target, 'w', encoding='utf8') as new:
    for i in new_file(names):
        new.write(i)
