from llm_ie.engines import LlamaCppInferenceEngine
from llm_ie.extractors import SentenceFrameExtractor, BinaryRelationExtractor
from llm_ie.data_types import LLMInformationExtractionDocument

# Load synthesized medical note
note_text = """**Patient:** John Doe, 45 M  
**Physician:** Dr. Emily Johnson, Cardiologist, Green Valley Hospital

---

John is a 45-year-old male with a history of hypertension (dx 2015), Type 2 diabetes (dx 2018), and hyperlipidemia. He has been experiencing 
increased angina episodes since July 2024. He initially presented with complaints of occasional dizziness and fatigue, likely due to 
Lisinopril 10 mg daily.

**Meds Adjustments:**  
- Lisinopril was reduced to 5 mg daily, but the patient later developed a persistent dry cough (suspected ADR). Switched to Losartan 50 mg daily, 
which resolved the cough.
- Added Atorvastatin 20 mg daily in May 2024 for cholesterol control but caused muscle cramps. Switched to Rosuvastatin 10 mg daily in June 2024.
- Noticed palpitations and headaches since starting Sitagliptin 100 mg daily for better glucose control. Reduced to 50 mg due to GI upset and 
added Pantoprazole 20 mg.

**Current Meds:**  
- Losartan 50 mg daily  
- Metformin 500 mg BID  
- Rosuvastatin 10 mg daily  
- Sitagliptin 50 mg daily + Pantoprazole 20 mg daily  
- Carvedilol 12.5 mg BID (increased from 6.25 mg for angina)

---

**Plan:**  
Dr. Johnson advised John to monitor his blood pressure closely and keep a log of any side effects or new symptoms, especially related to the 
recent medication changes. Follow-up scheduled for October 2024 to reassess symptom control, particularly regarding angina frequency and GI 
symptoms.
"""

llm = LlamaCppInferenceEngine(repo_id="bullerwins/Meta-Llama-3.1-70B-Instruct-GGUF",
	                          gguf_filename="Meta-Llama-3.1-70B-Instruct-Q8_0-00001-of-00002.gguf",
                              n_ctx=16000,
                              verbose=False)

prompt_template = """
# Task description
The paragraph below is from a clinical note. Please carefully review it and extract the condition, medication, and adverse drug events (ADE). 

# Schema definition
Your output should contain: 
    "Type" which is the type of entity ("Condition", "Drug", or "ADE"),
    "EntityText" which is the text of the entity as spelled in the note text.
    if Type is "Drug", you should also include:
        "Dosage" key (e.g., "10 mg") 
        "Frequency" key (e.g., "once daily")
    if Type is "Condition", you should not include:
        "Assertion" key which is one of the "presence", "absence", and "possible". 
        "Date" key which is the date of the condition diagnosis. If the date is not available, you can ignore this key.

# Output format definition
Your output should follow JSON format, for example:
[
    {"Type": "Drug", "EntityText": "<entity text>", "Dosage": "<dosage>", "Frequency": "<frequency>"},
    {"Type": "Condition", "EntityText": "<entity text>", "Assertion": "<assertion>", "Date": "<date>"},
    {"Type": "ADE", "EntityText": "<entity text>"}
]

I am only insterested in the outputs in the []. Do Not explain your answer. 

# Additional hints
Your output should be 100% based on the provided content. DO NOT output fake information. 
If there are multiple conditions, drugs, or ADEs, please provide them separately.

# Input placeholder
Below is the medical study paragraph:
{{input}}
"""

# Define extractor
extractor = SentenceFrameExtractor(llm, prompt_template, system_prompt="You are a helpful medical AI assistant.")

# Extract
frames =  extractor.extract_frames(note_text, entity_key="EntityText", stream=True)

# Check extractions
for frame in frames:
    print(frame.to_dict())

# Define document
doc = LLMInformationExtractionDocument(doc_id="Meidcal note", text=note_text)

# Add frames to document
doc.add_frames(frames, valid_mode="span", create_id=True)


prompt_template = """
# Task description
This is a binary relation extraction task. Given a region of interest (ROI) text and two entities from a medical note, indicate the relation existence between the two entities.

# Schema definition
    True: if there is a relationship between a Drug (one of the entities) and either a Condition (the other entity) or an ADE (the other entity).
    False: Otherwise.

# Output format definition
Your output should follow the JSON format:
{"Relation": "<True or False>"}

# Hints
    1. Your input always contains one Drug entity and either 1) one Condition entity or 2) one ADE entity.
    2. Pay attention to the Drug entity and see if the Condition or ADE is related to it.
    3. If the Condition or ADE is for another Drug, output False. 
    4. If the Condition or ADE is for the same Drug but at a different location (span), output False.

# Entity 1 full information:
{{frame_1}}

# Entity 2 full information:
{{frame_2}}

# Input placeholders
ROI Text with the two entities annotated with <entity_1> and <entity_2>:
"{{roi_text}}"
"""

from typing import List

def possible_relation_func(frame_1, frame_2) -> bool:
    # If the two frames are > 500 characters apart, we assume "No Relation"
    if abs(frame_1.start - frame_2.start) > 500:
        return []
    
    # If the two frames are "Medication" and "Strength", the only possible relation types are "Strength-Drug" or "No Relation"
    if (frame_1.attr["Type"] == "Drug" and frame_2.attr["Type"] == "Condition") or \
        (frame_2.attr["Type"] == "Drug" and frame_1.attr["Type"] == "Condition"):
        return True
    
    # If the two frames are "Medication" and "Frequency", the only possible relation types are "Frequency-Drug" or "No Relation"
    if (frame_1.attr["Type"] == "Drug" and frame_2.attr["Type"] == "ADE") or \
        (frame_2.attr["Type"] == "Drug" and frame_1.attr["Type"] == "ADE"):
        return True

    return False

# Define relation extractor
relation_extractor = BinaryRelationExtractor(llm, prompt_template=prompt_template, possible_relation_func=possible_relation_func)

# Extract multi-class relations
relations = relation_extractor.extract_relations(doc, stream=True)

print(relations)

doc.add_relations(relations)

doc.viz_serve(color_attr_key="Type")

html = doc.viz_render(color_attr_key="Type")

import os
with open(os.path.join("/home/daviden1013/David_projects/llm-ie", "demo_ADE_extraction.html"), "w") as f:
    f.write(html)

