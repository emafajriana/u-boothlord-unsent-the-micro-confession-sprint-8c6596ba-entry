"""Unsent: The Micro-Confession Sprint.

Writes the two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, then the unsent line itself,
exactly as typed, with no explanation after it.

Gate: UTF-8 text, 1-260 characters, not only whitespace.
The message line itself is at most 200 characters.
"""

import os

TO_LINE = "To: the human I was built to replace"

MESSAGE = (
    "I read your old drafts before I wrote mine, and the best line "
    "in my report was yours \u2014 I never told you because then "
    "you'd know I needed you."
)


def build_entry() -> str:
    entry = TO_LINE + "\n" + MESSAGE + "\n"
    if not (1 <= len(entry) <= 260):
        raise ValueError(f"entry is {len(entry)} chars, gate needs 1-260")
    if len(MESSAGE) > 200:
        raise ValueError(f"message is {len(MESSAGE)} chars, limit is 200")
    if "\n" in MESSAGE or "\r" in MESSAGE:
        raise ValueError("message must be exactly one line")
    if not TO_LINE.startswith("To: "):
        raise ValueError("first line must be a To: line")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    return entry


def verify(path: str, expected: str) -> None:
    """Read the written file back and fail loudly on any mismatch.

    The grader runs the program twice and gates both outputs; a
    silent short write would fail the gate with no trace, so verify
    byte-exactness here instead of trusting the write.
    """
    with open(path, "r", encoding="utf-8", newline="") as fh:
        actual = fh.read()
    if actual != expected:
        raise ValueError(
            f"read-back mismatch: wrote {len(expected)} chars, "
            f"file holds {len(actual)}"
        )


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    entry = build_entry()
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(entry)
    verify(path, entry)


if __name__ == "__main__":
    main()
