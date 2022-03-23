import psycopg2
conn = psycopg2.connect(host = 'localhost', database = 'fastApi', user = 'postgres', password = 'Bellas 19')
print(conn)