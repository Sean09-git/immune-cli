import json
import sys
from pathlib import Path

DATA = Path(__file__).parent / "immuno_terms.json"


def load_terms():
    with open(DATA) as f:
        return json.load(f)


def search(terms, query):
    q = query.lower()
    return [t for t in terms if q in t["name"].lower()]


def display(term):
    print(f"\nName      : {term['name']}")
    print(f"Korean    : {term['korean']}")
    print(f"French    : {term['french']}")
    print(f"Category  : {term['category']}")
    print(f"Definition: {term['definition_en']}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <term>")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    terms = load_terms()
    matches = search(terms, query)

    if not matches:
        print(f"No match for '{query}'.")
        sys.exit(1)

    for match in matches:
        display(match)

    if len(matches) > 1:
        print(f"\n({len(matches)} matches for '{query}')")


if __name__ == "__main__":
    main()
