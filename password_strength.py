import re


def get_password_strength(password):
    length_score = 1
    digit_score = 2
    uppercase_score = 2
    lowercase_score = 2
    symbol_score = 2
    min_score = 1

    # calculating the length
    length_rate = int(len(password) >= 8) * length_score

    # searching for digits
    digit_rate = int(re.search(r"\d", password) is not None) * digit_score

    # searching for uppercase
    uppercase_rate = int(
        re.search(r"[A-Z]", password) is not None
    ) * uppercase_score

    # searching for lowercase
    lowercase_rate = int(
        re.search(r"[a-z]", password) is not None
    ) * lowercase_score

    # searching for symbols
    symbol_rate = int(
        re.search(
            r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password
        ) is not None
    ) * symbol_score

    # overall result
    return sum([length_rate, digit_rate, uppercase_rate, lowercase_rate,
                symbol_rate]) + min_score



if __name__ == '__main__':
    password = input("Enter your password: ")
    print("Password strength: {}/10".format(get_password_strength(password)))
