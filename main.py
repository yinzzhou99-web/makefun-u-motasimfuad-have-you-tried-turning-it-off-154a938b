"""Have You Tried Turning It Off? -- one-line entry for make.fun.

Writes a single funny line from a hopeless tech support agent to a
desperate customer to /output/entry.txt. Standard library only, fully
deterministic: the same line every run.
"""

import os

LINE = (
    "Good news, I found the fault: your laptop is exhausted too. "
    "Turn it off, turn it on, and maybe apologise while you're at it."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
