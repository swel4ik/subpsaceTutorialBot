import asyncio
from aiogram import Bot, Dispatcher
import main_router
import docker_router
import installation_router


async def main():
    bot = Bot(token="5384669677:AAHepwAcMJWbcoesDOtC3jiqzty3ztsbGR8")
    dp = Dispatcher()
    dp.include_router(installation_router.router)
    dp.include_router(docker_router.router)
    dp.include_router(main_router.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())