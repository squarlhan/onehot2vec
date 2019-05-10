# -*- coding: utf-8 -*-
import sys
import logging
import os
import gensim
from gensim.models import word2vec

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#word2vec model
# sentences = gensim.models.word2vec.LineSentence('feature.seq') 
# model = gensim.models.Word2Vec(sentences, hs=1,min_count=1,window=3,size=100) 
# model.save('word.model')

#doc2vec model
# sentences = gensim.models.doc2vec.TaggedLineDocument('feature.seq') 
# model = gensim.models.Doc2Vec(sentences,hs=1,min_count=1,size=100, window=3)
# model.train(sentences, total_examples=model.corpus_count, epochs=model.iter)
# model.save('doc.model')

#test
model = gensim.models.Doc2Vec.load('doc.model')
# for key in model.most_similar('p10_0', topn=10):
#     print(key)
# tt = 'p03_1 p04_2 p05_4 p06_0 p07_1 p08_0 p09_0 p10_0 p11_2 p12_13 p13_0 p14_0 p15_2 p16_0 p17_0 p18_0 p19_1 p20_4 p21_1 p22_2 p23_2 p24_1 p25_2 p26_1 p27_1 p28_1 p29_2 p30_1 p31_1 p32_1 p35_1 p36_0 p38_1 p38_7 p40_2 '
# vec = model.infer_vector(doc_words = tt.split(' '),alpha = 0.25, steps = 50)
# print(vec)

with open('feature.vec', 'a') as f_vec_file:
    with open('feature.seq', 'r') as f_seq_file:
        for line in f_seq_file:
            vec = model.infer_vector(doc_words = line.split(' '),alpha = 0.25, steps = 50)
            s = str(vec).replace('[','').replace(']','').replace('\n','')
            f_vec_file.write(s)
            f_vec_file.write('\n')