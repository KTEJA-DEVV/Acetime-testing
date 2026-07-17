import random
import string


def mailgenerator(k=5):
    chars = string.ascii_letters
    mail=''.join(random.choices(chars ,k=k))
    email=mail+'@gmail.com'
    return email

def passgenerator(k=8):
    chars = string.ascii_letters +string.digits
    password=''.join(random.choices(chars, k=k))
    return password

def namegenerator(k=5):
    chars = string.ascii_letters
    name="".join(random.choices(chars,k=k))+''.join(random.choices(chars,k=k))
    return name


