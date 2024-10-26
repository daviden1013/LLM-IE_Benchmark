PATH = "/home/ehsu/David_projects/LLM_guideline_prompt/"

from typing import List
import os
import sys
sys.path.insert(0, os.path.join(PATH, 'pipelines'))
from modules.Utilities import Information_Extraction_Document
from nltk.tokenize.punkt import PunktSentenceTokenizer
import pandas as pd
from tqdm import tqdm


def get_sentences(ie) -> List[int]:
    sentences = []
    for start, end in PunktSentenceTokenizer().span_tokenize(ie['text']):
        entity_count = 0
        for entity in ie['entity']:
            if entity['start'] >= start and entity['end'] <= end:
                entity_count += 1

        sentences.append({"doc_id":ie.doc_id, "start": start, "end": end, "n_entities": entity_count}) 

    return sentences


with open(os.path.join(PATH, 'benchmarks', 'Temporal event 2012', 'doc_id', 'test_id')) as f:
    lines = f.readlines()
test_ids = [line.strip() for line in lines]

count_list = []
filenames = os.listdir(os.path.join(PATH, 'benchmarks', 'Temporal event 2012', 'IE'))
testset_filenames = [f for f in filenames if f.replace('.ie', '') in test_ids]
loop = tqdm(testset_filenames, total=len(testset_filenames), leave=True)
for filename in loop:
    count = {}
    doc_id = filename.replace('.ie', '')
    ie = Information_Extraction_Document(doc_id=doc_id, filename=os.path.join(PATH, 'benchmarks', 'Temporal event 2012', 'IE', filename))
    count_list.extend(get_sentences(ie))


df = pd.DataFrame(count_list)

n_notes = len(df['doc_id'].unique())
n_sentences = df.shape[0]
n_entities = df['n_entities'].sum()
mean_entities = df['n_entities'].mean()
std_entities = df['n_entities'].std()
median_entities = df['n_entities'].median()
q1 = df['n_entities'].quantile(0.25)
q3 = df['n_entities'].quantile(0.75)
doc_level = df.groupby('doc_id').agg({'n_entities':'sum'})
doc_median = doc_level['n_entities'].median()
doc_q1 = doc_level['n_entities'].quantile(0.25)
doc_q3 = doc_level['n_entities'].quantile(0.75)

[n_notes,
n_sentences,
n_entities,
f'{median_entities} [{q1},{q3}]',
f'{mean_entities:.2f} ({std_entities:.2f})',
f'{doc_median} [{doc_q1},{doc_q3}]']
