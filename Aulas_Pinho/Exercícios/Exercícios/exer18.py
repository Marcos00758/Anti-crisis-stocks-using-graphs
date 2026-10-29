
"""Exemplo:

>>> letras = ["e", "s", "q", "u", "e", "c", "e", "r", "a", "m", "/", "d", "e", "/", "m", "i", "m"]
>>> converter_lista_para_string(letras)
'Esqueceram de Mim'"""

letras = ["e", "s", "q", "u", "e", "c", "e", "r", "a", "m", "/", "d", "e", "/", "m", "i", "m"]
print(letras)
vazio = ""

for letra in letras:
    if letra == "/":
        vazio += " "
    else:
        vazio += letra

print(vazio.title())