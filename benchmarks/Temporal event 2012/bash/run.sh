cd /home/ehsu/David_projects/LLM-IE_benchmark/pipelines

# python NER_basic.py -c "/home/ehsu/David_projects/LLM-IE_benchmark/benchmarks/Temporal event 2012/configs/Meta-Llama-3.1-70B-Instruct_float16_ner_basic.yaml"
# python NER_review.py -c "/home/ehsu/David_projects/LLM-IE_benchmark/benchmarks/Temporal event 2012/configs/Meta-Llama-3.1-70B-Instruct_float16_ner_review.yaml"
# python NER_sentence.py -c "/home/ehsu/David_projects/LLM-IE_benchmark/benchmarks/Temporal event 2012/configs/Meta-Llama-3.1-70B-Instruct_float16_ner_sentence.yaml"
python NER_sentence.py -c "/home/ehsu/David_projects/LLM-IE_benchmark/benchmarks/Temporal event 2012/configs/Meta-Llama-3.3-70B-Instruct_float16_ner_sentence.yaml"