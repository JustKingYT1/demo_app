import fastapi

from server.database.models import ProductsGet
from server.resolvers import products


products_router = fastapi.APIRouter(prefix='/products', tags=["Products"])


@products_router.post(path='/get', response_model=dict)
def get_product(product: ProductsGet) -> dict:
    return products.get(product=product)


@products_router.get(path='/get', response_model=dict)
def get_all_products() -> dict:
    return products.get_all()
