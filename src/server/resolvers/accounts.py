from server.database.db_manager import db_manager

from server.database.models import AccountPass, Accounts

def new(account: Accounts) -> dict:
    res = db_manager.execute(query="""INSERT INTO Accounts(userID, login, password) 
                                       VALUES(?, ?, ?) 
                                       RETURNING ID""", 
                              args=(account.userID, account.login, account.password))

    res["result"] = None if not res["result"] else get(res["result"][0])["result"]

    return res
    

def get(user_id: int) -> dict:
    res = db_manager.execute(query="""SELECT * 
                                       FROM Accounts 
                                       WHERE userID = ?""", 
                              args=(user_id,))
    
    res["result"] = None if not res["result"] else Accounts(
        userID=res["result"][1],
        login=res["result"][2],
        password=res["result"][3]
    )

    if res["result"] is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res

def get_all() -> dict:
    res = db_manager.execute(query="""SELECT * 
                                       FROM Accounts""", 
                              many=True)
    
    list_accounts = []

    if res["result"]:
        for account in res["result"]:
            list_accounts.append(Accounts(
                userID=account[1],
                login=account[2],
                password=account[3],               
           ))
            
    res["result"] = None if len(list_accounts) == 0 else list_accounts

    if res["result"] is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res


def update(user_id: int, new_password: AccountPass) -> dict:
    res = db_manager.execute(query="""UPDATE Accounts
                                       SET password = ?
                                       WHERE ID = ?""",
                              args=(new_password.password, user_id))
    
    res["result"] = get(user_id=user_id)["result"]

    if res["result"] is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res


def delete(user_id: int) -> dict:
    check_user = get(user_id=user_id)["result"]

    res = db_manager.execute(query="""DELETE FROM Accounts 
                                       WHERE userID = ?""", 
                              args=(user_id,))

    if check_user is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res