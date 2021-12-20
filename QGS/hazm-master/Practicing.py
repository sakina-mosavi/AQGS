# coding: utf-8

from __future__ import unicode_literals
import sys, inspect, doctest, unittest
from docx import Document
from hazm import *
import json
tagger = POSTagger(model='resources/postagger.model')


#
# normalizer = Normalizer()
# normalizer.normalize('اصلاح نويسه ها و استفاده از نیم‌فاصله پردازش را آسان مي كند' )
# sent_tokenize('ما هم برای وصل کردن آمدیم! ولی برای پردازش، جدا بهتر نیست؟')
#
# word_tokenize('ولی برای پردازش، جدا بهتر نیست؟')


stemmer = Stemmer()
stemmer.stem('کتاب‌ها')

lemmatizer = Lemmatizer()
lemmatizer.lemmatize('می‌روم')

# delete between prackets
mystring = ""
start = mystring.find( '(' )
end = mystring.find( ')' )
if start != -1 and end != -1:
  result = mystring[start+1:end]




tagger = POSTagger(model='resources/postagger.model')
tagger.tag(word_tokenize('ما بسیار کتاب می‌خوانیم'))


chunker = Chunker(model='resources/chunker.model')
tagged = tagger.tag(word_tokenize('اقای محمدی امروز نتوانست به کابل سفر کند'))
# print(tagged)
print(tree2brackets(chunker.parse(tagged)))
tagg = tagger.tag(word_tokenize('ما بسیار کتاب می‌خوانیم'))
print(tree2brackets(chunker.parse(tagg)))

import APISetup

# parser = DependencyParser(tagger=tagger, lemmatizer=lemmatizer)
# print(parser.parse(word_tokenize('زنگ‌ها برای که به صدا درمی‌آید؟')))
