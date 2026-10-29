velocidade = 60 #km/h
kmcarro = 1000

RADAR_1 = 60 #km/h
LOCAL_1 = 125
RAIO_RADAR = 1

if kmcarro >= (LOCAL_1 - RAIO_RADAR) and kmcarro <= (LOCAL_1 + RAIO_RADAR):
    if velocidade > RADAR_1:
        print("Você foi multado!")
    else:
        print("Você está no raio do radar, mas com velocidade menor")
elif velocidade > RADAR_1:
    print("Você está acima da velocidade, mas fora do radar")
else: 
    print("Você está fora do radar e abaixo da velocidade")