from aiogram import Dispatcher

from . import aiogram_logging

def setup(dp: Dispatcher) -> None:
  dp.update.middleware(bot_logging.LoggingMiddleware())
