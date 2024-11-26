import time
import sqlite3 as sql

def createDB():
    conn = sql.connect("autoconocimiento.db")
    print("Base de datos de autoconocimiento creada")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("autoconocimiento.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE emotional_tracking (
    tracking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    planning_id INTEGER,
    motivation_level INTEGER CHECK (motivation_level BETWEEN 1 AND 10),
    confidence_level INTEGER CHECK (confidence_level BETWEEN 1 AND 10),
    notes TEXT,
     track_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (planning_id) REFERENCES experience_planning(planning_id)
    );
    """)
    print("Tabla creada")
    conn.commit()
    conn .close()

if __name__== "__main__":
    createDB()
    createTable()