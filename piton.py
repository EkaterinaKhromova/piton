a = int(input('Введите рост '))

if a < 90:
    print('Нужно ешё немножко подрасти и мы обязательно увидимся!')
else:
    if a >= 90 & a <= 109:
        print('Доступен детский маршрут!')
    else:
        if a >= 110 & a <= 124:
            print('Доступно 2 маршрута на высоте 1 м + прыжок + скалодром!')
        else:
            if a >= 125 & a <= 134:
                print('Доступно 2 маршрута на высоте 1 м+ 2 маршрута на высоте 4 м + прыжок + скалодром!')
            else:
                if a >= 135 & a <= 139:
                    print('Доступно 4 маршрута на высоте 4.3 м + троллей + прыжок + скалодром!')
                else:
                    if a > 230:
                        print('Кажется, Вы из сказки о великанах!')

