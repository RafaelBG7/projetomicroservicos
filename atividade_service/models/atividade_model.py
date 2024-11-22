class Atividade:
    def __init__(self, id_atividade, id_disciplina, enunciado, respostas):
        self.id_atividade = id_atividade
        self.id_disciplina = id_disciplina
        self.enunciado = enunciado
        self.respostas = respostas

    def to_dict(self):
        return {
            'id_atividade': self.id_atividade,
            'id_disciplina': self.id_disciplina,
            'enunciado': self.enunciado,
            'respostas': self.respostas
        }