minimum=int(input('Введите минимум: '))
maximum=int(input('Введите максимум: '))
inter=int(input('Введите шаг: '))
a=[x for x in range(minimum, maximum, inter)]
print("""
         |     
    x    |    y  
_________|_________
         |         """ )
for x in a:
    y=-1.24*(x**2)+x
    print("   ", x, "   | ", y, "  ")
    print("         |         ")