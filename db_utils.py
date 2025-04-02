import os
import psycopg2
from dotenv import load_dotenv, set_key

def test_db_connection(db_name, user, password, host='localhost', port='5432'):

    try:
        connection = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        return True
    except Exception as e:
        print(f'Error de conexión: {e}')
        return False


def create_env_file(file_name, db_name, user, password, host='localhost', port='5432'):
    if not os.path.exists('config'):
        os.makedirs('config')

    env_file_path = os.path.join('config', f'{file_name}.env')

    if not os.path.isfile(env_file_path):
        with open(env_file_path, 'w') as env_file:
            env_file.write(f'DB_NAME={db_name}\n')
            env_file.write(f'DB_USER={user}\n')
            env_file.write(f'DB_PASSWORD={password}\n')
            env_file.write(f'DB_HOST={host}\n')
            env_file.write(f'DB_PORT={port}\n')

    load_dotenv(env_file_path)

def reset_environment_variables():
    env_vars = list(os.environ.keys())
    for var in env_vars:
        del os.environ[var]
    print('Todas las variables de entorno han sido eliminadas.')