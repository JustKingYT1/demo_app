from server.routers import accounts, list_products, orders, remnants_products


routers = (accounts.accounts_router, list_products.listProducts_router, orders.orders_router, remnants_products.remnants_router)