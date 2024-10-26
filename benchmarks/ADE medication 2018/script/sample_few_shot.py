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

""" Define functions """
extractor = RelationExtractor(inference_engine=None, 
                              prompt_template=None,
                              possible_relation_types_func=None)


def get_relation_sample(ie: Information_Extraction_Document, rel:Dict[str,str]) -> Tuple[str, str]:
    entity_1 = ie.get_entity_by_id(rel['entity_1_id'])
    frame_1 = LLMInformationExtractionFrame(frame_id=entity_1['entity_id'], 
                                            start=entity_1['start'],
                                            end=entity_1['end'],
                                            entity_text=entity_1['entity_text'],
                                            attr={"EntityType": entity_1['entity_type']})

    entity_2 = ie.get_entity_by_id(rel['entity_2_id'])
    frame_2 = LLMInformationExtractionFrame(frame_id=entity_2['entity_id'],
                                            start=entity_2['start'],
                                            end=entity_2['end'],
                                            entity_text=entity_2['entity_text'],
                                            attr={"EntityType": entity_2['entity_type']})


    roi = extractor._get_ROI(frame_1=frame_1, frame_2=frame_2, text=ie['text'])
    return roi, rel['relation_type']


def sample_k_integers(n, k, seed=None):
    if seed is not None:
        random.seed(seed)
    return random.sample(range(n + 1), k)


""" Load IEs """
with open(os.path.join(PATH, 'benchmarks', 'ADE medication 2018', 'doc_id', 'train_id')) as f:
    lines = f.readlines()
doc_ids = [line.strip() for line in lines]

IEs = []
for doc_id in doc_ids:
    ie = Information_Extraction_Document(doc_id=doc_id, 
                                        filename=os.path.join(os.path.join(PATH, 'benchmarks', 'ADE medication 2018', 'IE', f'{doc_id}.ie')))
    IEs.append(ie)

""" Sample relations """
for i in sample_k_integers(len(IEs), 8, seed=123):
    ie = IEs[i]
    j = sample_k_integers(len(ie['relation']), 1, seed=None)
    roi, relation_type = get_relation_sample(ie, ie['relation'][j[0]])
    print(f"ROI text:{roi}")
    print(f"Output:{relation_type}")
    print("\n\n")



