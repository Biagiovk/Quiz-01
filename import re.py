import re

def validar_senha(s):
    if not (6 <= len(s) <= 32):
        return "Senha invalida."
    if not re.search("[A-Z]", s):
        return "Senha invalida."
    if not re.search("[a-z]", s):
        return "Senha invalida."
    if not re.search("[0-9]", s):
        return "Senha invalida."
    if re.search("[^a-zA-Z0-9]", s):
        return "Senha invalida."
    return "Senha valida."

while True:
    try:
        senha = input()
        print(validar_senha(senha))
    except EOFError:
        break
