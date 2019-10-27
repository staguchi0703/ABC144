# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\B\B_input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可
num = int(input())

def exe001(num):
    factor = 2
    factor_list = []
    flag = 'Yes'

    while num > 1 or factor < 10:
        if num % factor == 0:
            factor_list.append(factor)
            num //= factor
        else:
            factor += 1
    # print(factor_list)

    if len(factor_list) > 3:
        for item in factor_list:
            if item >= 5:
                flag = 'No'
                break
            else:
                if len(factor_list) > 6:
                    flag = 'No'
                    break
                elif len(factor_list) > 5:
                    if 3 in factor_list:
                        flag = 'No'
                        break                      

    elif len(factor_list) == 3:
        if factor_list[0] * factor_list[1] < 10 and factor_list[2] < 10:
            pass
        else:
            flag = 'No'

    else:
        for item in factor_list:
            if item >= 10:
                flag = 'No'
                break


    print(flag)
exe001(num)
