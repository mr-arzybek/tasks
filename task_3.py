import datetime

user_n = int(input('Сколько раз вы хотите ввести данные: '))
time_list = []
for i in range(user_n):
    while True:
        time_user = input(f'ответ  {i + 1} должен быть в Формате |час:минута:cекунда| - ')
        try:
            valid_time = datetime.datetime.strptime(time_user, '%H:%M:%S')
            if valid_time in time_list:
                print(f'время {valid_time} уже имеется . введите другое время !!!')
                continue
            time_list.append(str(valid_time.time()))
            break
        except ValueError:
            print(f'формат времени {time_user} неправильный !!. вводите в формате - |час:минута:cекунда| ')
    
print(sorted(time_list, reverse=True))