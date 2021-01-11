import sqlite3
from sqlite3 import Error
from datetime import datetime

def create_connection(file):
    conn = None
    
    try:
        conn = sqlite3.connect(file)
        return conn
    except Error as e:
        print(e)

def check_user(id):
    conn = create_connection('data.db')
    c = conn.cursor()

    query = """ SELECT * FROM members WHERE id = ? """

    c.execute(query, id)
    record = c.fetchall()
    print(record)

    conn.close()

def add_user(id, name, joined, guild_id):
    conn = create_connection('data.db')
    c = conn.cursor()

    query = """INSERT INTO members VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""

    c.execute(query, (id, guild_id, name, joined, "NA", 0, 0, "NA"))

    conn.commit()
    conn.close()

def add_guild(id, name):
    conn = create_connection('data.db')
    c = conn.cursor()

    query = """INSERT INTO guilds VALUES (?, ?, ?)"""

    c.execute(query, (id, name, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

    conn.commit()
    conn.close()



def update_points(id, guild_id, amount):
    conn = create_connection('data.db')

    c = conn.cursor()

    query = """ UPDATE members SET points = points + ? WHERE member_id = ? AND guild_id = ?"""

    c.execute(query, (amount, id, guild_id))

    conn.commit()
    conn.close()

    

def init():
    conn = create_connection('data.db')

    c = conn.cursor()

    guild_table = """ CREATE TABLE IF NOT EXISTS guilds (
        id integer PRIMARY KEY,
        name text NOT NULL,
        add_date text
    );"""

    member_table = """ CREATE TABLE IF NOT EXISTS members (
        member_id integer,
        guild_id REFERENCES guilds(id), 
        name text NOT NULL,
        join_date text,
        exit_date text,
        points int,
        level int,
        class text
    );"""

    c.execute(guild_table)
    c.execute(member_table)

    conn.commit()
    conn.close()



if __name__ == '__main__':
    init()