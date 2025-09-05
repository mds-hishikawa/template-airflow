import sys
import os
# Adiciona o diretório 'src' ao path para que os imports funcionem
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app', 'src')))

from utils.helpers import get_project_name

def test_get_project_name():
    assert get_project_name() == "Meu Projeto Airflow"