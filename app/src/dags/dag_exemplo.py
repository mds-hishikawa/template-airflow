from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
import pendulum
from utils.helpers import get_project_name # Importando do nosso módulo

def print_project_name():
    print(f"O nome do projeto é: {get_project_name()}")

with DAG(
    dag_id='dag_principal_com_utils',
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
) as dag:
    PythonOperator(
        task_id='tarefa_imprime_nome',
        python_callable=print_project_name,
    )