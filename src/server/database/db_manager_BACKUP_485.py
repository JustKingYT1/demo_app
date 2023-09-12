import sqlite3
<<<<<<< HEAD
import sys

sys.path.append("C:\demo_app\src")

import settings
=======
import os

>>>>>>> 6189f41d7458f4030266ace48f8455c5ab9b903f

class DBManager:
    def __init__(self, default_path: str) -> None:
        self.default_path = default_path
    
    def connect_to_db(self) -> tuple[sqlite3.Connection, sqlite3.Cursor]:
        conn = sqlite3.connect(self.default_path)
        cur = conn.cursor()
        return conn, cur
<<<<<<< HEAD
=======
    
    def check_base(self) -> bool:
        return os.path.exists(self.default_path)
>>>>>>> 6189f41d7458f4030266ace48f8455c5ab9b903f

    def execute(self, query: str, args: tuple[str] = (), many: bool = False) -> dict:
        conn, cur = self.connect_to_db()
        try: 
            res = cur.execute(query, args)
            if many:
                result = res.fetchall()
            else:
                result = res.fetchone()
        except sqlite3.Error as err:
            conn.close()
            return {"code": 400, "msg": err, "error": True, "result": None}
        conn.commit()
        conn.close()
        return {"code": 200, "msg": "Successfully", "error": False, "result": result}

<<<<<<< HEAD
    def create_base(self, sql_file: str) -> None:
        connect, cursor = self.connect_to_db()
        if self.check_base():
            cursor.executescript(open(sql_file).read())
            connect.commit()
            connect.close()
    

db_manager = DBManager(default_path=settings.DB_PATH)

print(db_manager.create_base(f"{settings.SCRIPTS_DIR}\\base.sql" ))
=======
    def create_base(self, path_script: str) -> dict:
        return self.execute(query=open(path_script).read(), many=True)


db_manager = DBManager(default_path="scripts\\base.sql")
>>>>>>> 6189f41d7458f4030266ace48f8455c5ab9b903f
