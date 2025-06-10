import pyodbc 
conn = pyodbc.connect(
    'DRIVER={SQL Server};''SERVER=localhost;''DATABASE=master;''UID=sa;''PWD=felijopanda.99' )
cursor = conn.cursor()

cursor.execute("SELECT name FROM sys.tables")
print("Tabellen in der Datenbank:")
for row in cursor.fetchall():
    print(" -", row.name)
 
cursor.execute("SELECT * FROM MojoJojo.dbo.Teilnehmer")
print("\nInhalt der Tabelle 'Teilnehmer':")
columns = [column[0] for column in cursor.description]
rows = cursor.fetchall()
 
for row in rows:
    print(dict(zip(columns, row)))
 
cursor.close()
conn.close()