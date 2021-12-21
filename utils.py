import sqlite3

try:
    conn = sqlite3.connect('prueba.db', check_same_thread = False)
    cur = conn.cursor()
except:
    pass

def db_create_table():
    try:
        # prioridad: 1 alta 2 media 3 baja
        cur.execute("""
            CREATE TABLE 'tasks' (
                'id_task' INTEGER PRIMARY KEY AUTOINCREMENT,
                'title' TEXT,
                'description' TEXT,
                'start_date' DATE,
                'end_date' DATE,
                'time' TIME,
                'priority' INTEGER
            )
        """)
        conn.commit()
        msg = 'Tabla creada correctamente'
    except:
        msg = 'Tabla ya existe'
    return msg

#Crea la tarea en la database
def db_create_task(title, description, start_date, end_date, time, priority):
    query = ("INSERT INTO 'tasks' VALUES (?, ?, ?, ?, ?, ?, ?)")
    parameters = (None, title, description, start_date, end_date, time, priority)
    cur.execute(query, parameters)
    conn.commit()
    msg = 'Tarea creada'
    return msg


