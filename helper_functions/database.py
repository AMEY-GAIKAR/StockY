import psycopg2

connection_string = 'postgresql://amey:gAUNGKnhZcoPk1tx70SIRA@malphite-3116.7s5.cockroachlabs.cloud:26257/StockY?sslmode=verify-full'
connection = psycopg2.connect(connection_string)
print('Connection Successfull')

cursor = connection.cursor()
cursor.execute('''''')
connection.commit()

connection.close()