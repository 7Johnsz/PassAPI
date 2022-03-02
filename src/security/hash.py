import random
import string

# This file is a hash generator


lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

def generate():
    hash = lower + upper + digits + punctuation

    length = 60

    hash = "".join(random.sample(hash, length))

    return hash
