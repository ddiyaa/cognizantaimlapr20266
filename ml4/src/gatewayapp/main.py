import httpx
from itertools import cycle

import consul
from fastapi import FastAPI, HTTPException, Request, Response

app = FastAPI(
    title="API Gateway",
    description="API Gateway for microservices",
    version="1.0.0"
)

CONSUL_HOST = "localhost"
CONSUL_PORT = 8500

consul_client = consul.Consul(
    host=CONSUL_HOST,
    port=CONSUL_PORT
)

LOAD_BALANCERS = {}

# Based on your Consul UI:
# payment-service-1 -> 8001
# payment-service-2 -> 8004
ROUTING_TABLE = {
    ("POST", "payments"): "payment-service-1",
    ("GET", "payments"): "payment-service-2"
}


def route_engine(method: str, resource: str):
    route_key = (
        method.upper().strip(),
        resource.lower().strip()
    )

    if route_key not in ROUTING_TABLE:
        raise HTTPException(
            status_code=404,
            detail=f"No route found for {method} /{resource}"
        )

    return ROUTING_TABLE[route_key]


def get_service_instance(service_name: str):
    print("Searching service:", service_name)

    index, services = consul_client.health.service(
        service=service_name,
        passing=True
    )

    if not services:
        raise HTTPException(
            status_code=503,
            detail=f"No healthy instances found for {service_name}"
        )

    instances = []

    for item in services:
        service = item["Service"]
        address = service["Address"]
        port = service["Port"]

        print(f"Found healthy instance: {address}:{port}")
        instances.append(f"http://{address}:{port}")

    current_instances = LOAD_BALANCERS.get(service_name, {}).get("instances")

    if current_instances != instances:
        LOAD_BALANCERS[service_name] = {
            "instances": instances,
            "cycle": cycle(instances)
        }

    return next(LOAD_BALANCERS[service_name]["cycle"])


async def forward_request(
    service_url: str,
    resource: str,
    order_id: int,
    request: Request
):
    target_url = f"{service_url}/{resource}/{order_id}"

    print("Forwarding request to:", target_url)

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=target_url,
            params=request.query_params,
            content=await request.body(),
            headers={
                key: value
                for key, value in request.headers.items()
                if key.lower() != "host"
            }
        )

    return Response(
        content=response.content,
        status_code=response.status_code,
        media_type=response.headers.get("content-type")
    )


@app.get("/")
def home():
    return {
        "message": "API Gateway running",
        "consul_host": CONSUL_HOST,
        "consul_port": CONSUL_PORT,
        "routes": {
            "create_payment": "POST /payments/{order_id} -> payment-service-1",
            "get_payment": "GET /payments/{order_id} -> payment-service-2"
        }
    }


@app.post("/payments/{order_id}")
async def create_payment_gateway(order_id: int, request: Request):
    service_name = route_engine("POST", "payments")
    service_url = get_service_instance(service_name)

    return await forward_request(
        service_url=service_url,
        resource="payments",
        order_id=order_id,
        request=request
    )


@app.get("/payments/{order_id}")
async def get_payment_gateway(order_id: int, request: Request):
    service_name = route_engine("GET", "payments")
    service_url = get_service_instance(service_name)

    return await forward_request(
        service_url=service_url,
        resource="payments",
        order_id=order_id,
        request=request
    )