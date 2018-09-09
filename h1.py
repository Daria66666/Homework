a=(int(input('Введите число: ')))
a=str(bin(a))
if (len(a)-2)%8==0:
    b1=(len(a)-2)/8
else:
    b1=((len(a)-2)//8)+1
while True:
    try:
        inp=input('''
Перевести в байты - b
Перевести в килобайты - k
''')
        if inp!='b' and inp!='k':
            raise Exception
    except Exception:
        print('Неправильный ввод')
    else:
        if inp=='b':
            print(b1)
        else:
            print(b1/1024)
        break
