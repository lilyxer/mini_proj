Данный скрипт создавал чтобы найти дубликаты файлов в mp3 коллекции, но будет искать все файлы с одинаковыми названиями!
скрипт ставим в папку где много других подпапок с файлами, еоторые хотим проверить на уникальность.
Разрабатывалась под windows!
Что делает: проходит по всем подпапкам начиная с папки в которой лежит скрипт, все названия файлов сохраняет в множество и сверяется на повтороы, если найдены - отправит повтор в папку где лежит скрипт -> /_tmp. 
Удаление пустой папки не реализовал, боюсь. но предупредит если папка, после переноса файла стала пустой

UPD. файл определяет рабочий каталог, а не где лежит сам файл, чтобы избежать конфлитка и переноса нужных файлов добавил подтверждение.