import re


def get_password_strength(password):
    # calculating the length
    length_rate = int(len(password) >= 8) * 2

    # searching for digits
    digit_rate = int(re.search(r"\d", password) is not None) * 2

    # searching for uppercase
    uppercase_rate = int(re.search(r"[A-Z]", password) is not None) * 2

    # searching for lowercase
    lowercase_rate = int(re.search(r"[a-z]", password) is not None) * 2

    # searching for symbols
    symbol_rate = int(
        re.search(
            r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password
        ) is not None
    ) * 2

    # overall result
    return (
        sum([length_rate, digit_rate, uppercase_rate, lowercase_rate,
             symbol_rate])
    )


if __name__ == '__main__':
    password = input("Enter your password: ")
    print("Password strength: {}/10".format(get_password_strength(password)))
