from flask import Blueprint, jsonify, request
from models import pessoa_model

pessoa_bp = Blueprint('pessoa_bp', __name__)

@pessoa_bp.route('/professores', methods=['GET'])
def listar_professores():
    professores = pessoa_model.listar_professores()
    return jsonify(professores)

@pessoa_bp.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = pessoa_model.listar_alunos()
    return jsonify(alunos)

@pessoa_bp.route('/disciplinas', methods=['GET'])
def listar_disciplinas():
    disciplinas = pessoa_model.listar_disciplinas()
    return jsonify(disciplinas)

@pessoa_bp.route('/leciona/<int:id_professor>/<int:id_disciplina>', methods=['GET'])
def verificar_leciona(id_professor, id_disciplina):
    try:
        leciona = pessoa_model.leciona(id_professor, id_disciplina)
        return jsonify({'leciona': leciona})
    except pessoa_model.DisciplinaNaoEncontrada:
        return jsonify({'erro': 'Disciplina não encontrada'}), 404

@pessoa_bp.route('/professores', methods=['POST'])
def criar_professor():
    dados = request.get_json()
    novo_professor = {
        'nome': dados['nome'],
        'id_professor': dados['id_professor']
    }
    pessoa_model.professores.append(novo_professor)
    return jsonify(novo_professor), 201

@pessoa_bp.route('/professores/<int:id_professor>', methods=['PUT'])
def atualizar_professor(id_professor):
    dados = request.get_json()
    professor = next((p for p in pessoa_model.professores if p['id_professor'] == id_professor), None)
    if professor is None:
        return jsonify({'erro': 'Professor não encontrado'}), 404
    professor['nome'] = dados['nome']
    return jsonify(professor)

@pessoa_bp.route('/professores/<int:id_professor>', methods=['DELETE'])
def deletar_professor(id_professor):
    global professores
    professor = next((p for p in pessoa_model.professores if p['id_professor'] == id_professor), None)
    if professor is None:
        return jsonify({'erro': 'Professor não encontrado'}), 404
    pessoa_model.professores = [p for p in pessoa_model.professores if p['id_professor'] != id_professor]
    return '', 204

@pessoa_bp.route('/alunos', methods=['POST'])
def criar_aluno():
    dados = request.get_json()
    novo_aluno = {
        'nome': dados['nome'],
        'id_aluno': dados['id_aluno']
    }
    pessoa_model.alunos.append(novo_aluno)
    return jsonify(novo_aluno), 201

@pessoa_bp.route('/alunos/<int:id_aluno>', methods=['PUT'])
def atualizar_aluno(id_aluno):
    dados = request.get_json()
    aluno = next((a for a in pessoa_model.alunos if a['id_aluno'] == id_aluno), None)
    if aluno is None:
        return jsonify({'erro': 'Aluno não encontrado'}), 404
    aluno['nome'] = dados['nome']
    return jsonify(aluno)

@pessoa_bp.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def deletar_aluno(id_aluno):
    global alunos
    aluno = next((a for a in pessoa_model.alunos if a['id_aluno'] == id_aluno), None)
    if aluno is None:
        return jsonify({'erro': 'Aluno não encontrado'}), 404
    pessoa_model.alunos = [a for a in pessoa_model.alunos if a['id_aluno'] != id_aluno]
    return '', 204

@pessoa_bp.route('/disciplinas', methods=['POST'])
def criar_disciplina():
    dados = request.get_json()
    nova_disciplina = {
        'nome': dados['nome'],
        'id_disciplina': dados['id_disciplina'],
        'alunos': dados.get('alunos', []),
        'professores': dados.get('professores', []),
        'publica': dados.get('publica', False)
    }
    pessoa_model.disciplinas.append(nova_disciplina)
    return jsonify(nova_disciplina), 201

@pessoa_bp.route('/disciplinas/<int:id_disciplina>', methods=['PUT'])
def atualizar_disciplina(id_disciplina):
    dados = request.get_json()
    disciplina = next((d for d in pessoa_model.disciplinas if d['id_disciplina'] == id_disciplina), None)
    if disciplina is None:
        return jsonify({'erro': 'Disciplina não encontrada'}), 404
    disciplina['nome'] = dados['nome']
    disciplina['alunos'] = dados.get('alunos', disciplina['alunos'])
    disciplina['professores'] = dados.get('professores', disciplina['professores'])
    disciplina['publica'] = dados.get('publica', disciplina['publica'])
    return jsonify(disciplina)

@pessoa_bp.route('/disciplinas/<int:id_disciplina>', methods=['DELETE'])
def deletar_disciplina(id_disciplina):
    global disciplinas
    disciplina = next((d for d in pessoa_model.disciplinas if d['id_disciplina'] == id_disciplina), None)
    if disciplina is None:
        return jsonify({'erro': 'Disciplina não encontrada'}), 404
    pessoa_model.disciplinas = [d for d in pessoa_model.disciplinas if d['id_disciplina'] != id_disciplina]
    return '', 204