PATH = r'/home/ehsu/David_projects/LLM-IE_benchmark/benchmarks/Temporal event 2012/'

import os
import re
import xml.etree.ElementTree as ET

with open(os.path.join(PATH, 'doc_id', 'train_id')) as f:
    lines = f.readlines()
doc_ids = [line.strip() for line in lines]


sentence = "She had worsening abdominal pain on exam ."

for doc_id in doc_ids:
    with open(os.path.join(PATH, 'data', 'ann', f'{doc_id}.xml'), 'r') as file:
        xml_data = file.read()
        
    xml_data = re.sub(r'&(?!lt;|gt;|amp;|quot;|apos;)', '&amp;', xml_data)

    tree = ET.ElementTree(ET.fromstring(xml_data))
    root = tree.getroot()
    text = root.find('TEXT').text
    if sentence in text:
        print(f"Found sentence in {doc_id}")
        break

# find the sentence span in text
sentence_start = text.index(sentence)
sentence_end = sentence_start + len(sentence)


event_elements = root.find("TAGS").findall("EVENT")
for event_element in event_elements:
    attr = event_element.attrib
    if int(attr['start']) >= sentence_start and int(attr['end']) <= sentence_end:
        print({"entity_text": attr['text'], "entity_type": "EVENT", "type": attr['type'], "polarity": attr['polarity'], "modality": attr['modality']})

timex3_elements = root.find("TAGS").findall("TIMEX3")
for timex3_element in timex3_elements:
    attr = timex3_element.attrib
    if int(attr['start']) >= sentence_start and int(attr['end']) <= sentence_end:
        print({"entity_text": attr['text'], "entity_type": "TIMEX3", "type": attr['type'], "val": attr['val'], "mod": attr['mod']})

