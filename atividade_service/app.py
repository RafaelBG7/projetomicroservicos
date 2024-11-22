import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import create_app
from atividade_service.controllers.atividade_controller import atividade_bp

app = create_app()
app.register_blueprint(atividade_bp, url_prefix='/atividades')

if __name__ == '__main__':
    app.run(host='localhost', port=5002)