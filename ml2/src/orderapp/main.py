from fastapi import FastAPI

app = FastAPI(
    title="🛒 E-commerce API",
    description="API for managing e-commerce operations",
    version="1.0.0"
)

from orderapp.configurations.mysql_conf import engine, base
from orderapp.models.order import Order

# create tables
base.metadata.create_all(bind=engine)

# import router directly
from orderapp.controllers.order_controller import order_router

# debug routes
#for route in app.routes:
    #print("ROUTE:", route.path, route.methods)
app.include_router(order_router)
