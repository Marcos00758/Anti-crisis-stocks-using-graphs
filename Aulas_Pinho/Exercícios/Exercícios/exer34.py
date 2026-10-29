#criptografia de césar
# 0 1 2 3 

def criptografia(chave, mensagem):
    mensagem_criptografada = ''
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for letra in mensagem.lower():
        if letra == " ":
            mensagem_criptografada += " "
            continue
        for indice in range(len(alfabeto)):

            if letra == alfabeto[indice]:

                if indice + chave >= 26:
                    novo_indice = indice + (chave%26) - 26
                    mensagem_criptografada += alfabeto[novo_indice]
                else:
                    mensagem_criptografada += alfabeto[indice + chave]
                    
            continue

    return mensagem_criptografada.title()

print(criptografia(1, "z"))
    
                

        
