a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
number = 61
count = 2
while True:
    number % count 
    count = count + 1   
    if number % count == 0:
        print('{}は素数でない'.format(number))
        break
    elif  count > number ** (1/2):
        print('{}は素数'.format(number))
        break

number = 10
count = 2
while count <= number:
    number % count 
    count = count + 1   
    if number % count == 0:
        print('{}は素数でない'.format(number))
        break
    elif  count > number ** (1/2):
        print('{}は素数'.format(number))
        break

     

