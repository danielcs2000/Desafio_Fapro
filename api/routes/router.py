from fastapi import APIRouter
from api.routes import uf

router = APIRouter()


@router.get("/", tags=["Health Check"])
def health_check():
    return {"message": f"It Works!"}


router.include_router(
    uf.router,
    prefix="/uf",
    tags=["UF"],
)
