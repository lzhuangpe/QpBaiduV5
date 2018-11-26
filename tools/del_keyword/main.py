# -*- coding: utf-8 -*-
import re

def text2list(file):
    with open(file, encoding='utf-8') as f:
        return (line.strip() for line in f.readlines())


def list2text(arr, file):
    with open(file, 'w', encoding='utf-8') as f:
        for i in arr:
            print(i, file=f)


def del_keyword(keyword, keyword_list, file='result.txt'):
    result = []
    for line in keyword_list:
        if re.search(keyword, line):
            print('del keyword: {}'.format(line))
        else:
            result.append(line)

    list2text(result, 'result.txt')


def main():
    keyword_list = text2list('keyword.txt')
    del_keyword('三国杀', keyword_list)


if __name__ == '__main__':
    main()