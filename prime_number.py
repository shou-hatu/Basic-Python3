a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
#出力された後にコロンの後に数字を入力できる→入力した数値に対して素数判定できるようにするといい
#数値を入力した際にその値を素数判定させるイメージ


def  primalitytest(number):
    if  number == 1:
        return('{}は素数でない'.format(number))
    if  number == 2:
        return('{}は素数'.format(number))    
    for i in range(2,(number + 1)) :
        number % i   
        if number % i == 0:
                return('{}は素数でない'.format(number))
                
        elif  i == (number - 1):
                return('{}は素数'.format(number))
print(primalitytest(int(a)))
print(primalitytest(int(b)))
                

     


