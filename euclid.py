a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO

#def;関数を定義する(一連の処理を定義し、関数にまとめるイメージ)
def mygcd(a ,b):
    r = a % b

    while r != 0 :
        a,b = b,r
        r = a % b
    return b    
print('最大公約数は{}'.format(mygcd(int(a),int(b))))






  
      

