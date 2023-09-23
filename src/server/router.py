from server.routers import accounts, list_products, orders


routers = (accounts.accounts_router, list_products.listProducts_router, orders.orders_router)