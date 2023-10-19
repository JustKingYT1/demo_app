from server.database.db_manager import db_manager

from server.database.models import Products, ProductsGet

def new(product: Products) -> dict:
    res = db_manager.execute(query="""INSERT INTO Products(ID, title, cost) 
                                          VALUES(?, ?, ?) 
                                          RETURNING ID""", 
                              args=(product.ID, product.title, product.cost))
    
    # res["result"] = None if not res["result"] else get(res["result"][0])["result"]

    return res

def get(product: ProductsGet) -> dict:
    res = db_manager.execute(query=f'''SELECT * 
                                       FROM Products
                                       WHERE title LIKE ?''',
                             args=(f'{product.title}%',),
                            many=True)
 
    list_products = []

    if res["result"]:
        for productone in res["result"]:
            list_products.append(Products(
                ID=productone[0],
                title=productone[1],
                cost=productone[2]
            ))
        res["result"] = None if len(list_products) == 0 else list_products

    if product.title == '':
        res = get_all()

    if res["result"] is None:
            res["msg"] = "Not found"
            res["code"] = 400
            res["error"] = True

    return res

def get_all() -> dict:
    res = db_manager.execute(query="""SELECT * 
                                       FROM Products""", 
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
