# -*- coding:utf8 -*-
import datetime
import os
import tldextract


def text2list(file):
    with open(file) as f:
        return (line.strip() for line in f.readlines())


def list2text(url_list, file):
    with open(file, 'w', encoding='utf-8') as f:
        for url in url_list:
            print(url, file=f)


def main():
    filter_domain_list = set(text2list('../../text/exclude_domain.txt'))
    result_list = set(text2list('result.txt'))
    lv1_list = list()
    lv2_list = list()

    for url in result_list:
        o = tldextract.extract(url)
        domain = '{}.{}'.format(o.domain, o.suffix)
        if domain in filter_domain_list:
            continue
        if o.subdomain and o.subdomain != 'www':
            lv2_list.append(url)
        else:
            lv1_list.append(url)

    if lv1_list or lv2_list:
        today = datetime.date.today()
        target_dir = os.path.join(os.curdir, str(today))

        if not os.path.exists(target_dir):
            os.mkdir(target_dir)

        lv1_dir, lv2_dir = os.path.join(target_dir, 'domainLv1.txt'), os.path.join(target_dir, 'domainLv2.txt')
        list2text(url_list=lv1_list, file=lv1_dir)
        list2text(url_list=lv2_list, file=lv2_dir)


if __name__ == '__main__':
    main()
