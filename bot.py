import asyncio
from aiogram import Bot, Dispatcher

import middlewares

async def main():
    bot = Bot(config.bot_token.get_secret_value(), parse_mode="MarkdownV2")
    dp = Dispatcher()
    setup_logging()
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
    
if name == "main":
    asyncio.run(main())
