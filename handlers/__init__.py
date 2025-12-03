from aiogram import Router
from handlers.users import instagram_download, youtube_download


def setup_handle_router():
    router = Router()
    router.include_router(instagram_download.router)
    router.include_router(youtube_download.router)
    return router