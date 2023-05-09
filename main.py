from fastapi import FastAPI


from api.routes.router import router as api_router

app = FastAPI(title="Fapro API", version="1.0")


app.include_router(api_router, prefix="")
