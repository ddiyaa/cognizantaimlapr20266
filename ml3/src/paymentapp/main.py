# Create app FIRST
from fastapi import FastAPI
app = FastAPI(
    title="🛒 E-commerce API",
    description="API for managing e-commerce operations",
    version="1.0.0"
)

from paymentapp.configurations.mysql_conf import engine, base

#  IMPORT MODELS FIRST (VERY IMPORTANT)
from paymentapp.models.payment import Payment
#create all the tables in the database
base.metadata.create_all(bind=engine)
#make api call to the customer controller

from paymentapp.controllers import payment_controller


app.include_router(payment_controller.payment_router)




