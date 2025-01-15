# Object-Oriented Programming Evaluation Benchmark for LLMs.

## OOP Benchmark

OOP is a code generation benchmark to <b>quantify the object-oriented programming ability</b> of language Large Language Models (LLMs), and the details can be seen in our paper "[OOP: Object-Oriented Programming Evaluation Benchmark for Large Language Models](https://aclanthology.org/2024.findings-acl.808.pdf) | [[HuggingFace Link](https://huggingface.co/datasets/codeai-dteam/oop)]". 
We collect code snippets from the [LeetCode](https://leetcode.com/), [open-source repositories on GitHub](https://github.com/), [Stack Overflow](https://stackoverflow.com/), and [Codewars](https://www.codewars.com/), and all the test samples have undergone carefully designed post-processing. 

We show that 🔎:
- ⚠️ Despite excelling in functional programming (FP), e.g., HumanEval and MBPP, code-specialized LLMs like WizardCoder lag in our OOP compared to proprietary models like ChatGPT;
- 🚀 The poor performance of all advanced LLMs on our OOP benchmark highlights a critical need for improvements in this field.

📢 News: \[May 15, 2024\] OOP has been accepted by ACL 2024 Findings. 
### Basic Statistics
- OOP consists of 431 instances;
- OOP contains three difficulty levels:  Simple-level OOP, Moderate-level OOP, and Difficult-level OOP.

### Performance of widely-used LLMs
<div align="center">
    <img width="80%" alt="image" src="https://github.com/alphadl/OOP-eval/blob/main/img/results.jpg">
</div>

## Citations

Please cite the paper and star this repo if you use OOP and find it helpful.
Feel free to contact wangshuai123@whu.edu.cn or open an issue if you have any questions.

```ruby
@inproceedings{wang2024oop,
  title={OOP: Object-Oriented Programming Evaluation Benchmark for Large Language Models},
  author={Wang, Shuai and Ding, Liang and Shen, Li and Luo, Yong and Du, Bo and Tao, Dacheng},
  booktitle={Findings of the Association for Computational Linguistics: ACL 2024},
  year={2024}
}
```
