#!/usr/bin/env python


word_dict = { 'key1' : 'hello', 'key2' : 'to', 'key3': 'the', 'key4': 'world' }


def unscramble(scrambled, word_dict):
    t = tuple(scrambled)
    key = ""
    for i in t:
        key = i
        for j in t:
            if t.index(i) is not t.index(j):
                    key = key + j
                    print(key)

scrambled = 'elhloothtedrowl'
unscramble(scrambled, word_dict)