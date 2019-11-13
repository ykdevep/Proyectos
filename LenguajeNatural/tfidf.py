import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import math

text1 = """
Puede trabajar de forma independiente o en una empresa especializada en este campo.
Puede consultar cada clase y contestar su cuestionario las veces que lo necesites.
La idea es identificar los temas que ya dominas e indicarte los que necesitas reforzar.
"""

def remove_string_special_characters(s):
    stripped = re.sub('[\w\s]', '', s)
    stripped = re.sub('_', '', stripped)
    stripped = re.sub('\s+', '', stripped)
    stripped = stripped.strip()

    return stripped

def get_doc(sent):
    doc_info = []
    i = 0
    for sent in sent:
        i += 1
        count = count_words(sent)
        temp = {'doc_id' : i, 'doc_length' : count}
        doc_info.append(temp)
    return doc_info

def count_words(sent):
    count = 0
    words = word_tokenize(sent)
    for word in words:
        count += 1
    return count

def create_freq_dict(sent):
    i = 0
    freqDict_list = []
    for sent in sent:
        i += 1
        freq_dict = {}
        words = word_tokenize(sent)
        for word in words:
            word = word.lower()
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] += 1
            temp = {'doc_id' : i, 'freq_dict' : freq_dict}
        freqDict_list.append(temp)
    return freqDict_list

def computeTF(doc_info, freqDict_list):
    IDF_scores = []
    counter = 0
    for dict in freqDict_list:
        counter += 1
        for k in dict['freq_dict'].keys():
            count = sum([k in tempDict['freq_dict'] for tempDict in freqDict_list])
            temp = {'doc_id' : counter, 'IDF_score' : math.log(len(doc_info)/count), 'key' : k}
            IDF_scores.append(temp)
    return IDF_scores

def computeTDIDF(TF_scores, IDF_scores):
    TDIDF_scores = []
    for j in IDF_scores:
        for i in TF_scores:
            if j['key'] == i['key'] and j['doc_id'] == i['doc_id']:
                temp = {'doc_id' : j['doc_id'],
                        'TDFIDF_score' : j['IDF_score'] * i['TF_score'],
                        'key' : i['key']}
        TDIDF_scores.append(temp)
    return TDIDF_scores

