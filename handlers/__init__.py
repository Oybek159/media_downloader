from aiogram import Router
from handlers.users import instagram_download


def setup_handle_router():
    router = Router()
    router.include_router(instagram_download.router)
    return router