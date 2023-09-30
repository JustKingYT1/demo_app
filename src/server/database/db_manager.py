import sqlite3
import os
import sys

sys.path.append("C:\demo_app\src")

import settings 

class DBManager:
    def __init__(self, default_path: str) -> None:
        self.default_path = default_path
    
    def connect_to_db(self) -> tuple[sqlite3.Connection, sqlite3.Cursor]:
        conn = sqlite3.connect(self.default_path)
        cur = conn.cursor()
        return conn, cur
    
    def check_base(self) -> bool:
        return os.path.exists(self.default_path)

    def execute(self, query: str, args: tuple = (), many: bool = False) -> dict:
        conn, cur = self.connect_to_db()
        try: 
            res = cur.execute(query, args)
            if many:
                result = res.fetchall()
            else:
                result = res.fetchone()
        except sqlite3.Error as err:
            conn.close()
            return {"code": 400, "msg": str(err), "error": True, "result": None}
        conn.commit()
        conn.close()
        return {"code": 200, "msg": "Successfully", "error": False, "result": result}

    def create_base(self, script_path: str) -> None:
        conn, cur = self.connect_to_db()
        if self.check_base():
            cur.executescript(open(script_path).read())
            conn.commit()
            conn.close()


db_manager = DBManager(default_path=settings.DB_PATH)
    