# coding: utf-8

from __future__ import unicode_literals
from hazm import *
import json
tagger = POSTagger(model='resources/postagger.model')
import APISetup

# this function check an INT value in a senetence and then replace it with dashes

def Int_BS(text):
    text = text.__add__("؟")
    output = tagger.tag(word_tokenize(text))
    for ind, o in enumerate(output):
        if o[1] =="NUM":
            Matching_value = o[0]
            value = u"\"" + text +"\""
            withDash = value.replace(Matching_value, "ـــــــــــــ", 1)
            return withDash


# this function checks a person name and then replace it with dashes and so on
def Per_BS(text):
    baseUrl = "http://api.text-mining.ir/api/"
    tokenKey = APISetup.tokenkey()
    url =  baseUrl + "NamedEntityRecognition/Detect"
    payload = u"\"" + text.__add__("؟") +"\""
    Result =  json.loads(APISetup.callApi(url, payload, tokenKey))
    for phrase in Result:
        if phrase['tags']['NER']['item1'] == "B-PER":
            payload = payload.replace(phrase['wordComment'],"", 1)
            for phrase in Result:
                if phrase['tags']['NER']['item1'] == "I-PER":
                    payload = payload.replace(phrase['wordComment'],"", 1)
                    break
            return payload
        if phrase['tags']['NER']['item1'] == "I-PER":
            payload = payload.replace(phrase['wordComment'],"", 1)
            for phrase in Result:
                if phrase['tags']['NER']['item1'] == "B-PER":
                    payload = payload.replace(phrase['wordComment'],"", 1)
                    break
            return payload


def Dat_BS(text):
    baseUrl = "http://api.text-mining.ir/api/"
    tokenKey = APISetup.tokenkey()
    url =  baseUrl + "NamedEntityRecognition/Detect"
    payload = u"\"" + text.__add__("؟") +"\""
    Result =  json.loads(APISetup.callApi(url, payload, tokenKey))
    for phrase in Result:
        if phrase['tags']['NER']['item1'] == "B-DAT":
            payload = payload.replace(phrase['wordComment'], "ـــــــــــ", 1)
            for phrase in Result:
                if phrase['tags']['NER']['item1'] == "I-DAT":
                    payload = payload.replace(phrase['wordComment'],"", 1)
                    break
            return payload
        if phrase['tags']['NER']['item1'] == "I-DAT":
            payload = payload.replace(phrase['wordComment'], "ـــــــــ", 1)
            for phrase in Result:
                if phrase['tags']['NER']['item1'] == "B-DAT":
                    payload = payload.replace(phrase['wordComment'],"", 1)
                    break
            return payload

def Loc_BS(text):
    baseUrl = "http://api.text-mining.ir/api/"
    tokenKey = APISetup.tokenkey()
    url =  baseUrl + "NamedEntityRecognition/Detect"
    payload = u"\"" + text.__add__("؟") +"\""
    Result =  json.loads(APISetup.callApi(url, payload, tokenKey))
    for phrase in Result:
        if phrase['tags']['NER']['item1'] == "B-LOC":
            payload = payload.replace(phrase['wordComment'], "ــــــــــ", 1)
            for phrase in Result:
                if phrase['tags']['NER']['item1'] == "I-LOC":
                    payload = payload.replace(phrase['wordComment'],"", 1)
                    break
            return payload
        if phrase['tags']['NER']['item1'] == "I-LOC":
            payload = payload.replace(phrase['wordComment'], "ـــــــــ", 1)
            for phrase in Result:
                if phrase['tags']['NER']['item1'] == "B-LOC":
                    payload = payload.replace(phrase['wordComment'],"", 1)
                    break
            return payload



def Eve_BS(text):
    baseUrl = "http://api.text-mining.ir/api/"
    tokenKey = APISetup.tokenkey()
    url =  baseUrl + "NamedEntityRecognition/Detect"
    payload = u"\"" + text.__add__("؟") +"\""
    Result =  json.loads(APISetup.callApi(url, payload, tokenKey))
    for phrase in Result:
        if phrase['tags']['NER']['item1'] == "B-EVE":
            payload = payload.replace(phrase['wordComment'], "ـــــــــ", 1)
            for phrase in Result:
                if phrase['tags']['NER']['item1'] == "I-EVE":
                    payload = payload.replace(phrase['wordComment'],"", 1)
                    break
            return payload
        if phrase['tags']['NER']['item1'] == "I-EVE":
            payload = payload.replace(phrase['wordComment'], "ــــــــــ", 1)
            for phrase in Result:
                if phrase['tags']['NER']['item1'] == "B-EVE":
                    payload = payload.replace(phrase['wordComment'],"", 1)
                    break
            return payload



# print(Eve_BS("احمدعباسی در ایران، انگلستان و آمریکا سفر کرده است؟"))
# baseUrl = "http://api.text-mining.ir/api/"
# url =  baseUrl + "NamedEntityRecognition/Detect"
# payload = u'"در ۲۸  اسد روز استقلال وطن عزیز ما افغانستان است که در غازی امان الله خان به دست آمد. "'
# tokenKey = APISetup.tokenkey()
# result = json.loads(APISetup.callApi(url, payload, tokenKey))
# for phrase in result:
#     print("("+phrase['word']+","+phrase['tags']['NER']['item1']+") ")
