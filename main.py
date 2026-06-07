import argparse
import difflib
import json
import random
import sys
from pathlib import Path

DATA = Path(__file__).parent / "immuno_terms.json"

PROMPTS = {
    "en": {
        "question": "Definition: {definition}\nYour answer: ",
        "correct":  "Correct!",
        "wrong":    "Wrong — answer: {en}  ({ko} / {fr})",
        "score":    "Score: {score}/10",
        "missed":   "Missed:",
    },
    "ko": {
        "question": "정의: {definition}\n답: ",
        "correct":  "정답!",
        "wrong":    "오답 — 정답: {en}  ({ko} / {fr})",
        "score":    "점수: {score}/10",
        "missed":   "틀린 문제:",
    },
    "fr": {
        "question": "Définition : {definition}\nVotre réponse : ",
        "correct":  "Correct !",
        "wrong":    "Faux — réponse : {en}  ({ko} / {fr})",
        "score":    "Score : {score}/10",
        "missed":   "Manqués :",
    },
}


def load_terms():
    with open(DATA) as f:
        return json.load(f)


def normalize(s):
    return s.lower().replace("-", "").replace(" ", "")


def search(terms, query):
    q = query.lower()
    qn = normalize(query)
    return [t for t in terms if q in t["name"].lower() or qn in normalize(t["name"])]


def suggest(terms, query):
    names = [t["name"] for t in terms]
    return difflib.get_close_matches(query, names, n=3, cutoff=0.4)


def display(term):
    print(f"\nName      : {term['name']}")
    print(f"Korean    : {term['korean']}")
    print(f"French    : {term['french']}")
    print(f"Category  : {term['category']}")
    print(f"Definition: {term['definition_en']}")


def is_correct(answer, term):
    a = answer.strip().lower()
    return a in (term["name"].lower(), term["korean"].lower(), term["french"].lower())


def quiz(terms, lang):
    p = PROMPTS[lang]
    sample = random.sample(terms, min(10, len(terms)))
    score, wrong = 0, []

    for i, term in enumerate(sample, 1):
        print(f"\n[{i}/10]")
        answer = input(p["question"].format(definition=term["definition_en"]))
        if is_correct(answer, term):
            print(p["correct"])
            score += 1
        else:
            print(p["wrong"].format(en=term["name"], ko=term["korean"], fr=term["french"]))
            wrong.append(term)

    print(f"\n{p['score'].format(score=score)}")
    if wrong:
        print(p["missed"])
        for t in wrong:
            print(f"  · {t['name']}  ({t['korean']} / {t['french']})")


def main():
    parser = argparse.ArgumentParser(prog="main.py")
    parser.add_argument("term", nargs="*", help="Term to look up")
    parser.add_argument("--quiz", action="store_true")
    parser.add_argument("--lang", choices=["en", "ko", "fr"], default="en")
    args = parser.parse_args()
    terms = load_terms()

    if args.quiz:
        quiz(terms, args.lang)
        return

    if not args.term:
        parser.print_help()
        sys.exit(1)

    query = " ".join(args.term)
    matches = search(terms, query)

    if not matches:
        suggestions = suggest(terms, query)
        if suggestions:
            print(f"No match for '{query}'. Did you mean: {', '.join(suggestions)}?")
        else:
            print(f"No match for '{query}'.")
        sys.exit(1)

    for match in matches:
        display(match)

    if len(matches) > 1:
        print(f"\n({len(matches)} matches for '{query}')")


if __name__ == "__main__":
    main()
