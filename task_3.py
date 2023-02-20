import datetime

n = int(input('Сколько раз вы хотите ввести данные: '))
time_list = []
for i in range(n):
    while True:
        time_user = input(f'ответ  {i + 1} должен быть в Формате |час:минута:cекунда| - ')
        try:
            valid_time = datetime.datetime.strptime(time_user, '%H:%M:%S')
            if valid_time in time_list:
                print(f'время {valid_time} уже имеется . введите другое время !!!')
                continue
            time_list.append(valid_time)
            break
        except ValueError:
            print(f'формат времени {time_user} неправильный !!. вводите в формате - |час:минута:cекунда| ')
hlist = []
mlist = []
slist = []

for valid_time in time_list:
    hlist.append(valid_time.hour)
    mlist.append(valid_time.minute)
    slist.append(valid_time.second)


print("список часов: ", hlist)
print("список минут : ", mlist)
print("список секунд: ", slist)
print("отсортировано")