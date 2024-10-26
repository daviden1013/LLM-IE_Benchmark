# -*- coding: utf-8 -*-
PATH = r"/home/ehsu/David_projects/llama2 weak supervision/benchmarks/PHI de-identification 2014/"
import os

train = [f.replace('.xml', '') for f in os.listdir(os.path.join(PATH, 'data', 'train')) if f[-4:] == '.xml']
test = [f.replace('.xml', '') for f in os.listdir(os.path.join(PATH, 'data', 'test')) if f[-4:] == '.xml']

with open(os.path.join(PATH, 'doc_id', 'train_id'), 'w') as f:
  for l in train:
    f.write("%s\n" % l)

    
with open(os.path.join(PATH, 'doc_id', 'test_id'), 'w') as f:
  for l in test:
    f.write("%s\n" % l)