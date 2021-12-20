from __future__ import unicode_literals
import sys, inspect, doctest, unittest
from docx import Document
from hazm import *
import json
tagger = POSTagger(model='resources/postagger.model')
import APISetup
import re
WDot = []
def preprocessing(data):
    d = data
    baseUrl = "http://api.text-mining.ir/api/"
    tokenKey = APISetup.tokenkey()
    url =  baseUrl + "PreProcessing/NormalizePersianWord"
    payload = u"{\"text\":\""+ d + "\",\"refineSeparatedAffix\":true}"
    Normalized = APISetup.callApi(url, payload, tokenKey)
    sent_token = sent_tokenize(Normalized)
    for s in sent_token:
        s = re.sub(r'[\.$]','',s)
        return s

print(preprocessing("1999"))
