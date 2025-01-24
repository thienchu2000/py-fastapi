from fastapi import APIRouter
from controllers.HomeController import HomeController
router = APIRouter()

@router.get("/")
def home():
    return HomeController.getApi()
