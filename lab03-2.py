import random
import string

def generuj_haslo(length):
    znaki_ascii = string.ascii_letters + string.digits + string.punctuation
    haslo = ""
    haslo += random.choice(string.ascii_uppercase)
    haslo += random.choice(string.ascii_lowercase)
    haslo += random.choice(string.digits)
    haslo += random.choice(string.punctuation)
    for i in range(length - 4):
        haslo += random.choice(znaki_ascii)
    haslo = ''.join(random.sample(haslo, len(haslo)))
    return haslo

haslo = generuj_haslo(8)
print(haslo)