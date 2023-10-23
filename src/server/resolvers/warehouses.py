from server.database.db_manager import db_manager

from server.database.models import Warehouses

def get_all() -> dict:
    res = db_manager.execute(query="""SELECT * 
                                       FROM Warehouses
                                       """,
                             many=True)
    
    list_warehouses = []

    if res["result"]:
        for warehouse in res["result"]:
            list_warehouses.append(Warehouses(
                ID=warehouse[0],
                name=warehouse[1],
                locationID=warehouse[2],
                phone=warehouse[3]
            ))

    res["result"] = None if len(list_warehouses) == 0 else list_warehouses

    if res["result"] is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res

