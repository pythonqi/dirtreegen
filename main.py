# -*- coding: utf-8 -*-
# @Time         : 2018/11/26 下午6:59
# @Author       : luoyeqi
# @Email        : luoyeqi@duoshoubang.cn
# @FileName     : main.py
# @Description  :

from bin.dirtreegen import treegen

ignore = ['venv', '.idea']

if __name__ == '__main__':
    treegen(ignore)