import fire
import sys
import json
import os

from oop_evaluate.data import OOP_EVAL
from oop_evaluate.evaluation import evaluate_functional_correctness

def save_json(data, file):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f'Saved to {file}.')
    return

def entry_point(
    sample_file: str,
    k: str = "1,2",
    n_workers: int = 4,
    timeout: float = 3.0,
    problem_file: str = OOP_EVAL,
):
    """
    Evaluates the functional correctness of generated samples, and writes
    results to f"{sample_file}_results.jsonl.gz"
    """
    k = list(map(int, k.split(",")))
    results = evaluate_functional_correctness(sample_file, k, n_workers, timeout, problem_file)
    code_result = dict({"OOP": results})
    print(sample_file)
    file_path = os.path.join(sample_file.split('/result')[0], 'OOP_result.json')
    save_json(code_result,file_path)
    
    print("results is", results)

def main():
    fire.Fire(entry_point)

sys.exit(main())
