# coding: utf-8

from __future__ import unicode_literals
import sys, inspect, doctest, unittest
from hazm import *
from docx.shared import Inches
import re
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
import ImportData as d
import requests
import json
import APISetup

##################### Get Token by Api Key ##########################
tokenKey = APISetup.tokenkey()


WDot = []		# list of sentences without dot
def preprocessing(data):
    d = data
    baseUrl = "http://api.text-mining.ir/api/"
    url =  baseUrl + "PreProcessing/NormalizePersianWord"
    payload = u"{\"text\":\""+ d + "\",\"refineSeparatedAffix\":true}"
    Normalized = APISetup.callApi(url, payload, tokenKey)
    sent_token = sent_tokenize(Normalized)
    for s in sent_token:
        s = re.sub(r'[\.$]','',s)
        WDot.append(s)
    	return WDot

# print(preprocessing("تا نوامبر ۲۰۱۰ این آلبوم در سراسر جهان حدود ۱۱ میلیون نسخه فروش کرد"))

def remove_brackets(data):
    ret = ''
    skip1c = 0
    skip2c = 0
    for i in data:
        if i == '[':
            skip1c += 1
        elif i == '(':
            skip2c += 1
        elif i == ']' and skip1c > 0:
            skip1c -= 1
        elif i == ')'and skip2c > 0:
            skip2c -= 1
        elif skip1c == 0 and skip2c == 0:
            ret += i
    return ret
