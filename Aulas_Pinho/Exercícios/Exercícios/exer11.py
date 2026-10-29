"""2. Contador de vogais e consoantes
- Peça uma frase ao usuário.
- Conte quantas vogais e quantas consoantes existem.
- Ignore espaços, números e pontuação.
- Mostre o resultado formatado com f-strings."""

frase = input("Digite uma frase e contarei o número de consoantes e vogais: ").lower()

vogal_a = frase.count("a")
vogal_e = frase.count("e")
vogal_i = frase.count("i")
vogal_o = frase.count("o")
vogal_u = frase.count("u")
vogais_frase = vogal_a + vogal_e + vogal_i + vogal_o + vogal_u
print(f"Há {vogais_frase} vogais na frase")

espaços_vazios = frase.count(" ")

consoantes_frase = (len(frase) - espaços_vazios - vogais_frase)
print(f"Há {consoantes_frase} consoantes na frase")