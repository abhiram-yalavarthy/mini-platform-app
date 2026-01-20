from fastapi import FastAPI
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

app = FastAPI(title="mini-platform-api")

REQS = Counter("http_requests_total", "Total HTTP requests", ["path"])
LAT = Histogram("http_request_latency_seconds", "Request latency", ["path"])

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/ready")
def ready():
    # later: check DB/redis/etc.
    return {"ready": True}

@app.get("/hello")
def hello():
    path = "/hello"
    REQS.labels(path=path).inc()
    with LAT.labels(path=path).time():
        return {"message": "hello from k3s on EC2"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
