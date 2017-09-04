#!/usr/bin/env python

import os


def remove(str1, str2):
    new_list = []
    list1 = str1.split(' ')
    list2 = str2.split(' ')
    mc = 0
    for j in list2:
        for i in list1:
            if (j == i) and (mc < 1):
                mc += 1
            else:
                new_list.append(i)
        list1 = new_list[:]
        mc = 0
        del new_list[:]

    print("The desired list is {} ".format(list1))


if __name__ == '__main__':
    remove('A Statement is a Statement', 'Statement a')
