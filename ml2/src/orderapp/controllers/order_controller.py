#cerate router for order service
from fastapi import APIRouter
from orderapp.dtos.order_request import OrderRequest    
from orderapp.dtos.order_response import OrderResponse
from orderapp.services.order_service_impl import OrderServiceImpl
order_router = APIRouter()
order_service = OrderServiceImpl()
@order_router.post("/orders", response_model=OrderResponse)
def add_order(order_request:OrderRequest):
    return order_service.add_order(order_request)
@order_router.get("/orders", response_model=list[OrderResponse])
def get_all_orders():
    return order_service.get_all_orders()
