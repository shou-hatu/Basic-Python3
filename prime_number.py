a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
number = 61

for x in range(2,number):#number-1の数まで繰り返す
    number % x  
    if number % x == 0:
        print('{}は素数でない'.format(number))
        break#繰り返しをやめる
    elif  x > number ** (1/2):
        print('{}は素数'.format(number))
        break
       

number = 10
for x in range(2,number):#number-1の数まで繰り返す
    number % x  
    if number % x == 0:
        print('{}は素数でない'.format(number))
        break#繰り返しをやめる
    elif  x > number ** (1/2):
        print('{}は素数'.format(number))
        break

     

