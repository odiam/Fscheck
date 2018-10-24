from random import randint
from hashlib import blake2b

def random_salt(length):
    '''Generates a random salt for hashes. No sense.'''
    res = ""
    for x in range(length):
        if randint(0, 2):
            res += randint(63, 63+26)
        else:
            res += randint(48, 48+10)
    return res.encode("utf-8")

def blake2_hash(content):
    key = b"oewqbfjerrrtftbjhgeklrjgblqwerbhl"
    SIZE = 64
    return blake2b(content, digest_size=SIZE, key=key).hexdigest().encode("utf-8")

# funzioen per debug
def base_hash(text):
    return text