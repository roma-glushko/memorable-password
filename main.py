import argparse
import random


def load_word_db() -> dict[int, str]:
    words: dict[int, str] = {}

    for line in open("./data/wordlist.txt"):
        if line.startswith("#"):
            continue

        index: str
        word: str
        index, word = line.split("	")

        words[int(index)] = word.strip()

    return words


def get_word_index() -> int:
    index: int = 0

    for idx in range(5):
        rand_num: int = random.randint(1, 6)
        index += rand_num * 10 ** idx

    return index


def generate(num_words: int = 4, num_passwords: int = 5, separator: str = "-") -> None:
    word_db = load_word_db()

    print("🔐 Your Password(s):")

    for _ in range(num_passwords):
        words: list[str] = []

        for _ in range(num_words):
            words.append(word_db.get(get_word_index()))

        password: str = separator.join(words)

        print(f"- {password}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a memorable password for you 🔐')
    parser.add_argument('-n', metavar='N', type=int, help='number of words')
    args = parser.parse_args()

    generate()

