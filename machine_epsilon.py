# TODO
#εを1/2し続ける
count = 1

while True:
    1 + (1 / 2) **count
    count = count + 1
    if 1 + (1 / 2) **count <= 1:
        break
epsilon = (1 / 2) **count
print(epsilon)
