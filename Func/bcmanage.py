import sqlite3
con = sqlite3.connect("database.db")
c = con.cursor()
#
#             EM DESENVOLVIMENTO
#
class DatabaseManager():
    def create():
        c.execute("CREATE TABLE IF NOT EXISTS Users(id interger, user text, passw text, cargo text)")
        c.execute("CREATE TABLE IF NOT EXISTS Clientes(id interger, name text, cell text, tell text, addres text, "
                  "email text)")
        #c.execute("CREATE TABLE IF NOT EXISTS Equipamentos")
    def read():
        pass
    def update():
        pass
    def delete():
        pass
