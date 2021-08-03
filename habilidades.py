from flask_restful import Resource

listaHabilidades = ['Python', 'Flask', 'Django', 'PHP', 'Laravel', 'MySQL', 'PostgreSQL']

#Consulta as habilidades disponíveis
class Habilidades(Resource):
    def get(self):
        return listaHabilidades