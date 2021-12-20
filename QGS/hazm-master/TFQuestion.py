# coding: utf-8

from __future__ import unicode_literals
import sys, inspect, doctest, unittest
from docx import Document
from hazm import *
import json
tagger = POSTagger(model='resources/postagger.model')
import random

# this function find and an Int value in the sentence and replace it with a random generated value
import preprocessing

def changing_int_value_TF(text):
    output = tagger.tag(word_tokenize(text))
    for ind, o in enumerate(output):
        payload = u"\"" + text.__add__("؟") +"\""
        try:
            if o[1] =="NUM":
                Matching_value = o[0]
                if int(Matching_value) >= 0 | int(Matching_value) <= 100:
                    Result = int(int(Matching_value) + random.randrange(100))
                    r =str(Result)
                    ques = payload.replace(o[0], r)
                    quest = preprocessing.preprocessing(ques)
                    return ques
                if int(Matching_value) >100:
                    R = int(Matching_value) /16 + random.randrange(10)
                    Result = int(int(Matching_value) - R)
                    r = str(Result)
                    ques = payload.replace(o[0], r)
                    quest = preprocessing.preprocessing(ques)
                    return ques
                break;
        except:
            return False

import APISetup

# this function finds an adverb in the sentence and replace it with a given synoname
def adverb_synoname_TF(text):
    output = tagger.tag(word_tokenize(text))
    for ind, o in enumerate(output):
        if o[1] =="ADV":
            baseUrl = "http://api.text-mining.ir/api/"
            tokenKey = APISetup.tokenkey()
            url =  baseUrl + "TextSimilarity/ExtractSynonyms"
            pay = u"\"" + text.__add__("؟") +"\""
            payload = u"\"" + o[0] +"\""
            if (json.loads(APISetup.callApi(url, payload, tokenKey))):
                Result = json.loads(APISetup.callApi(url, payload, tokenKey))
                payload = pay.replace(o[0], Result[1])
                return payload


# this function finds an adjective in the sentence and replace it with a given synoname
def Adjective_synoname_TF(text):
    output = tagger.tag(word_tokenize(text))
    for ind, o in enumerate(output):
        if o[1] =="AJ":
            baseUrl = "http://api.text-mining.ir/api/"
            tokenKey = APISetup.tokenkey()
            url =  baseUrl + "TextSimilarity/ExtractSynonyms"
            payload = u"\"" + o[0] +"\""
            pay = u"\"" + text.__add__("؟") +"\""
            if (json.loads(APISetup.callApi(url, payload, tokenKey))):
                Result = json.loads(APISetup.callApi(url, payload, tokenKey))
                payload = pay.replace(o[0], Result[1])
                return payload


# this function check if there is any following tags and than consider that sentence as a true false sentence without any variation
def Any_TF(text):
    baseUrl = "http://api.text-mining.ir/api/"
    tokenKey = APISetup.tokenkey()
    url =  baseUrl + "NamedEntityRecognition/Detect"
    payload = u"\"" + text.__add__("؟") +"\""
    Result =  json.loads(APISetup.callApi(url, payload, tokenKey))
    for phrase in Result:
        if phrase['tags']['NER']['item1'] == "B-PER":
            return payload
        if phrase['tags']['NER']['item1'] == "I-PER":
            return payload
        if phrase['tags']['NER']['item1'] == "B-LOC":
            return payload
        if phrase['tags']['NER']['item1'] == "I-LOC":
            return payload
        if phrase['tags']['NER']['item1'] == "B-ORG":
            return payload
        if phrase['tags']['NER']['item1'] == "I-ORG":
            return payload
        if phrase['tags']['NER']['item1'] == "B-DAT":
            return payload
        if phrase['tags']['NER']['item1'] == "I-DAT":
            return payload


# print(changing_int_value_TF("تا نوامبر ۲۰۱۰ این آلبوم در سراسر جهان حدود ۱۱ میلیون نسخه فروش کر"))
