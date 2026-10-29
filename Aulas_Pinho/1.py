import copy

def filtrar_candidatos(competencias_vaga: set, competencias_candidato: dict = {str, tuple}) -> dict:
    if not isinstance(competencias_vaga, set):
        raise ValueError("As competências da vaga não estão em set")
    
    for nomes, competencias in competencias_candidato.items():
        if not isinstance(competencias, tuple):
            raise ValueError("Há competências de candidatos que não estão no padrão (em tupla)")
        
        for competencia in competencias:
            if competencia == "":
                raise ValueError
            if isinstance(competencia, str) == False:
                raise ValueError

    resultado = {}

    for nome, competencias in competencias_candidato.items():
        competencias_faltantes = copy.deepcopy(competencias_vaga)
        for competencia in competencias:
            if competencia in competencias_faltantes:
                competencias_faltantes.remove(competencia)
            
        if len(competencias_faltantes) == 0:
            resultado[nome] = (True,set())
        else:
            resultado[nome] = (False, competencias_faltantes)
    
    
    return resultado


vaga = {"Python", "SQL", "Git"}
    
banco_talentos = {
    "ana": ("Python", "SQL", "Git", "Docker"),
    "bruno": ("Python", "Git"),
    "carla": ("Java", "SQL")
}

resultado = filtrar_candidatos(vaga, banco_talentos)
print(resultado)

            