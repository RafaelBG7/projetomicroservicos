import requests

def verifica_leciona(id_professor, id_disciplina):
    try:
        response = requests.get(f'http://localhost:5001/pessoas/leciona/{id_professor}/{id_disciplina}')
        response.raise_for_status()
        data = response.json()
        return data.get('leciona'), data.get('mensagem')
    except requests.exceptions.RequestException as e:
        return False, f'Erro na comunicação com pessoa_service: {e}'