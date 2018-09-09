summa=0
pr=1
while True:
    try:
        a = input('Введите натуральное число: ')
        a=int(a)
        if a < 0:
            raise Exception
    except Exception:
        print('Неправильный ввод')
    else:
        a=str(a)
        i=len(a)-1
        while i>-1:
            summa+=(int(a[i]))
            pr*=int(a[i])
            i-=1
        print('Сумма: ',summa)
        print('Произведение: ', pr)
        break