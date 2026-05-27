#create api gateway app
from ensurepip import version

from fastapi import FastAPI
import consul
from gatewayapp.configurations.config import CONSUL_HOST, CONSUL_PORT
from fastapi import HTTPException
#create api gateway app
app = FastAPI(title="API Gateway", description="API Gateway for microservices", version="1.0.0")
#create consul client
consul_client = consul.Consul(host=CONSUL_HOST, 
                              port=CONSUL_PORT)

#create load balancer
LOAD_BALANCERS = {}
#routing table
ROUTING_TABLE = {
    ("POST", "orders"): "order-service",
    ("GET", "payments"): "payment-service"
}
#create routing engine function
def route_engine(method: str, resource: str):
     route_key = (
        
        method.upper().strip(),
        resource.lower().strip()
    )

     if route_key not in ROUTING_TABLE:
        raise HTTPException(
            status_code=404,
            detail=f"No route found for {method} /api/{resource}"
        )

     return ROUTING_TABLE[route_key]


