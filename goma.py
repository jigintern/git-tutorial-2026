import random
import time

AA_CHARACTERS = [
    {
        "name": "もちすみ",
        "aa": r"""
       ､ゝ
    ＿ﾉ  `ｰ､
   /  ･  ･  ヽ
  │    ᵕ    │
  │  つ⌒と  │
   \  (___)  /
    `ｰ┬─┬ｰ´
      し し
""",
        "message": "もちすみは、たぶん今日も元気です。"
    },
    {
        "name": "ぽゆ",
        "aa": r"""
        __
     .´    `.
    /  ◜  ◝  \
   |     ˘     |
   |  づ  づ  |
    \   ︶   /
     `､___,´
       | |
      ﾉ  ヽ
""",
        "message": "ぽゆは何もしていません。えらい。"
    },
    {
        "name": "ぬ",
        "aa": r"""
          へ
      ＿/  `､＿
    /            \
   |   ◉      ◉   |
   |       ᴗ       |
   |    /つ つ\    |
    \  /     \   /
     `ｰ､_____,ｰ´
        ∪   ∪
""",
        "message": "ぬ。"
    }
]


def summon_aa():
    character = random.choice(AA_CHARACTERS)

    print("AAキャラ召喚中", end="", flush=True)
    for _ in range(3):
        time.sleep(0.35)
        print(".", end="", flush=True)

    print("\n")
    print(character["aa"])
    print(f"[{character['name']}] {character['message']}")


if __name__ == "__main__":
    summon_aa()