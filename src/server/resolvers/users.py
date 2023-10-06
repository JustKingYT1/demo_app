from server.database.db_manager import db_manager

from server.database.models import UserAccount

def get(user_id: int) -> dict:
    res = db_manager.execute(query="""SELECT a.userID, a.login, a.password, tou.ID 
                                            FROM Accounts a 
                                            JOIN Users u 
                                                ON a.userID = u.ID 
                                            JOIN TypesOfUsers tou 
                                                ON tou.ID = u.typeID
                                            WHERE a.userID = ?""",
                             args=(user_id,))
    
    res["result"] = None if not res["result"] else UserAccount(
        userID=res["result"][0],
        login=res["result"][1],
        password=res["result"][2],
        access_level=res["result"][3]
    )

    if res["result"] is None:
            res["msg"] = "Not found"
            res["code"] = 400
            res["error"] = True

    return res