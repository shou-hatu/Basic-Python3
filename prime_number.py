a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
#出力された後にコロンの後に数字を入力できる→入力した数値に対して素数判定できるようにするといい
#数値を入力した際にその値を素数判定させるイメージ

def  primalitytest(number):
    #数字の文字列を整数に変換するのがint,小数点にするのがfloat
    #str.isdecima()；文字列中の全ての文字が十進数字で、
    # かつ 1 文字以上あるなら True を、そうでなければ False を返します
    if str.isdecimal(number):
        if  int(number) == 1:
            return('{}は素数でない'.format(int(number)))
        if  int(number) == 2:
            return('{}は素数'.format(int(number)))    
        for i in range(2,(int(number) + 1)) :
            int(number) % i   
            if int(number) % i == 0:
                    return('{}は素数でない'.format(int(number)))
            elif i > (int(number)) ** (1 / 2) :
                    return('{}は素数'.format(int(number)))
    else:
         return "数値を入力してください"
print(primalitytest(a))
print(primalitytest(b))
                

     


