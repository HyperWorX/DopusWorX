"""A small sample so you can see the code view: syntax highlighting,
line gutter, word-wrap toggle, and the copy button in the corner."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Document:
    path: str
    words: int

    @property
    def is_long(self) -> bool:
        return self.words > 1_000


def total_words(docs: Iterable[Document]) -> int:
    """Sum the word counts across a set of documents."""
    return sum(d.words for d in docs)


def main() -> None:
    docs = [
        Document("welcome.md", 320),
        Document("math.md", 140),
        Document("report.md", 4_200),
    ]
    long_docs = [d.path for d in docs if d.is_long]

    print(f"{len(docs)} documents, {total_words(docs):,} words total")
    print("Long documents:", ", ".join(long_docs) or "none")


if __name__ == "__main__":
    main()
