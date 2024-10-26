# -*- coding: utf-8 -*-
PATH = r'/home/ehsu/David_projects/LLM-IE_benchmark/benchmarks/Temporal event 2012/'

import argparse
from typing import List, Dict
import os
import re
import xml.etree.ElementTree as ET
from llm_ie.data_types import LLMInformationExtractionDocument

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def main():
    parser = argparse.ArgumentParser()
    add_arg = parser.add_argument
    add_arg("-indir", "--indir", help='dir for input', type=str)
    add_arg("-outdir", "--outdir", help='dir for output', type=str)
    args = parser.parse_known_args()[0]

    labels = ['EVENT', 'TIMEX3']

    """ Load NER results """
    ann_filenames = os.listdir(args.indir) 
    for ann_filename in ann_filenames:
        doc = LLMInformationExtractionDocument(filename=os.path.join(args.indir, ann_filename))
  
        with open(os.path.join(PATH, 'data', 'ann', f'{doc.doc_id}.xml'), 'r') as file:
            xml_data = file.read()
    
        xml_data = re.sub(r'&(?!lt;|gt;|amp;|quot;|apos;)', '&amp;', xml_data)

        tree = ET.ElementTree(ET.fromstring(xml_data))
        root = tree.getroot()
        text = root.find('TEXT').text
    
        pred_elements = []
        for i, frame in enumerate(doc.frames):
            if frame.attr is None or 'entity_type' not in frame.attr or frame.attr['entity_type'] not in labels:
                continue

            name = frame.attr['entity_type']
            entity_type = frame.attr['entity_type']
            
            if entity_type == 'EVENT':
                type = frame.attr["type"] if "type" in frame.attr else "FACTUAL"
                polarity = frame.attr["polarity"] if "polarity" in frame.attr else "POS"
                modality = frame.attr["modality"] if "modality" in frame.attr else "NA"
                pred_elements.append(ET.Element(name, {"id": f"E{i}", "start": str(frame.start), "end": str(frame.end), "text": frame.entity_text, "modality": modality, "polarity": polarity, "type":type}))
        
            elif entity_type == 'TIMEX3':
                type = frame.attr["type"] if "type" in frame.attr else "DATE"
                val = frame.attr["val"] if "val" in frame.attr else ""
                mod = frame.attr["mod"] if "mod" in frame.attr else "NA"
                pred_elements.append(ET.Element(name, {"id": f"T{i}", "start": str(frame.start), "end": str(frame.end), "text": frame.entity_text, "type": type, "val":val, "mod":mod}))
        
            # Create new output XML
            root_new = ET.Element("ClinicalNarrativeTemporalAnnotation")
            # Create the TEXT element and its text content
            text_element = ET.SubElement(root_new, "TEXT")
            text_element.text = text
            
            # Create the TAGS element
            tags_element = ET.SubElement(root_new, "TAGS")
            tags_element.extend(pred_elements)
            
            # Save the XML to a file
            indent(root_new)
            tree = ET.ElementTree(root_new)
            tree.write(os.path.join(args.outdir, f"{doc.doc_id}.xml"), encoding='UTF-8', xml_declaration=True, method="xml")
        
if __name__ == '__main__':
  main()





