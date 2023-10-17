from server.database.db_manager import db_manager

from server.database.models import Products, ProductsGet

def new(order: Products) -> dict:
    res = db_manager.execute(query="""INSERT INTO Orders(ID, accountID, trackNumber, totalCost, completed) 
                                          VALUES(?, ?, ?, ?, ?) 
                                          RETURNING ID""", 
                              args=(order.ID, order.accountID, order.track_number, order.total_cost, order.completed))
    
    res["result"] = None if not res["result"] else get(res["result"][0])["result"]

    return res

def get(product: ProductsGet) -> dict:
    res = db_manager.execute(query='''SELECT * 
                                       FROM Product 
                                       WHERE title LIKE "?%"''' if not product.title == '' else """SELECT * 
                                                                                            FROM Product""", 
                              args=(product.title,) if not product.title == '' else (),
                              many=True) 
    print(res)
    list_products = []

    if res["result"]:
        if product.title == '':
            for product in res["result"]:
                list_products.append(Products(
                    ID=product[0],
                    title=product[1],
                    cost=product[2]
                ))
            res["result"] = None if len(list_products) == 0 else list_products
        else:
            print(res)
            res["result"] = Products(
                                                ID=res["result"][0][0],
                                                title=res["result"][0][1],
                                                cost=res["result"][0][2]
                                            )

    if res["result"] is None:
            res["msg"] = "Not found"
            res["code"] = 400
            res["error"] = True

    return res

def get_all() -> dict:
    res = db_manager.execute(query="""SELECT * 
                                       FROM Product""", 
                              many=True)

    list_products = []

    if res["result"]:
        for product in res["result"]:
            list_products.append(Products(
                ID=product[0],
                title=product[1],
                cost=product[2]
            ))

    res["result"] = None if len(list_products) == 0 else list_products

    if res["result"] is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res
