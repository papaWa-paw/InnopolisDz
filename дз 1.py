a = int(input())
if a % 10 == 1:
    print(a, 'рубль')
elif a % 10 == 2 or a % 10 == 3 or a % 10 == 4:
    print(a, 'рубля')
else:
    print(a, 'рублей')
