import re


def get_password_strength(password):
    length_ball = 1
    digit_ball = 2
    uppercase_ball = 2
    lowercase_ball = 2
    symbol_ball = 2
    min_ball = 1

    # calculating the length
    length_rate = int(len(password) >= 8) * length_ball

    # searching for digits
    digit_rate = int(re.search(r"\d", password) is not None) * digit_ball

    # searching for uppercase
    uppercase_rate = int(
        re.search(r"[A-Z]", password) is not None
    ) * uppercase_ball

    # searching for lowercase
    lowercase_rate = int(
        re.search(r"[a-z]", password) is not None
    ) * lowercase_ball

    # searching for symbols
    symbol_rate = int(
        re.search(
            r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password
        ) is not None
    ) * symbol_ball

    # overall result
    return (
        sum([length_rate, digit_rate, uppercase_rate, lowercase_rate,
             symbol_rate]) + min_ball
    )


if __name__ == '__main__':
    password = input("Enter your password: ")
    print("Password strength: {}/10".format(get_password_strength(password)))
