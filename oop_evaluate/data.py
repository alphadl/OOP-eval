from typing import Iterable, Dict
import gzip
import json
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
OOP_EVAL = os.path.join(ROOT, "..", "data", "oop_data.jsonl.gz")


def read_problems(evalset_file: str = OOP_EVAL) -> Dict[str, Dict]:
    problem = []
    for id, task in enumerate(stream_jsonl(evalset_file)):
        test_assert = "\n\nMETADATA = {}\n\n\ndef check(candidate):"
        for test_example in task["test_list"]:
            test_assert = test_assert + "\n    " + test_example
        test_test = task["test_function"] + "\n" + test_assert + "\n"
        test_rule_assert = "\n\nMETADATA = {}\n\n\ndef check(candidate):"
        test_rule_assert = test_rule_assert + "\n    " + task["test_matching"]
        test_rulematch = task["test_match_function"] + "\n" + test_rule_assert + "\n"

        problem.append({"task_id": task["task_id"], "prompt": task["question"], "test": test_test, "test_rulematch": test_rulematch, "entry_point": task["entry_point"]})
    return {problem[number]["task_id"]: problem[number] for number in range(len(problem))}

def stream_jsonl(filename: str) -> Iterable[Dict]:
    """
    Parses each jsonl line and yields it as a dictionary
    """
    if filename.endswith(".gz"):
        with open(filename, "rb") as gzfp:
            with gzip.open(gzfp, 'rt') as fp:
                for line in fp:
                    if any(not x.isspace() for x in line):
                        yield json.loads(line)
    else:
        with open(filename, "r") as fp:
            for line in fp:
                if any(not x.isspace() for x in line):
                    yield json.loads(line)


def write_jsonl(filename: str, data: Iterable[Dict], append: bool = False):
    """
    Writes an iterable of dictionaries to jsonl
    """
    if append:
        mode = 'ab'
    else:
        mode = 'wb'
    filename = os.path.expanduser(filename)
    if filename.endswith(".gz"):
        with open(filename, mode) as fp:
            with gzip.GzipFile(fileobj=fp, mode='wb') as gzfp:
                for x in data:
                    gzfp.write((json.dumps(x) + "\n").encode('utf-8'))
    else:
        with open(filename, mode) as fp:
            for x in data:
                fp.write((json.dumps(x) + "\n").encode('utf-8'))
