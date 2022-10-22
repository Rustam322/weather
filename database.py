import psycopg2

database = psycopg2.connect(
    database='ls4',
    host='localhost',
    user='postgres',
    password='123456'
)

cursor = database.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather(
        weather_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        city VARCHAR(20),
        temp VARCHAR(5),
        wind VARCHAR(5),
        sunrice VARCHAR(25),
        sunset VARCHAR(25)
    );
''')
database.commit()
database.close()


