import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="Titanic_db",
    user="postgres",
    password=input("Enter PostgreSQL password: ")
)

cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM titanic_project.passengers")

result = cur.fetchone()

print("Total passengers:", result[0])

cur.close()
conn.close()