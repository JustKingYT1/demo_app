from database.db_manager import db_manager

from database.models import RemnantsOfProducts

def new(product: RemnantsOfProducts) -> dict:
    res = db_manager.execute(query="""INSERT INTO RemnantsOfProducts(warehouseID, productID, count) 
                                          VALUES(?, ?, ?) 
                                          RETURNING warehouseID""", 
                             args=(product.warehouseID, product.productID, product.count))
    
    res["result"] = None if not res["result"] else get(res['result'][0])
    
    return res


def get(warehouse_id: int) -> dict:
    res = db_manager.execute(query="""SELECT * 
                                       FROM RemnantsOfProducts 
                                       WHERE warehouseID = ?""", 
                             args=(warehouse_id,))

    res["result"] = None if not res["result"] else RemnantsOfProducts(
        id=res["result"][0],
        warehouseID=res["result"][1],
        productID=res["result"][2],
        count=res["result"][3]
    ) 

    return res


def get_all() -> dict:
    res = db_manager.execute(query="""SELECT * 
                                       FROM RemnantsOfProducts
                                       GROUP BY warehouseID""", 
                              many=True)
    
    list_warhouses = []

    if res["result"]:
        for warehouse in res["result"]:
            list_warhouses.append(RemnantsOfProducts(
                id=warehouse["result"][0],
                warehouseID=warehouse["result"][1],
                productID=warehouse["result"][2],
                count=warehouse["result"][3]
            ))
        res["result"] = list_warhouses
    else:
        res["result"] = None

    return res


def update(new_data: RemnantsOfProducts) -> dict:
    res = db_manager.execute(query="""UPDATE RemnantsOfProducts(productID, count) 
                                       SET (?, ?, ?) 
                                       WHERE (warehouseID, productID) = (?, ?)
                                       RETURNING ID""",
                              args=(new_data.productID, new_data.count, new_data.warehouseID, new_data.productID))
    
    res["result"] = None if not res["result"] else get(res["result"][0])

    return res


def delete(data: RemnantsOfProducts) -> dict:
    return db_manager.execute(query="""DELETE FROM RemnantsOfProducts WHERE (warehouseID, productID) = (?, ?) """,
                              args=(data.orderID, data.productID))