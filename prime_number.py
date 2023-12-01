a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
#出力された後にコロンの後に数字を入力できる→入力した数値に対して素数判定できるようにするといい
#数値を入力した際にその値を素数判定させるイメージ
firstnumber = int(a)

for i in range(2,firstnumber) :
    firstnumber % i 
    i = i + 1   
    if firstnumber % i == 0:
        print('{}は素数でない'.format(firstnumber))
        break
    elif  i == (firstnumber - 1):
        print('{}は素数'.format(firstnumber))
        break


secondnumber = int(b)
for i in range(2,secondnumber) :
    secondnumber % i 
    i = i + 1   
    if secondnumber % i == 0:
        print('{}は素数でない'.format(secondnumber))
        break
    elif  i == (secondnumber - 1):
        print('{}は素数'.format(secondnumber))
        break

     

