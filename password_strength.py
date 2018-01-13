import re
from getpass import getpass
from string import punctuation


def get_password_strength(password):
    length_score = 1
    digit_score = 2
    uppercase_score = 2
    lowercase_score = 2
    symbol_score = 2
    min_score = 1

    password_min_length = 8

    length_rate = (len(password) >= password_min_length) * length_score

    digit_rate = bool(re.search(r"\d", password)) * digit_score

    uppercase_rate = bool(re.search(r"[A-Z]", password)) * uppercase_score

    lowercase_rate = bool(re.search(r"[a-z]", password)) * lowercase_score

    symbol_rate = bool(
        re.search(r"[{}]".format(punctuation), password)
    ) * symbol_score

    return sum(
        [
            length_rate,
            digit_rate,
            uppercase_rate,
            lowercase_rate,
            symbol_rate
        ]
    ) + min_score


if __name__ == "__main__":
    password = getpass()
    print("Password strength: {}/10".format(get_password_strength(password)))
