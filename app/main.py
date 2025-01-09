from fastapi import FastAPI

from app.api import api_router
from app.core.setup_lifspan import lifespan


app = FastAPI(
    title="Oryza AI FastAPI Backend",
    docs_url="/",
    lifespan=lifespan,
)

app.include_router(api_router, prefix="")
