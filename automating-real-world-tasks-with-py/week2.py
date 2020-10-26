#! /usr/bin/env python3
import os
import requests

path='/data/feedback/'
keys=['title','name','date','feedback']
f = os.listdir(path)

for i in f:
    count=0
    fb={}
    j = open(path+i):
    for l in j:
        val = l.strip()
        fb[keys[count]]=val
        count+=1
    j.close()
    print(fb)
    response=requests.post('http://34.123.206.184/feedback/',json=fb)

