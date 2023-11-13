# Это программа на Python
# Импортируем модуль datetime
import datetime
import csv

from google.colab import drive
drive.mount('/content/drive')

# Степень
n= 3

end = 20001 # измените это значение на нужное вам число

# Путь к файлу
file_path = '/content/drive/MyDrive/Colab Notebooks/a³+b³=c³-1/CSV/solutions-1.csv'

# Получаем последний a из текстового файла
try:
    with open(file_path, 'r') as f:
        last_a = list(csv.reader(f))[-1][0]
except (IOError, IndexError):
    last_a = None

if last_a is None:
    a_begin = 1
else:
    a_begin = int(last_a) + 1

for a in range(a_begin, end+1):
       an = a ** n
       c = a; cn = an
       # Для каждого значения b в интервале
       for b in range(1, end+1):
           anbn = an + b ** n
           while anbn > cn:
               c += 1
               cn = (c ** n)-1
           if anbn == cn: # Bingo!
               # Получаем текущую дату и время без секунд и миллисекунд
               date_time = datetime.datetime.now().replace(second=0, microsecond=0)
               date_time = date_time.strftime("%Y-%m-%d %H:%M")

               print(f'{a}³+{b}³={c}³-1 | {a**3}+{b**3}={c**3}-1 | {a_begin} {end} | {date_time}')

               # Записываем решение и пределы в текстовый файл
               with open(file_path, 'a', newline='') as f:
                   writer = csv.writer(f)
                   writer.writerow([a, b, c, a**3, b**3, c**3, a_begin, end, date_time])
