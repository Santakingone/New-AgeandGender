import mysql.connector
from mysql.connector import Error

host = 'o2olb7w3xv09alub.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
database = 'p4ht145tr5m53p17'
user = 'ktttcen0a2sdgaro'
password = 'oetpy3e9ja0ewmek'

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=database
        )
    except Error as e:
        return e

    return connection

def read_query(file_name):
    with open('sql/' + str(file_name), 'r') as f:
        query = f.read()
        return query

def read_query_insert_data(file_name, table=None, value=None):
    with open('sql/' + str(file_name), 'r') as f:
        contents = f.readlines()
        if table and value:
            query = contents[0].format(table=table, value=value)
        return query