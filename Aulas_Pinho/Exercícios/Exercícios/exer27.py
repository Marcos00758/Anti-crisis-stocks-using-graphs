#contar quantas vezes aparece cada ingrediente
ingredientes = [
    "lavanda", "baunilha", "sândalo", "jasmim", "bergamota", "rosa", "patchouli", 
    "lavanda", "âmbar", "almíscar", "vetiver", "baunilha", "cedro", "neroli", 
    "ylang-ylang", "cardamomo", "sândalo", "pimenta rosa", "lavanda", "bergamota",
    "rosa", "jasmim", "patchouli", "baunilha", "âmbar", "cedro", "vetiver", 
    "lavanda", "sândalo", "neroli", "almíscar", "bergamota", "rosa", "pimenta rosa",
    "baunilha", "jasmim", "patchouli", "lavanda", "âmbar", "vetiver", "cedro",
    "sândalo", "bergamota", "rosa", "neroli", "baunilha", "jasmim", "lavanda",
    "patchouli", "âmbar", "almíscar", "cedro", "vetiver", "sândalo", "bergamota",
    "pimenta rosa", "cardamomo", "ylang-ylang", "rosa", "baunilha", "lavanda",
    "jasmim", "patchouli", "âmbar", "cedro", "vetiver", "sândalo", "bergamota",
    "almíscar", "neroli", "rosa", "baunilha", "lavanda", "jasmim", "patchouli",
    "cardamomo", "âmbar", "vetiver", "cedro", "sândalo", "bergamota", "rosa",
    "lavanda", "baunilha", "jasmim", "patchouli", "almíscar", "neroli", "ylang-ylang"
]

def conta_elementos(lista):
    dicionario = {}
    
    # for item in set(lista):

    for item in lista:
        if item in dicionario:
            continue
        contador = lista.count(item)
        dicionario[item.title()] = contador
    
    return dicionario

print(conta_elementos(ingredientes))

            
        
                
            
        