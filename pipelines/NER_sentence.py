# -*- coding: utf-8 -*-
import argparse
from easydict import EasyDict
import yaml
import os
from tqdm import tqdm
from modules.Utilities import Information_Extraction_Document
from llm_ie.engines import OpenAIInferenceEngine
from llm_ie.extractors import SentenceFrameExtractor
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
    
    """ Load IE """
    logging.info("Loading IE document id...")
    with open(config['id_file']) as f:
        lines = f.readlines()
    doc_ids = [line.strip() for line in lines]

    if not os.path.isdir(os.path.join(config['out_dir'], config['run_name'])):
        os.makedirs(os.path.join(config['out_dir'], config['run_name']))

    exist = [f.replace('.llmie', '') for f in os.listdir(os.path.join(config['out_dir'], config['run_name']))]
    doc_ids_filtered = [f for f in doc_ids if f not in exist]
    logging.info(f"A set of {len(doc_ids_filtered)} created, dropped {len(doc_ids) - len(doc_ids_filtered)} exist.")
    
    logging.info(f"Loading IEs from {config['IE_dir']}...")
    IEs = []
    for doc_id in doc_ids_filtered:
        ie = Information_Extraction_Document(doc_id=doc_id, 
                                            filename=os.path.join(os.path.join(config['IE_dir'], f'{doc_id}.ie')))
        IEs.append(ie)
  
    logging.info(f"A total of {len(IEs)} IEs loaded.")
    
    """ Load inference engine """
    logging.info("Loading inference engine...")
    engine = OpenAIInferenceEngine(base_url=config['base_url'],
                                   api_key="EMPTY",
                                   model="meta-llama/Llama-3.3-70B-Instruct")
    
    """ Define extractor """
    logging.info("Define inference engine...")
    extractor = SentenceFrameExtractor(inference_engine=engine,
                                       prompt_template=prompt_template,
                                       system_prompt=config['system_prompt'])
    
    """ Extract """
    logging.info("Extracting...")                    
    loop = tqdm(IEs, total=len(IEs), leave=True)
    for ie in loop:
        loop.set_description(f"doc_id: {ie.doc_id}")
        frames = extractor.extract_frames(text_content=ie['text'], entity_key="entity_text", multi_turn=False, stream=False)
        doc = LLMInformationExtractionDocument(doc_id=ie['doc_id'], text=ie['text'])
        for frame in frames:
            doc.add_frame(frame, valid_mode="span", create_id=True)

        doc.save(os.path.join(config['out_dir'], config['run_name'], f"{doc.doc_id}.llmie"))

if __name__ == '__main__':
    main()
