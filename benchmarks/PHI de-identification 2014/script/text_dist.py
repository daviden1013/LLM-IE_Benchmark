PATH = '/home/ehsu/David_projects/LLM_guideline_prompt/benchmarks/PHI de-identification 2014'

import os
import textdistance

with open(os.path.join(PATH, 'guideline', 'Llama-3.1-405B_generated_guideline.txt'), 'r') as f:
    guideline = f.read()

with open(os.path.join(PATH, 'guideline', 'Llama-3.1-405B_generated_guideline_modified.txt'), 'r') as f:
    modified = f.read()


textdistance.overlap.normalized_similarity(guideline, modified)
# 0.9975890704527189
