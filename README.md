# Object-Oriented Programming Evaluation Benchmark for LLMs.

## OOP Benchmark

OOP is a code generation benchmark to <b>quantify the object-oriented programming ability</b> of language Large Language Models (LLMs), and the details can be seen in our paper "[OOP: Object-Oriented Programming Evaluation Benchmark for Large Language Models](https://arxiv.org/abs/2401.06628)". 
We collect code snippets from the [LeetCode](https://leetcode.com/), [open-source repositories on GitHub](https://github.com/), [Stack Overflow](https://stackoverflow.com/), and [Codewars](https://www.codewars.com/), and all the test samples have undergone carefully designed post-processing. 

We show that 🔎:
- ⚠️ Despite excelling in functional programming (FP), e.g., HumanEval and MBPP, code-specialized LLMs like WizardCoder lag in our OOP compared to proprietary models like ChatGPT;
- 🚀 The poor performance of all advanced LLMs on our OOP benchmark highlights a critical need for improvements in this field.

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
@article{wang2024oop,
  title={OOP: Object-Oriented Programming Evaluation Benchmark for Large Language Models},
  author={Wang, Shuai and Ding, Liang and Shen, Li and Luo, Yong and Du, Bo and Tao, Dacheng},
  journal={arXiv preprint arXiv:2401.06628},
  year={2024}
}
```
