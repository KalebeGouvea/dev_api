from flask import Flask, jsonify, request
import json

app = Flask(__name__)

#Lista de desenvolvedores pré existentes na API
desenvolvedores = [
    {
        'nome':'Kalebe',
        'habilidade':['Python', 'Flask']
    },
    {
        'nome':'Gouvea',
        'habilidades':['Python', 'Django']
    }
]

#Consulta, altera e deleta desenvolvedores pelo ID
@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de id {} não existe'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'erro', 'mensagem':mensagem}
        return jsonify(response)   
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'Registro excluído'})

#Insere novos desenvolvedores e consulta todos os desenvolvedores da API
@app.route('/dev', methods=['POST', 'GET'])
def listaDesenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status':'sucesso', 'mensagem':'Registro inserido'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)