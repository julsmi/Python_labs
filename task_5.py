import random
import string


def get_random_password(n: int = 8) -> str:
    letters = list(string.ascii_uppercase) + list(string.ascii_lowercase) + list(string.digits)
    password = ''.join(random.sample(letters, n))
    return password


print(get_random_password())
