from server.routers import accounts, list_products, orders, products, remnants_products, users


routers = (accounts.accounts_router, list_products.listProducts_router, 
           orders.orders_router, remnants_products.remnants_router, 
           users.users_router, products.products_router)