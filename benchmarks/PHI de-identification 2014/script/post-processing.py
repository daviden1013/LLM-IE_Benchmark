# -*- coding: utf-8 -*-
PATH = r'/home/ehsu/David_projects/LLM_guideline_prompt/benchmarks/PHI de-identification 2014/'

import argparse
from typing import List, Dict
import os
import pickle
import re
from tqdm import tqdm
import xml.etree.ElementTree as ET
from llm_ie.data_types import LLMInformationExtractionDocument

      
def main():
    parser = argparse.ArgumentParser()
    add_arg = parser.add_argument
    add_arg("-indir", "--indir", help='dir for input', type=str)
    add_arg("-outdir", "--outdir", help='dir for output', type=str)
    args = parser.parse_known_args()[0]
    
    labels = ['NAME_PATIENT',
              'NAME_DOCTOR',
              'NAME_USERNAME',
              'PROFESSION',
              'LOCATION_HOSPITAL',
              'LOCATION_ORGANIZATION',
              'LOCATION_STREET',
              'LOCATION_CITY',
              'LOCATION_STATE',
              'LOCATION_COUNTRY',
              'LOCATION_ZIP',
              'LOCATION_LOCATION-OTHER',
              'AGE',
              'DATE',
              'CONTACT_PHONE',
              'CONTACT_FAX',
              'CONTACT_EMAIL',
              'CONTACT_URL',
              'ID_BIOID',
              'ID_DEVICE',
              'ID_HEALTHPLAN',
              'ID_IDNUM',
              'ID_MEDICALRECORD']
    
    """ Load NER results """
    ann_filenames = os.listdir(args.indir)
    for ann_filename in ann_filenames:
        ie = LLMInformationExtractionDocument(filename=os.path.join(args.indir, ann_filename))

        tree = ET.parse(os.path.join(PATH, 'data', 'ann', f'{ie.doc_id}.xml'))
        root = tree.getroot()
        text = root.find('TEXT').text
    
        pred_elements = []
        for i, frame in enumerate(ie.frames):
            if frame.attr is None or 'entity_type' not in frame.attr or frame.attr['entity_type'] not in labels:
                continue

            entity_type = frame.attr['entity_type']
          
            if '_' in entity_type:
                name, entity_type = entity_type.split('_')
            else:
                name = entity_type
                entity_type = entity_type
            
            pred_elements.append(ET.Element(name, {"id": f"P{i}", "start": str(frame.start), "end": str(frame.end), "text": frame.entity_text, "TYPE": entity_type, "comment": ""}))
      
        # Create new output XML
        root_new = ET.Element("deIdi2b2")
        # Create the TEXT element and its text content
        text_element = ET.SubElement(root_new, "TEXT")
        text_element.text = text
        
        # Create the TAGS element
        tags_element = ET.SubElement(root_new, "TAGS")
        tags_element.extend(pred_elements)
        
        # Save the XML to a file
        tree = ET.ElementTree(root_new)
        tree.write(os.path.join(args.outdir, f"{ie.doc_id}.xml"), encoding='UTF-8', xml_declaration=True, method="xml")
        
if __name__ == '__main__':
    main()





