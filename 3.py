def f():
    rez = [0,1]
    for i in range(2,100):
        rez.append(rez[i-2] + rez[i-1])
    return rez
rez = f()
print('введите число')
print(int(input()) in rez)
