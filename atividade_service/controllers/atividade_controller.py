from flask import Blueprint, request, jsonify
from ..services.atividade_service import criar_atividade, atualizar_atividade, deletar_atividade

atividade_bp = Blueprint('atividade_bp', __name__)

@atividade_bp.route('/', methods=['POST'])
def criar():
    dados = request.get_json()
    atividade, mensagem = criar_atividade(dados)
    if atividade is None:
        return jsonify({'error': mensagem}), 400
    return jsonify(atividade), 201

@atividade_bp.route('/<int:id_atividade>/', methods=['PUT'])
def atualizar(id_atividade):
    dados = request.get_json()
    atividade, mensagem = atualizar_atividade(id_atividade, dados)
    if atividade is None:
        return jsonify({'error': mensagem}), 404
    return jsonify(atividade)

@atividade_bp.route('/<int:id_atividade>/', methods=['DELETE'])
def deletar(id_atividade):
    sucesso, mensagem = deletar_atividade(id_atividade)
    if not sucesso:
        return jsonify({'error': mensagem}), 404
    return '', 204