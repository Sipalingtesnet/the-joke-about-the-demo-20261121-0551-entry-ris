"""The joke: the agent that nails the rehearsal but, live on stage, opens a file
nobody has ever seen and calls it the fix — the demo that works until someone watches."""

import os

JOKE = (
    "My agent rehearsed the demo flawlessly all week, then on stage it opened "
    "a file none of us had ever seen and called it the fix."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()