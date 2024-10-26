# -*- coding: utf-8 -*-
from typing import List
import argparse
from easydict import EasyDict
import yaml
import os
from tqdm import tqdm
from llm_ie.engines import OpenAIInferenceEngine
from llm_ie.extractors import MultiClassRelationExtractor
from llm_ie.data_types import LLMInformationExtractionDocument
import logging


def main():
    parser = argparse.ArgumentParser()
    add_arg = parser.add_argument
    add_arg("-c", "--config", help='dir to config file', type=str)
    args = parser.parse_known_args()[0]
    
    """ Load config"""
    with open(args.config) as yaml_file:
        config = EasyDict(yaml.safe_load(yaml_file))

    """ Logging """
    log_file = os.path.join(config['log_dir'], f"{config['run_name']}.txt")
    logging.basicConfig(format='%(asctime)s - %(message)s', filename=log_file, level=logging.INFO)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(asctime)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    logging.getLogger().addHandler(console_handler)

    logging.info('LLM in-context learning pipeline started')
    
    """ Load prompt """
    logging.info(f"Loading prmopt template from {config['prompt_template']}")
    with open(config['prompt_template'], 'r') as f:
        prompt_template = f.read()
    
    """ Load llmie """
    logging.info("Loading test document id...")
    with open(config['id_file']) as f:
        lines = f.readlines()
    doc_ids = [line.strip() for line in lines]

    if not os.path.isdir(os.path.join(config['out_dir'], config['run_name'])):
        os.makedirs(os.path.join(config['out_dir'], config['run_name']))

    exist = [f.replace('.llmie', '') for f in os.listdir(os.path.join(config['out_dir'], config['run_name']))]
    doc_ids_filtered = [f for f in doc_ids if f not in exist]
    logging.info(f"A set of {len(doc_ids_filtered)} created, dropped {len(doc_ids) - len(doc_ids_filtered)} exist.")
    
    logging.info(f"Loading IEs from {config['llmie_dir']}...")
    docs = []
    for doc_id in doc_ids_filtered:
        doc = LLMInformationExtractionDocument(filename=os.path.join(os.path.join(config['llmie_dir'], f'{doc_id}.llmie')))
        docs.append(doc)
  
    logging.info(f"A total of {len(docs)} llmie loaded.")
    
    """ Load inference engine """
    logging.info("Loading inference engine...")
    engine = OpenAIInferenceEngine(base_url=config['base_url'],
                                   api_key="EMPTY",
                                   model="meta-llama/Meta-Llama-3.1-70B-Instruct")
    """ Load relation function """
    if 'ADE medication 2018' in config['prompt_template']:
        def possible_relation_types_func(frame_1, frame_2) -> List[str]:
            # If the two frames are > 500 characters apart, we assume "No Relation"
            if abs(frame_1.start - frame_2.start) > 200:
                return []
            
            # If the two frames are "Drug" and an attribute entity
            if (frame_1.attr["EntityType"] == "Drug" and frame_2.attr["EntityType"] != "Drug"):
                return [f'{frame_2.attr["EntityType"]}-Drug']
            if (frame_2.attr["EntityType"] == "Drug" and frame_1.attr["EntityType"] != "Drug"):
                return [f'{frame_1.attr["EntityType"]}-Drug']

            return []

    """ Define extractor """
    logging.info("Define extractor...")
    extractor = MultiClassRelationExtractor(inference_engine=engine,
                                            prompt_template=prompt_template,
                                            system_prompt=config['system_prompt'],
                                            possible_relation_types_func=possible_relation_types_func)
    
    """ Extract """
    logging.info("Extracting...")                    
    loop = tqdm(docs, total=len(docs), leave=True)
    for doc in loop:
        loop.set_description(f"doc_id: {doc.doc_id}")
        relations = extractor.extract_relations(doc=doc, stream=False)
        doc.add_relations(relations)
        doc.save(os.path.join(config['out_dir'], config['run_name'], f"{doc.doc_id}.llmie"))

if __name__ == '__main__':
    main()
