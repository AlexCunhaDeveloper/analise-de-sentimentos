import twitter_dados
import analys
import pprint
import json
print('---------- buscando dados ---------------')
valor = twitter_dados.buscar_dados('Vue')

print('------------------ limpando dados -----------------')
dados_limpo = twitter_dados.limpar_dados(valor)

print('----------- analisando dados -------------------')
result = analys.analise(dados_limpo)

result.append(dados_limpo)
pprint.pprint(result)
