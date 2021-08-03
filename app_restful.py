from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json

app = Flask(__name__)
api = Api(app)

#Lista de desenvolvedores pré existentes na API
desenvolvedores = [
    {   'id':'0',
        'nome':'Kalebe',
        'habilidade':['Python', 'Flask']
    },
    {
        'id':'1',
        'nome':'Gouvea',
        'habilidades':['Python', 'Django']
    }
]

#Consulta, altera e deleta desenvolvedores pelo ID
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de id {} não existe'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'erro', 'mensagem':mensagem}
        return response
        
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status':'sucesso', 'mensagem':'Registro excluído'}

#Insere novos desenvolvedores e consulta todos os desenvolvedores da API
class listaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return {'status':'sucesso', 'mensagem':'Registro inserido'}

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(listaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')


if __name__ == '__main__':
    app.run(debug=True)