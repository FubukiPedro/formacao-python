"""
CONSTANTE = "Variáveis" que não vão mudar
para indicar uma constante escrevem em capslock!!!

Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim) 
    (quanto mais blocos de código dentro de outros blocos de código, mas complexo seu código é)
"""

velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

vel_car_passou_radar_1 = velocidade > RADAR_1
loc_car_passou_radar_1 = (local_carro >= LOCAL_1 - RADAR_RANGE) and (local_carro <= LOCAL_1 + RADAR_RANGE)
mul_car_passou_radar_1 = vel_car_passou_radar_1 and loc_car_passou_radar_1

if vel_car_passou_radar_1:
    print('Você está acima da velocidade permitida pelo radar 1')

if loc_car_passou_radar_1:
    print('Você passou pelo radar 1')

if mul_car_passou_radar_1:
    print('Você foi multado pelo radar 1')

if loc_car_passou_radar_1 and not mul_car_passou_radar_1:
    print('Você estava abaixo do limite de velocidade e não foi multado.')