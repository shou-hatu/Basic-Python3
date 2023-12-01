# TODO
#εを1/2し続ける
EPS = 1
#今回は左辺が1を超えない時のepsilonの値が欲しい→計算作業の後の値を出力するとギリギリ1を超えた時のεの値が出力されてしまう！
while 1 + EPS > 1:
    #ループ処理前の値を拾えるようにepsilonに置き換えた
    epsilon = EPS
    EPS = EPS / 2
    
print(epsilon)

