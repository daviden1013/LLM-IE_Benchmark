cd /home/ehsu/David_projects/LLM-IE_benchmark/pipelines

# python RE_multiclass.py -c "/home/ehsu/David_projects/LLM-IE_benchmark/benchmarks/ADE medication 2018/configs/Meta-Llama-3.1-70B-Instruct_float16_re_multiclass.yaml"
# python NER_basic.py -c "/home/ehsu/David_projects/LLM-IE_benchmark/benchmarks/ADE medication 2018/configs/Meta-Llama-3.1-70B-Instruct_float16_ner_basic.yaml" 
# python NER_review.py -c "/home/ehsu/David_projects/LLM-IE_benchmark/benchmarks/ADE medication 2018/configs/Meta-Llama-3.1-70B-Instruct_float16_ner_review.yaml" 
python NER_sentence.py -c "/home/ehsu/David_projects/LLM-IE_benchmark/benchmarks/ADE medication 2018/configs/Meta-Llama-3.3-70B-Instruct_float16_ner_sentence.yaml" 
# python NER_sentence_review.py -c "/home/ehsu/David_projects/LLM-IE_benchmark/benchmarks/ADE medication 2018/configs/Meta-Llama-3.1-70B-Instruct_float16_ner_sentence_addition.yaml" 
# python NER_sentence_review.py -c "/home/ehsu/David_projects/LLM-IE_benchmark/benchmarks/ADE medication 2018/configs/Meta-Llama-3.1-70B-Instruct_float16_ner_sentence_revision.yaml" 
# python NER_sentence_CoT.py -c "/home/ehsu/David_projects/LLM-IE_benchmark/benchmarks/ADE medication 2018/configs/Meta-Llama-3.1-70B-Instruct_float16_ner_sentence_CoT.yaml" 
# python NER_sentence_CoT.py -c "/home/ehsu/David_projects/LLM-IE_benchmark/benchmarks/ADE medication 2018/configs/Meta-Llama-3.1-70B-Instruct_float16_ner_sentence_0.3.4.yaml" 