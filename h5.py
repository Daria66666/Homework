print('Вводите числа')
a=[]
while True:
    a1=input()
    if a1!='':
        a.append(int(a1))
    else:
        break
s=0
n=0
for x in a:
    if x>0:
        s+=x
        n+=1
print('Среднее арифметическое: ', s/n)