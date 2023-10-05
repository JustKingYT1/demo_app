from server.database.db_manager import db_manager

from server.database.models import UserAccount


def get(user_id: int) -> dict:
    res = db_manager.execute(query="""SELECT a.userID, a.login, a.password, tou.ID 
                                            FROM Accounts a 
                                            JOIN Users u 
                                                ON a.userID = u.ID 
                                            JOIN TypesOfUsers tou 
                                                ON tou.ID = u.typeID""")
    
    print(res)

    return res