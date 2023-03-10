import sqlite3
conn = sqlite3.connect("PERFIL EMPRESA SA.sqlite")
c = conn.cursor()

c.execute("CREATE TABLE datosest  (nombre TEXT,asunto TEXT,fecha INTEGER)")


conn.commit()
conn.close()