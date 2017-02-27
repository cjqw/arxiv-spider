#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os

max_img = 50

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def count(cnt):
    """The program will download no more than max_img images"""
    cnt = cnt + 1
    print(cnt)
    if(cnt == max_img):
        os._exit(0)
    return cnt

def getHtml(url):
    """Get the html of url"""
    try:
        headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        html = requests.get(url,  headers=headers)
        return html
    except:
        return nil

def getSoup(url):
    """Get the soup of url"""
    html = getHtml(url)
    soup = BeautifulSoup(html.text,'lxml')
    return soup

def getPdf(url_end):
    "Download the pdf file"
    url = 'https://arxiv.org/'+url_end
    pdf = getHtml(url)
    if pdf:
        f = open(url_end [5:]+'.pdf', 'ab')
        f.write(pdf.content)
        f.close()
        print (url,'scratched')
        return True
    else:
        return False

def st(length,x):
    res = str (x)
    while (len (res) < length):
        res = '0'+res
    return res

os.makedirs('pdf-files',exist_ok=True)
url_head = 'pdf/1702.'
cnt = 0
max_pdf = 10
with cd ('pdf-files'):
    for i in range (0,100000):
        s = st(5,i)
        url = url_head + s
        if (getPdf (url)):
            cnt = cnt + 1;
            if cnt == max_pdf:
                os._exit (0)
os._exit (0)
