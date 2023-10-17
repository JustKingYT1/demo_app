from server.database.db_manager import db_manager

from server.database.models import UserAccount, Users

def get(user_id: int) -> dict:
    res = db_manager.execute(query="""SELECT a.userID, a.login, a.password, tou.accessLevel 
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

def get_all() -> dict:
    res = db_manager.execute(query="""SELECT * 
                                       FROM Users""", 
                              many=True)

    list_users = []

    if res["result"]:
        for user in res["result"]:
            list_users.append(Users(
                ID=user[0],
                typeID=user[1],
                FIO=user[2],
                phone=user[3],
                date_birth=user[4]
            ))

    res["result"] = None if len(list_users) == 0 else list_users

    if res["result"] is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res

      