'''
CONSTANTE = são 'váriaveis' fixas // que não vão mudar, são escritas toda em maisculo.
Por exemplo a velocidade e o local do carro muda, mas a velocidade maxima do radar
e onde ele esta não muda!, ESSAS.

Identificando um código ruim:
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
    quanto mais longe de margem o código estar, mais complexo ou "ruim de ler" ele é
'''

velocidade = 50 # velocidade atual do carro
local_carro = 150 # km/local que o carro esta

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_RADAR_1 = 100 # km/local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

velocpassouradar1 = velocidade > RADAR_1

carromultadoradar1 = local_carro >= (LOCAL_RADAR_1-RADAR_RANGE) and \
    local_carro <= (LOCAL_RADAR_1+RADAR_RANGE) and velocpassouradar1

carroudentrovelocradar1 = local_carro >= (LOCAL_RADAR_1-RADAR_RANGE) and \
    local_carro <= (LOCAL_RADAR_1+RADAR_RANGE) and (velocidade<RADAR_1)

carroforadoradar1 = (local_carro < LOCAL_RADAR_1-RADAR_RANGE) or \
      (local_carro > LOCAL_RADAR_1+RADAR_RANGE)

if velocpassouradar1:
    print(f'Passou da velocidade máxima ({RADAR_1}) no radar 1')

if carroudentrovelocradar1:
    print('O carro passou pelo radar 1 dentro da velocidade')

if carromultadoradar1:
    print('Carro multado em radar 1')

elif carroforadoradar1:
    print('O carro não passou pelo radar')
