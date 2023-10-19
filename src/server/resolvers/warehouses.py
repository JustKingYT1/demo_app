from server.database.db_manager import db_manager

from server.database.models import Warehouses

def get_all(accountID: int) -> dict:
    res = db_manager.execute(query="""SELECT * 
                                       FROM Warehouses
                                       """,
                             many=True)
    
    list_warehouses = []

    if res["result"]:
        for warehouse in res["result"]:
            list_warehouses.append(Warehouses(
                name=warehouse[0],
                locationID=warehouse[1],
                phone=warehouse[2]
            ))

    res["result"] = None if len(list_warehouses) == 0 else list_warehouses

    if res["result"] is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res

