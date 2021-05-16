# 加载使用库
import pandas
import os
import numpy
import jieba.posseg as pseg
from multiprocessing import Pool, Process
import re
from tqdm import tqdm
import json
import threading


def threadWork2(key):
    print(key, 'start')
    set_temp = set(clazz[key])
    freCount = {'negative': [], 'neutral': [], 'positive': []}
    for index, item in enumerate(set_temp):
        if index % 1000 == 0:
            print(key, str(index / len(set_temp)))
        freCount[key].append([item, clazz[key].count(item)])
    with open(r'E:\Download\数据大赛\选题1\第二部分分词\0-%s.json' % key, 'w', encoding='gb18030') as f:
        json.dump(freCount, f)
    print(key, 'DONE')


with open(r'E:\Download\数据大赛\选题1\第二部分分词\0.txt', encoding='gb18030') as f:
    data = f.read()
data = data.split('\n')
data = [item.split('\t') for item in data[:-1]]
clazz = {'negative': [], 'neutral': [], 'positive': []}
for item in tqdm(data):
    try:
        clazz[item[1]].append(item[0])
    except:
        continue

if __name__ == '__main__':
    thread1 = Process(target=threadWork2, args=('negative',))
    thread2 = Process(target=threadWork2, args=('neutral',))
    thread3 = Process(target=threadWork2, args=('positive',))
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()
