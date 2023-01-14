import random
import string

def generuj_haslo(dlugoscmin = 8, dlugoscmax = 128):
    znaki_ascii = string.ascii_letters + string.digits + string.punctuation
    haslo = ""
    haslo += random.choice(string.ascii_uppercase)
    haslo += random.choice(string.ascii_lowercase)
    haslo += random.choice(string.digits)
    haslo += random.choice(string.punctuation)
    dlugosc_hasla = random.randint(dlugoscmin, dlugoscmax)
    for i in range(dlugosc_hasla):
        haslo += random.choice(znaki_ascii)
    haslo = ''.join(random.sample(haslo, len(haslo)))
    return haslo

haslo = generuj_haslo()
print(haslo)