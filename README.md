This is a benchmark repo for the [LLM-IE](https://github.com/daviden1013/llm-ie) Python package. The 2012, 2014, and 2018 i2b2/ n2c2 datasets are used for benchmarking. Note that the datasets are NOT included in this repo in compliance to the data user agreements. To access the datasets, please refer to the [DBMI data portal](https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/). 



## Table of Contents
- [Overview](#overview)
- [Prerequisite](#prerequisite)
- [Methods](#methods)
    - [Named Entity Recognition](#named-entity-recognition)
    - [Entity Attribute Extraction](#entity-attribute-extraction)
    - [Relation Extraction](#relation-extraction)


## Overview
For the NER and EA tasks, the Sentence Frame Extractor achieved the best F1 scores, while consuming more GPU time. The Review Frame Extractor had higher recall than the Basic Frame Extractor on all NER tasks. 

<div align="center">
<table style="width: 677px;">
<tbody>
<tr>
<td style="width: 79px;">
<p><strong>Tasks</strong></p>
</td>
<td style="width: 65px;">
<p><strong>Algorithm</strong></p>
</td>
<td style="width: 188px;">
<p><strong>GPU time (s)/ Note</strong></p>
</td>
<td style="width: 368px;" colspan="6">
<p><strong>Benchmarks</strong></p>
</td>
</tr>
<tr>
<td style="width: 79px;" rowspan="18">
<p><strong>Named Entity Recognition</strong></p>
</td>
<td style="width: 65px;">
<p><strong>&nbsp;</strong></p>
</td>
<td style="width: 188px;">
<p><strong>&nbsp;</strong></p>
</td>
<td style="width: 368px;" colspan="6">
<p style="text-align: center;"><strong>2012 Temporal Relations Challenge</strong></p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>&nbsp;</p>
</td>
<td style="width: 188px;">
<p>&nbsp;</p>
</td>
<td style="width: 146px;" colspan="3">
<p style="text-align: center;">EVENT</p>
</td>
<td style="width: 222px;" colspan="3">
<p style="text-align: center;">TIMEX</p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>&nbsp;</p>
</td>
<td style="width: 188px;">
<p>&nbsp;</p>
</td>
<td style="width: 26px;">
<p>Precision</p>
</td>
<td style="width: 64.1px;">
<p>Recall</p>
</td>
<td style="width: 55.9px;">
<p>F1</p>
</td>
<td style="width: 62px;">
<p>Precision</p>
</td>
<td style="width: 92px;">
<p>Recall</p>
</td>
<td style="width: 68px;">
<p>F1</p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>Basic</p>
</td>
<td style="width: 188px;">
<p>67.5</p>
</td>
<td style="width: 26px;">
<p>0.9406</p>
</td>
<td style="width: 64.1px;">
<p>0.2841</p>
</td>
<td style="width: 55.9px;">
<p>0.4364</p>
</td>
<td style="width: 62px;">
<p>0.9595</p>
</td>
<td style="width: 92px;">
<p>0.3516</p>
</td>
<td style="width: 68px;">
<p>0.5147</p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>Review</p>
</td>
<td style="width: 188px;">
<p>84.0</p>
</td>
<td style="width: 26px;">
<p>0.8965</p>
</td>
<td style="width: 64.1px;">
<p>0.3995</p>
</td>
<td style="width: 55.9px;">
<p>0.5527</p>
</td>
<td style="width: 62px;">
<p>0.9352</p>
</td>
<td style="width: 92px;">
<p>0.5473</p>
</td>
<td style="width: 68px;">
<p>0.6905</p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>Sentence</p>
</td>
<td style="width: 188px;">
<p>132.9</p>
</td>
<td style="width: 26px;">
<p>0.9101</p>
</td>
<td style="width: 64.1px;">
<p>0.6824</p>
</td>
<td style="width: 55.9px;">
<p>0.7799</p>
</td>
<td style="width: 62px;">
<p>0.8891</p>
</td>
<td style="width: 92px;">
<p>0.739</p>
</td>
<td style="width: 68px;">
<p>0.8071</p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>&nbsp;</p>
</td>
<td style="width: 188px;">
<p><strong>&nbsp;</strong></p>
</td>
<td style="width: 368px;" colspan="6">
<p style="text-align: center;"><strong>2014 De-identification Challenge</strong></p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>&nbsp;</p>
</td>
<td style="width: 188px;">
<p>&nbsp;</p>
</td>
<td style="width: 146px;" colspan="3">
<p style="text-align: center;">Strict</p>
</td>
<td style="width: 222px;" colspan="3">
<p style="text-align: center;">Relaxed</p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>&nbsp;</p>
</td>
<td style="width: 188px;">
<p>&nbsp;</p>
</td>
<td style="width: 26px;">
<p>Precision</p>
</td>
<td style="width: 64.1px;">
<p>Recall</p>
</td>
<td style="width: 55.9px;">
<p>F1</p>
</td>
<td style="width: 62px;">
<p>Recall</p>
</td>
<td style="width: 92px;">
<p>Precision</p>
</td>
<td style="width: 68px;">
<p>F1</p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>Basic</p>
</td>
<td style="width: 188px;">
<p>9.4</p>
</td>
<td style="width: 26px;">
<p>0.7154</p>
</td>
<td style="width: 64.1px;">
<p>0.4813</p>
</td>
<td style="width: 55.9px;">
<p>0.5755</p>
</td>
<td style="width: 62px;">
<p>0.7172</p>
</td>
<td style="width: 92px;">
<p>0.4826</p>
</td>
<td style="width: 68px;">
<p>0.5769</p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>Review</p>
</td>
<td style="width: 188px;">
<p>15.7</p>
</td>
<td style="width: 26px;">
<p>0.5649</p>
</td>
<td style="width: 64.1px;">
<p>0.5454</p>
</td>
<td style="width: 55.9px;">
<p>0.555</p>
</td>
<td style="width: 62px;">
<p>0.5667</p>
</td>
<td style="width: 92px;">
<p>0.5471</p>
</td>
<td style="width: 68px;">
<p>0.5567</p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>Sentence</p>
</td>
<td style="width: 188px;">
<p>20.7</p>
</td>
<td style="width: 26px;">
<p>0.6683</p>
</td>
<td style="width: 64.1px;">
<p>0.7379</p>
</td>
<td style="width: 55.9px;">
<p>0.7014</p>
</td>
<td style="width: 62px;">
<p>0.6703</p>
</td>
<td style="width: 92px;">
<p>0.7401</p>
</td>
<td style="width: 68px;">
<p>0.7035</p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>&nbsp;</p>
</td>
<td style="width: 188px;">
<p><strong>&nbsp;</strong></p>
</td>
<td style="width: 368px;" colspan="6">
<p style="text-align: center;"><strong>2018 (Track 2) ADE and Medication Extraction Challenge</strong></p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>&nbsp;</p>
</td>
<td style="width: 188px;">
<p>&nbsp;</p>
</td>
<td style="width: 146px;" colspan="3">
<p style="text-align: center;">Strict</p>
</td>
<td style="width: 222px;" colspan="3">
<p style="text-align: center;">Lenient</p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>&nbsp;</p>
</td>
<td style="width: 188px;">
<p>&nbsp;</p>
</td>
<td style="width: 26px;">
<p>Precision</p>
</td>
<td style="width: 64.1px;">
<p>Recall</p>
</td>
<td style="width: 55.9px;">
<p>F1</p>
</td>
<td style="width: 62px;">
<p>Recall</p>
</td>
<td style="width: 92px;">
<p>Precision</p>
</td>
<td style="width: 68px;">
<p>F1</p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>Basic</p>
</td>
<td style="width: 188px;">
<p>44.3</p>
</td>
<td style="width: 26px;">
<p>0.7384</p>
</td>
<td style="width: 64.1px;">
<p>0.3534</p>
</td>
<td style="width: 55.9px;">
<p>0.478</p>
</td>
<td style="width: 62px;">
<p>0.8537</p>
</td>
<td style="width: 92px;">
<p>0.4034</p>
</td>
<td style="width: 68px;">
<p>0.5479</p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>Review</p>
</td>
<td style="width: 188px;">
<p>63.2</p>
</td>
<td style="width: 26px;">
<p>0.7209</p>
</td>
<td style="width: 64.1px;">
<p>0.427</p>
</td>
<td style="width: 55.9px;">
<p>0.5363</p>
</td>
<td style="width: 62px;">
<p>0.8416</p>
</td>
<td style="width: 92px;">
<p>0.4918</p>
</td>
<td style="width: 68px;">
<p>0.6208</p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>Sentence</p>
</td>
<td style="width: 188px;">
<p>114.1</p>
</td>
<td style="width: 26px;">
<p>0.852</p>
</td>
<td style="width: 64.1px;">
<p>0.6166</p>
</td>
<td style="width: 55.9px;">
<p>0.7154</p>
</td>
<td style="width: 62px;">
<p>0.963</p>
</td>
<td style="width: 92px;">
<p>0.692</p>
</td>
<td style="width: 68px;">
<p>0.8053</p>
</td>
</tr>
<tr>
<td style="width: 79px;" rowspan="6">
<p><strong>Entity Attribute Extraction</strong></p>
</td>
<td style="width: 65px;">
<p>&nbsp;</p>
</td>
<td style="width: 188px;">
<p><strong>&nbsp;</strong></p>
</td>
<td style="width: 368px;" colspan="6">
<p style="text-align: center;"><strong>2012 Temporal Relations Challenge</strong></p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>&nbsp;</p>
</td>
<td style="width: 188px;">
<p>&nbsp;</p>
</td>
<td style="width: 146px;" colspan="3">
<p style="text-align: center;">EVENT</p>
</td>
<td style="width: 222px;" colspan="3">
<p style="text-align: center;">TIMEX</p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>&nbsp;</p>
</td>
<td style="width: 188px;">
<p>&nbsp;</p>
</td>
<td style="width: 26px;">
<p>Type</p>
</td>
<td style="width: 64.1px;">
<p>Polarity</p>
</td>
<td style="width: 55.9px;">
<p>Modality</p>
</td>
<td style="width: 62px;">
<p>Type</p>
</td>
<td style="width: 92px;">
<p>Value</p>
</td>
<td style="width: 68px;">
<p>Modifier</p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>Basic</p>
</td>
<td style="width: 188px;">
<p>67.5</p>
</td>
<td style="width: 26px;">
<p>0.2589</p>
</td>
<td style="width: 64.1px;">
<p>0.2707</p>
</td>
<td style="width: 55.9px;">
<p>0.2737</p>
</td>
<td style="width: 62px;">
<p>0.3236</p>
</td>
<td style="width: 92px;">
<p>0.2835</p>
</td>
<td style="width: 68px;">
<p>0.3198</p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>Review</p>
</td>
<td style="width: 188px;">
<p>84.0</p>
</td>
<td style="width: 26px;">
<p>0.358</p>
</td>
<td style="width: 64.1px;">
<p>0.3799</p>
</td>
<td style="width: 55.9px;">
<p>0.3828</p>
</td>
<td style="width: 62px;">
<p>0.4934</p>
</td>
<td style="width: 92px;">
<p>0.4209</p>
</td>
<td style="width: 68px;">
<p>0.4857</p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>Sentence</p>
</td>
<td style="width: 188px;">
<p>132.9</p>
</td>
<td style="width: 26px;">
<p>0.6056</p>
</td>
<td style="width: 64.1px;">
<p>0.642</p>
</td>
<td style="width: 55.9px;">
<p>0.6432</p>
</td>
<td style="width: 62px;">
<p>0.678</p>
</td>
<td style="width: 92px;">
<p>0.5505</p>
</td>
<td style="width: 68px;">
<p>0.667</p>
</td>
</tr>
<tr>
<td style="width: 79px;" rowspan="3">
<p><strong>Relation Extraction</strong></p>
</td>
<td style="width: 65px;">
<p>&nbsp;</p>
</td>
<td style="width: 188px;">
<p><strong>&nbsp;</strong></p>
</td>
<td style="width: 368px;" colspan="6">
<p style="text-align: center;"><strong>2018 (Track 2) ADE and Medication Extraction Challenge</strong></p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>&nbsp;</p>
</td>
<td style="width: 188px;">
<p>&nbsp;</p>
</td>
<td style="width: 90.1px;" colspan="2">
<p>Precision</p>
</td>
<td style="width: 117.9px;" colspan="2">
<p>Recall</p>
</td>
<td style="width: 160px;" colspan="2">
<p>F1</p>
</td>
</tr>
<tr>
<td style="width: 65px;">
<p>Multi-class</p>
</td>
<td style="width: 188px;">
<p>213.9</p>
</td>
<td style="width: 90.1px;" colspan="2">
<p>0.3831</p>
</td>
<td style="width: 117.9px;" colspan="2">
<p>0.978</p>
</td>
<td style="width: 160px;" colspan="2">
<p>0.5505</p>
</td>
</tr>
</tbody>
</table>
</div>

## Prerequisite
All the experiments were conducted with the [LLM-IE](https://github.com/daviden1013/llm-ie) Python package and [vLLM](https://github.com/vllm-project/vllm) inference engine. 

```python
pip install llm-ie==0.3.1
pip install vllm==0.5.4
```

We used the [OpenAI compatible server](https://docs.vllm.ai/en/v0.6.0/serving/openai_compatible_server.html) to run Llama-3.1-70B-Instruct. 

```cmd
vllm serve meta-llama/Meta-Llama-3.1-70B-Instruct --api-key EMPTY --tensor-parallel-size 4 --enable-prefix-caching
```

## Methods
The full code is available in the [pipeline](/pipelines/). The configuration files are in the `config` directories: [2012 i2b2](/benchmarks/Temporal%20event%202012/configs/), [2014 i2b2](/benchmarks/PHI%20de-identification%202014/configs/), and [2018 n2c2](/benchmarks/ADE%20medication%202018/configs/). Below are technical highlights for each task. 

### Named Entity Recognition
We use the Sentence frame extraction pipeline to demo. The full code is available [NER_sentence.py](/pipelines/NER_sentence.py). 

We import the inference engine, extractor (prompting algorithm), and document (for entity output storage) from the LLM-IE.

```python
from llm_ie.engines import OpenAIInferenceEngine
from llm_ie.extractors import SentenceFrameExtractor
from llm_ie.data_types import LLMInformationExtractionDocument
```

Define inference engine. Since we use vLLM's OpenAI compatible server, we use `OpenAIInferenceEngine`. The `config['base_url']` is `http://localhost:8000/v1` following the default. 
```python
engine = OpenAIInferenceEngine(base_url=config['base_url'],
                               api_key="EMPTY",
                               model="meta-llama/Meta-Llama-3.1-70B-Instruct")
```

Define extractor with prompt template and system prompt. the full prompt templates are in the `prompt_templates` directories under each benchmark. The system prompt for all tasks is "*You are a highly skilled clinical AI assistant, proficient in reviewing clinical notes and performing accurate information extraction*"
```python
extractor = SentenceFrameExtractor(inference_engine=engine,
                                   prompt_template=prompt_template,
                                   system_prompt=config['system_prompt'])
```

Iterate through all documents and extract frames with the `extractor.extract_frames()` method. The extracted frames are stored in the `LLMInformationExtractionDocument` and save to disk. 
```python
loop = tqdm(IEs, total=len(IEs), leave=True)
for ie in loop:
    loop.set_description(f"doc_id: {ie.doc_id}")
    frames = extractor.extract_frames(text_content=ie['text'], entity_key="entity_text", multi_turn=False, stream=False)
    doc = LLMInformationExtractionDocument(doc_id=ie['doc_id'], text=ie['text'])
    for frame in frames:
        doc.add_frame(frame, valid_mode="span", create_id=True)

    doc.save(os.path.join(config['out_dir'], config['run_name'], f"{doc.doc_id}.llmie"))
```

### Entity Attribute Extraction
The named entity recognition and entity attribute extraction use the same pipeline, following the steps above. The only difference is the prompt template. The Schema defines the attributes.

```
...
# Schema definition
Your output should contain: 
    "entity_text": the exact wording as mentioned in the note.
    "entity_type": type of the entity. It should be one of the "EVENT" or "TIMEX3".
    if entity_type is "EVENT",
        "type": the event type as one of the "TEST", "PROBLEM", "TREATMENT", "CLINICAL_DEPT", "EVIDENTIAL", or "OCCURRENCE".
        "polarity": whether an EVENT is positive ("POS") or negative ("NAG"). For example, in “the patient reports headache, and denies chills”, the EVENT [headache] is positive in its polarity, and the EVENT [chills] is negative in its polarity.
        "modality": whether an EVENT actually occurred or not. Must be one of the "FACTUAL", "CONDITIONAL", "POSSIBLE", or "PROPOSED".

    if entity_type is "TIMEX3",
        "type": the type as one of the "DATE", "TIME", "DURATION", or "FREQUENCY".
        "val": the numeric value 1) DATE: [YYYY]-[MM]-[DD], 2) TIME: [hh]:[mm]:[ss], 3) DURATION: P[n][Y/M/W/D]. So, “for eleven days” will be 
represented as “P11D”, meaning a period of 11 days. 4)  R[n][duration], where n denotes the number of repeats. When the n is omitted, the expression denotes an unspecified amount of repeats. For example, “once a day for 3 days” is “R3P1D” (repeat the time interval of 1 day (P1D) for 3 times (R3)), twice every day is “RP12H” (repeat every 12 hours)
        "mod": additional information regarding the temporal value of a time expression. Must be one of the:
            “NA”: the default value, no relevant modifier is present;  
            “MORE”, means “more than”, e.g. over 2 days (val = P2D, mod = MORE);  
            “LESS”, means “less than”, e.g. almost 2 months (val = P2M, mod=LESS); 
            “APPROX”, means “approximate”, e.g. nearly a week (val = P1W, mod=APPROX);  
            “START”, describes the beginning of a period of time, e.g.  Christmas morning, 2005 (val= 2005-12-25, mod= START).  
            “END”, describes the end of a period of time, e.g. late last year, (val = 2010, mod = END)
            “MIDDLE”, describes the middle of a period of time, e.g. mid-September 2001 (val = 2001-09, mod = MIDDLE) 

# Output format definition
Your output should follow JSON format, 
if there are one of the EVENT or TIMEX3 entity mentions:
    [
        {"entity_text": "<Exact entity mentions as in the note>", "entity_type": "EVENT", "type": "<event type>", "polarity": "<event polarity>", "modality": "<event modality>"},
        {"entity_text": "<Exact entity mentions as in the note>", "entity_type": "TIMEX3", "type": "<TIMEX3 type>", "val": "<time value>", "mod": "<additional information>"}
        ...
     ]
if there is no entity mentioned in the given sentence, just output an empty list:
    []

I am only interested in the extracted contents in []. Do NOT explain your answer.
...
```

### Relation Extraction
The full code is available [RE_multiclass](/pipelines/RE_multiclass.py).

We import the `MultiClassRelationExtractor` class for relation extraction.

```python
from llm_ie.engines import OpenAIInferenceEngine
from llm_ie.extractors import MultiClassRelationExtractor
from llm_ie.data_types import LLMInformationExtractionDocument
```

Define inference engine. Since we use vLLM's OpenAI compatible server, we use `OpenAIInferenceEngine`. The `config['base_url']` is `http://localhost:8000/v1` following the default. 
```python
engine = OpenAIInferenceEngine(base_url=config['base_url'],
                               api_key="EMPTY",
                               model="meta-llama/Meta-Llama-3.1-70B-Instruct")
```

We define a Python function `possible_relation_types_func()` that inputs 2 frames and outputs the possible relation types between them. In this dataset, there are relations:
- Strength-Drug: this is a relationship between the drug strength and its name.
- Dosage-Drug: this is a relationship between the drug dosage and its name.
- Duration-Drug: this is a relationship between a drug duration and its name.
- Frequency-Drug: this is a relationship between a drug frequency and its name.
- Form-Drug: this is a relationship between a drug form and its name.
- Route-Drug: this is a relationship between the route of administration for a drug and its name.
- Reason-Drug: this is a relationship between the reason for which a drug was administered (e.g., symptoms, diseases, etc.) and a drug name.
- ADE-Drug: this is a relationship between an adverse drug event (ADE) and a drug name. 

The `possible_relation_types_func()` returns `[]` ("no relation") when the 2 frames are over 500 characters apart. If the entity types are a *Drug* and something else, return the *something-Drug* relation type. Else return `[]`.

```python
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
```

Define extractor and pass the `possible_relation_types_func()`.

```python
extractor = MultiClassRelationExtractor(inference_engine=engine,
                                        prompt_template=prompt_template,
                                        system_prompt=config['system_prompt'],
                                        possible_relation_types_func=possible_relation_types_func)
```

Run extractor with `extractor.extract_relations()` and add the relations to the document object. Then save to disk. 

```python
loop = tqdm(docs, total=len(docs), leave=True)
for doc in loop:
    loop.set_description(f"doc_id: {doc.doc_id}")
    relations = extractor.extract_relations(doc=doc, stream=False)
    doc.add_relations(relations)
    doc.save(os.path.join(config['out_dir'], config['run_name'], f"{doc.doc_id}.llmie"))
```
