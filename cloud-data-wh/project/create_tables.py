import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


"""drop database tables from drop_table_queries, 
a list with DROP statements
"""
def drop_tables(cur, conn):
    for query in drop_table_queries:
        print('Executing drop: '+query)
        cur.execute(query)
        conn.commit()

""" create database tables from create_table_queries, 
a list with INSERT statements
"""
def create_tables(cur, conn):
    for query in create_table_queries:
        print('Executing create: '+query)
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    print('Connecting to redshift')
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    print('Connected to redshift')
    cur = conn.cursor()

    print('Dropping existing tables if any')
    drop_tables(cur, conn)
    
    print('Creating tables')
    create_tables(cur, conn)

    conn.close()
    print('Create table Ended')


if __name__ == "__main__":
    main()