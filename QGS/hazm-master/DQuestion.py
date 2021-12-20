# coding: utf-8

from __future__ import unicode_literals
import sys, inspect, doctest, unittest
from docx import Document
from hazm import *
import json
tagger = POSTagger(model='resources/postagger.model')

import APISetup
# this function check a person noun in the sentence if there is so, it replace it with چه کسی

def Int_D(text):
    text = text.__add__("؟")
    output = tagger.tag(word_tokenize(text))
    for ind, o in enumerate(output):
        if o[1] =="NUM":
            Matching_value = o[0]
            value = u"\"" + text +"\""
            withDash = value.replace(Matching_value, "چند", 1)
            return withDash

# print( Int_D("افغانستان در ۲۸ اسد استرداد استقلال خود را بدست اورد"))


def Person_Noun(text):
    baseUrl = "http://api.text-mining.ir/api/"
    tokenKey = APISetup.tokenkey()
    url =  baseUrl + "NamedEntityRecognition/Detect"
    payload = u"\"" + text.__add__("؟") +"\""
    Result =  json.loads(APISetup.callApi(url, payload, tokenKey))
    for phrase in Result:
        if phrase['tags']['NER']['item1'] == "B-PER":
            payload = payload.replace(phrase['wordComment'], "چه کسی",1)
            for phrase in Result:
                 if phrase['tags']['NER']['item1'] == "I-PER":
                    payload = payload.replace(phrase['wordComment'], "",1)
                    break
            return payload
        if phrase['tags']['NER']['item1'] == "I-PER":
            payload = payload.replace(phrase['wordComment'], "چه کسی",1)
            for phrase in Result:
                if phrase['tags']['NER']['item1'] == "B-PER":
                    payload = payload.replace(phrase['wordComment'], "",1)
                    break
            return payload



# print(Person_Noun("حضرت ابوبکر صدیق از جمله یاران حضرت محمد بود؟"))

# this function check if there is a location name in the sentence and then replace it with کجا and so on
def Location_Noun(text):
    baseUrl = "http://api.text-mining.ir/api/"
    tokenKey = APISetup.tokenkey()
    url =  baseUrl + "NamedEntityRecognition/Detect"
    payload = u"\"" + text.__add__("؟") +"\""
    Result =  json.loads(APISetup.callApi(url, payload, tokenKey))
    for phrase in Result:
        print(phrase['tags']['NER']['item1'])
        if phrase['tags']['NER']['item1'] == "B-LOC":
            payload = payload.replace(phrase['wordComment'], "کجا",1)
            for phrase in Result:
                if phrase['tags']['NER']['item1'] == "I-LOC":
                    payload = payload.replace(phrase['wordComment'], "",1)
                    break
            return payload
        if phrase['tags']['NER']['item1'] == "I-LOC":
            payload = payload.replace(phrase['wordComment'], "کدام سازمان" , 1)
            for phrase in Result:
                if phrase['tags']['NER']['item1'] == "B-LOC":
                    payload = payload.replace(phrase['wordComment'], "", 1)
                    break
            return payload
        if phrase['tags']['NER']['item1'] == "B-ORG":
            payload = payload.replace(phrase['wordComment'], "کدام سازمان", 1)
            for phrase in Result:
                 if phrase['tags']['NER']['item1'] == "I-ORG":
                    payload = payload.replace(phrase['wordComment'], "", 1)
                    break
            return payload

def Date_Noun(text):
    baseUrl = "http://api.text-mining.ir/api/"
    tokenKey = APISetup.tokenkey()
    url =  baseUrl + "NamedEntityRecognition/Detect"
    payload = u"\"" + text.__add__("؟") +"\""
    Result =  json.loads(APISetup.callApi(url, payload, tokenKey))
    for phrase in Result:
        if phrase['tags']['NER']['item1'] == "B-DAT":
            payload = payload.replace(phrase['wordComment'], "چه زمانی", 1)
            for phrase in Result:
                if phrase['tags']['NER']['item1'] == "I-DAT":
                    payload = payload.replace(phrase['wordComment'], "", 1)
                    break
            return payload
        if phrase['tags']['NER']['item1'] == "I-DAT":
            payload = payload.replace(phrase['wordComment'], "چه زمانی", 1)
            for phrase in Result:
                if phrase['tags']['NER']['item1'] == "B-DAT":
                    payload = payload.replace(phrase['wordComment'], "", 1)
                    break
            return payload


def Date_D(text):
    baseUrl = "http://api.text-mining.ir/api/"
    tokenKey = APISetup.tokenkey()
    url =  baseUrl + "NamedEntityRecognition/Detect"
    payload = u"\"" + text.__add__("؟") +"\""
    Result =  json.loads(APISetup.callApi(url, payload, tokenKey))
    for phrase in Result:
        if phrase['tags']['NER']['item1'] == "B-DAT":
            firstP =  phrase['wordComment']
            for phrase in Result:
                if phrase['tags']['NER']['item1'] == "I-DAT":
                    secondP = phrase['wordComment']
                    complete = firstP + secondP
                    payload = "در" +  complete + " چه اتفاقی افتاد؟"
                    return payload
        if phrase['tags']['NER']['item1'] == "I-DAT":
            firstP =  phrase['wordComment']
            for phrase in Result:
                if phrase['tags']['NER']['item1'] == "B-DAT":
                    secondP = phrase['wordComment']
                    complete = firstP + " " + secondP
                    payload = "در" +  complete + "چه اتفاقی افتاد؟"
                    return payload

def Event(text):
    baseUrl = "http://api.text-mining.ir/api/"
    tokenKey = APISetup.tokenkey()
    url =  baseUrl + "NamedEntityRecognition/Detect"
    payload = u"\"" + text.__add__("؟") +"\""
    Result =  json.loads(APISetup.callApi(url, payload, tokenKey))
    for phrase in Result:
        if phrase['tags']['NER']['item1'] == "B-EVE":
            payload = payload.replace(phrase['wordComment'], "کدام رویداد", 1)
            for phrase in Result:
                if phrase['tags']['NER']['item1'] == "I-EVE":
                    payload = payload.replace(phrase['wordComment'], "", 1)
                    break
            return payload
        if phrase['tags']['NER']['item1'] == "I-EVE":
            payload = payload.replace(phrase['wordComment'], "کدام رویداد", 1)
            for phrase in Result:
                if phrase['tags']['NER']['item1'] == "B-EVE":
                    payload = payload.replace(phrase['wordComment'], "", 1)
                    break
            return payload


def Per_D(text):
    baseUrl = "http://api.text-mining.ir/api/"
    tokenKey = APISetup.tokenkey()
    url =  baseUrl + "NamedEntityRecognition/Detect"
    payload = u"\"" + text.__add__("؟") +"\""
    Result =  json.loads(APISetup.callApi(url, payload, tokenKey))
    for phrase in Result:
        if phrase['tags']['NER']['item1'] == "B-PER":
            firstP = phrase['wordComment']
            for phrase in Result:
                if phrase['tags']['NER']['item1'] == "I-PER":
                    secondP = phrase['wordComment']
                    complete = firstP + " " + secondP
                    payload = "در مورد " +  complete + " مختصرا معلومات دهید؟"
                    return payload





# print(Per_D("خانم محمدی در پوهنتون کابل استاد است"))
# print(Person_Noun("حضرت محمد(ص) پیامبر ما است"))
# # # # #
# baseUrl = "http://api.text-mining.ir/api/"
# url =  baseUrl + "NamedEntityRecognition/Detect"
# payload = u'" حضرت محمد(ص) پیامبر ما است"'
# tokenKey = APISetup.tokenkey()
# result = json.loads(APISetup.callApi(url, payload, tokenKey))
# for phrase in result:
#     print("("+phrase['word']+","+phrase['tags']['NER']['item1']+") ")


