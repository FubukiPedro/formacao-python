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

vel_carro_pass_radar_1 = velocidade > RADAR_1 # se essa bool for True, significa que o carro está acima da velocidade permitida.


if vel_carro_pass_radar_1:
    print(f'Velocidade carro passou do radar 1: {velocidade}')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE):
    print('Você foi multado em radar 1')