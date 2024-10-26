python vLLM_sentence.py -c "/home/ehsu/David_projects/LLM_guideline_prompt/benchmarks/ADE medication 2018/configs/Meta-Llama-3.1-70B-Instruct_float16_sentence.yaml" --n_subset 1 --subset 0

python vLLM_sentence_guide.py -c "/home/ehsu/David_projects/LLM_guideline_prompt/benchmarks/ADE medication 2018/configs/Meta-Llama-3.1-70B-Instruct_float16_sentence_guide.yaml" --n_subset 1 --subset 0

python vLLM_sentence.py -c "/home/ehsu/David_projects/LLM_guideline_prompt/benchmarks/ADE medication 2018/configs/Meta-Llama-3.1-70B-Instruct_float16_sentence_8shot.yaml" --n_subset 1 --subset 0

python vLLM_sentence_guide.py -c "/home/ehsu/David_projects/LLM_guideline_prompt/benchmarks/ADE medication 2018/configs/Meta-Llama-3.1-70B-Instruct_float16_sentence_guide_8shot.yaml" --n_subset 1 --subset 0