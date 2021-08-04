from flask_restful import Resource
from flask import request
import json

listaHabilidades = ['Python', 'Flask', 'Django', 'PHP', 'Laravel', 'MySQL', 'PostgreSQL']

#Consulta as habilidades disponíveis e insere novas, validando se já existem.
class Habilidades(Resource):
    def get(self):
        return listaHabilidades

    def post(self):
        dados = json.loads(request.data)
        if dados in listaHabilidades:
            mensagem = 'Registro já existe'
            response = {'status':'erro', 'mensagem':mensagem}
        else:
            listaHabilidades.append(dados)
            mensagem = 'Registro inserido'
            response = {'status':'sucesso', 'mensagem':mensagem}
        return response

#Altera e deleta habilidades a partir de um id, validando se já existem.
class posicaoHabilidades(Resource):
    def put(self, id):
        try:
            dados = json.loads(request.data)
            if dados in listaHabilidades:
                mensagem = 'Registro já existe'
                response = {'status':'erro', 'mensagem':mensagem}
            else:
                listaHabilidades[id] = dados
                mensagem = 'Registro alterado'
                response = {'status':'sucesso', 'mensagem':mensagem}
        except IndexError:
            mensagem = 'Habilidade de id {} não existe.'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'erro', 'mensagem':mensagem}
        return response

    def delete(self, id):
        try:
            listaHabilidades.pop(id)
            mensagem = 'Registro excluído'
            response = {'status':'sucesso', 'mensagem':mensagem}
        except IndexError:
            mensagem = 'Habilidade de id {} não existe.'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'erro', 'mensagem':mensagem}
        return response