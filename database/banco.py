import psycopg2
from psycopg2 import OperationalError


def create_connection(db_name, db_user, db_password, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            port=db_port
        )
        print("Conexão com banco de dados PostgreSQL successfull")
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")
    return connection


if __name__ == "__main__":
    connection = create_connection(
        "tersetec_db", "postgres", "1234", "5432"
    )
