# if (se) / começa sempre com if e só pode haver 1 if
# elif (se não se) / se a condição do if não for satisfeita, usa-se elif
# else (se não) / se nenhuma das condições acima for satisfeita, vai a do else
#else é sempre a última condição

entrada = input("Você quer sair ou entrar? ")

if entrada == "sair":
    print('Você saiu do sistema')
elif entrada == "entrar":
    print("Você entrou no sistema")
else:
    print("Erro")