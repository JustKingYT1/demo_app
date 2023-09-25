from database.db_manager import db_manager

from database.models import AccountLog, AccountPass, Accounts

def new(account: Accounts) -> dict:
    res =  db_manager.execute(query="""INSERT INTO Accounts(userID, login, password) 
                                       VALUES(?, ?, ?) 
                                       RETURNING ID""", 
                              args=(account.userID, account.login, account.password))
    
    res["result"] = None if not res["result"] else get(res["result"][0])

    return res
    

def get(user_id: int) -> dict:
    res = db_manager.execute(query="""SELECT * 
                                       FROM Accounts 
                                       WHERE ID = ?""", 
                              args=(user_id,))

    res["result"] = None if not res["result"] else Accounts(
        id=res["result"][0],
        login=res["result"][1],
        password=res["result"][2],
        userID=res["result"][3]
    )

    return res

def get_all() -> dict:
    res = db_manager.execute(query="""SELECT * 
                                       FROM Accounts""", 
                              many=True)
    
    list_accounts = []

    if res["result"]:
        for account in res["result"]:
            list_accounts.append(Accounts(
                id=account["result"][0],
                login=account["result"][1],
                password=account["result"][2],
                userID=account["result"][3]                
            ))


def update_login(user_id: int, new_login: AccountLog) -> dict:
    res = db_manager.execute(query="""UPDATE Accounts 
                                       SET login = ? 
                                       WHERE ID = ?
                                       RETURNING ID""",
                              args=(user_id, new_login.login))
    
    res["msg"] = None if not res["result"] else "Successfully"
    res["result"] = None if not res["result"] else get(res["result"][0])

    return res

def update_password(user_id: int, new_password: AccountPass) -> dict:
    res = db_manager.execute(query="""UPDATE Accounts
                                       SET password = ?
                                       WHERE ID = ?
                                        RETURNING ID""",
                              args=(user_id, new_password.password))
    
    res["msg"] = None if not res["result"] else "Successfully"
    res["result"] = None if not res["result"] else get(res["result"][0])

    return res


def delete(user_id: int) -> dict:
    return db_manager.execute(query="""DELETE FROM Accounts 
                                       WHERE userID = ?""", 
                              args=(user_id,))