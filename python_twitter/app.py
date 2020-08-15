from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import os
import twitter_dados
import analys
import json
import pprint
app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/devs', methods=['POST'])
@cross_origin(supports_credentials=True)
def dev():
  
  busca = request.json['valor']
  valor = twitter_dados.buscar_dados(busca)
  dados_limpo = twitter_dados.limpar_dados(valor)
  result = analys.analise(dados_limpo)
  
  
  dados = {'data': result, 'text': dados_limpo}
  data = [dados]
  return jsonify(data)
  
  

if __name__=="__main__":
  port = int(os.environ.get("PORT", 8000))
  app.run(host='0.0.0.0', port=port, debug=True)


