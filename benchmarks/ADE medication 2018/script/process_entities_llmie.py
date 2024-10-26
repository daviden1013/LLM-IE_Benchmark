PATH = r'/home/ehsu/David_projects/LLM-IE_benchmark/'

from typing import Dict, Tuple
import random
import os
import sys
sys.path.insert(0, os.path.join(PATH, 'pipelines'))
from tqdm import tqdm

from modules.Utilities import Information_Extraction_Document
from llm_ie.data_types import LLMInformationExtractionFrame, LLMInformationExtractionDocument
from llm_ie.extractors import RelationExtractor

""" Load IEs """
with open(os.path.join(PATH, 'benchmarks', 'ADE medication 2018', 'doc_id', 'train_id')) as f:
    lines = f.readlines()
doc_ids = [line.strip() for line in lines]

IEs = []
for doc_id in doc_ids:
    ie = Information_Extraction_Document(doc_id=doc_id, 
                                        filename=os.path.join(os.path.join(PATH, 'benchmarks', 'ADE medication 2018', 'IE', f'{doc_id}.ie')))
    IEs.append(ie)

for ie in IEs:
    doc = LLMInformationExtractionDocument(doc_id=ie['doc_id'], text=ie['text'])
    for entity in ie['entity']:
        frame = LLMInformationExtractionFrame(frame_id=entity['entity_id'],
                                              start=entity['start'],
                                              end=entity['end'],
                                              entity_text=entity['entity_text'],
                                              attr={"EntityType": entity['entity_type']})
        doc.add_frame(frame)

    doc.save(os.path.join(PATH, 'benchmarks', 'ADE medication 2018', 'llmie', 'gold', f'{doc.doc_id}.llmie'))

