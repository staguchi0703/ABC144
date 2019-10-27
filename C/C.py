# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\C\C_input.txt', 'r', encoding="utf-8")
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
import math 
import itertools

num = int(input())

def mk_factor(num):
    factor = 2
    factor_list = []

    while num > 1 and factor < int(math.sqrt(num))+1:
        if num % factor == 0:
            factor_list.append(factor)
            num //= factor
        else:
            factor += 1

    factor_list.append(num)

    return factor_list

def nearest_path(factor_list):
    a = list(itertools.combinations(factor_list, len(factor_list)//2))

    res_list = []

    for item in a:
        temp_list = mk_factor(num)
        factor1 = 1
        factor2 = 1
        for k in item:
            temp_list.remove(k)
            factor2 *= k

        for j in temp_list:
            factor1 *= j
        res_list.append(factor1+factor2)

    return min(res_list) -2

factor_list = mk_factor(num)
print(nearest_path(factor_list))