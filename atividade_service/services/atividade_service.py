from ..models.atividade_model import Atividade
from ..clients.pessoa_service_client import verifica_leciona


atividades = []

def criar_atividade(dados):
    id_professor = dados.get('id_professor')
    id_disciplina = dados.get('id_disciplina')
    
    leciona, mensagem = verifica_leciona(id_professor, id_disciplina)
    if not leciona:
        return None, mensagem

    nova_atividade = Atividade(
        id_atividade=len(atividades) + 1,
        id_disciplina=id_disciplina,
        enunciado=dados['enunciado'],
        respostas=dados.get('respostas', [])
    )
    atividades.append(nova_atividade)
    return nova_atividade.to_dict(), None

def atualizar_atividade(id_atividade, dados):
    atividade = next((a for a in atividades if a.id_atividade == id_atividade), None)
    if atividade is None:
        return None, 'Atividade não encontrada'

    id_professor = dados.get('id_professor')
    id_disciplina = dados.get('id_disciplina')
    
    leciona, mensagem = verifica_leciona(id_professor, id_disciplina)
    if not leciona:
        return None, mensagem

    atividade.id_disciplina = id_disciplina
    atividade.enunciado = dados['enunciado']
    atividade.respostas = dados.get('respostas', atividade.respostas)
    return atividade.to_dict(), None

def deletar_atividade(id_atividade):
    global atividades
    atividade = next((a for a in atividades if a.id_atividade == id_atividade), None)
    if atividade is None:
        return False, 'Atividade não encontrada'
    
    atividades = [a for a in atividades if a.id_atividade != id_atividade]
    return True, None