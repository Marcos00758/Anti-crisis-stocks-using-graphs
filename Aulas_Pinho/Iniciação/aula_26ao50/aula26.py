#f-string
variavel = "abcd"
print(f"{variavel}")
print(f"{variavel:O>10}") # adiciona o escolhido na esquerda até completar 10 dígitos 
print(f"{variavel:O<10}") # adiciona na direita
print(f"{variavel:O^10}") # adiciona em ambos os lados (mais na direita)
print(f"{15000:,.3f}") #o , adiciona , a cada 3 algarismos

print(f"Hexadecimal de 1000 é {1000:08x}")
print(f"Hexadecimal de 1000 é {1000:08X}")