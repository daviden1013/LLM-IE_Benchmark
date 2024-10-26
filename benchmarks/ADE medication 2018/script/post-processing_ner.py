# -*- coding: utf-8 -*-
import argparse
import os
from llm_ie.data_types import LLMInformationExtractionDocument

      
def main():
    parser = argparse.ArgumentParser()
    add_arg = parser.add_argument
    add_arg("-indir", "--indir", help='dir for input', type=str)
    add_arg("-outdir", "--outdir", help='dir for output', type=str)
    args = parser.parse_known_args()[0]
    
    """ Load NER results """
    ann_filenames = os.listdir(args.indir)
    
    for ann_filename in ann_filenames:
        doc = LLMInformationExtractionDocument(filename=os.path.join(args.indir, ann_filename))
      
        t = ""
        for i, frame in enumerate(doc.frames):
            if frame.attr and 'entity_type' in frame.attr:
                if frame.attr['entity_type'] in ['Drug', 'Form', 'Strength', 'Frequency', 'Route', 'Dosage', 'Reason', 'ADE', 'Duration']:
                    t += f"T{i}	{frame.attr['entity_type']} {frame.start} {frame.end}	{frame.entity_text}\n"
          
        with open(os.path.join(args.outdir, f'{doc.doc_id}.ann'), 'w') as f:
            f.write(t)
        
if __name__ == '__main__':
    main()





