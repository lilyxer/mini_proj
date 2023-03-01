"""Позволяет находить дубликаты файлов в подкаталогах
Переносит дубликаты в коренвую папку _tmp
Если папка пуста - предупредит"""

import os
import shutil

directory = os.getcwd()
set_file = set()


def walkee():
    for folderName, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            if filename.casefold() in set_file:
                print(f'{filename} в подпапке {folderName}')
                old = os.path.join(folderName, *subfolders)
                shutil.move(f'{old}\\{filename}', f'{directory}\\_tmp\\{filename}')
                print(f'{filename} был перенесен в корень -> "_tmp"')
                if not os.listdir(old):
                    print(f'{old} - Папка пустая\nУдалить?')
                    answer = input('Y/N ... ')
                    if answer.casefold() == 'y':
                        print('что то я очкую, почитай еще раз про shutil.rmtree')
            set_file.add(filename.lower())
    print(f'файлов в директории: {len(set_file)}')

print(f'Ваша директория на данный момент {directory}\nТребуется Ваше подтверждение')
answer = input('Y - если директория верна ')

if answer.casefold() == 'y':
    walkee()


# сделаешь?
# если есть повтор - перенести файл в ./повторы
# если foldername - пуст, удалить