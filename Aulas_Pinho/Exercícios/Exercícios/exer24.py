#aproximação de limites

def aproximação_limite(x):

    if x <= -4:
        return "O x deve ser maior que -4"

    limite = (x+4)**(1/2)/2*x

    aproximacao_direita = []
    aproximaçao_esquerda = []
    
    for i in range(1,5):
        x += 1/10**(i)

        aproximacao_direita.append(round(((x+4)**(1/2)/2*x),3))

        x -= 2/10**(i)
        aproximaçao_esquerda.append(round(((x+4)**(1/2)/2*x),3))

        x += 1/10**(i)

    if round(aproximacao_direita[-1]) == round(aproximaçao_esquerda[-1]):
        return f"O limite da função existe e é {aproximacao_direita[-1]}"
    
    else:
        return f"O limite não existe porque os limites laterais são diferentes"



print(aproximação_limite(-4))



        


    
    
    
