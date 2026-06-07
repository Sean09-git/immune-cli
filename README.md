# immune-cli

A command-line study tool for immunology. Look up any of 50 terms across
8 categories — Innate, Adaptive, Cells, Molecules, Vaccines, Allergy,
Autoimmune, and Daily-life — with English, Korean, and French translations.
A built-in quiz picks 10 random terms, shows each definition, and accepts
a correct answer in any of the three languages.

## Installation

```bash
git clone https://github.com/Sean09-git/immune-cli.git
cd immune-cli
pip3 install colorama
```

## Usage

**Look up a term** (case-insensitive, partial match):
```
$ python3 main.py macrophage

Name      : Macrophage
Korean    : 대식세포
French    : Macrophage
Category  : Innate
Definition: A macrophage is a long-lived innate immune cell that eats
            pathogens, cleans debris, and signals the rest of the immune system.
```

**Quiz mode** — answers accepted in English, Korean, or French:
```
$ python3 main.py --quiz

[1/10]
Definition: A neutrophil is the most abundant white blood cell — a short-lived
innate phagocyte that arrives first at infection sites.
Your answer: neutrophil
✅ Correct!
...
Score: 8/10
```

**Quiz with Korean prompts:**
```
$ python3 main.py --quiz --lang ko

[1/10]
정의: 항체(면역글로불린)는 B 세포가 만드는 Y자형 단백질로, 특정 항원을 인식한다.
답: 항체
정답!
```

## About

immune-cli was built as part of a 12-week tutoring project for a teenager
studying immunology and Python together. Each term in the database started
as a biology lesson and became a coding exercise — from parsing JSON to
building a quiz engine. The 50-term library spans core immune concepts,
allergy, vaccines, and daily-life factors, with trilingual support added
so the same tool works for study in English, Korean, and French.
