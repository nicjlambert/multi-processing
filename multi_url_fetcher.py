#!/usr/bin/python3

#Data downloads
#Time series spreadsheets

#https://docs.python.org/3/library/multiprocessing.html
from multiprocessing import Pool
import time
import os


def download(link):
    os.system(f"wget {link} -x") 

links = []

for i in range(1,7):
    links.append(f"https://www.abs.gov.au/statistics/economy/business-indicators/business-indicators-australia/jun-2022/567600{i}.xlsx")

with Pool(7) as p:
    print(p.map(func=download, iterable=links))

