a=input('Введите число: ')
n=len(a)
i=(n//2)-1
answ=None
while i>-1:
    if a[i]==a[-i-1]:
        answ=True
        i-=1
    else:
        answ=False
        break
print(answ)