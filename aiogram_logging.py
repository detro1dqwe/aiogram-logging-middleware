from typing import Callable, Awaitable, Dict, Any
from aiogram import BaseMiddleware
from aiogram.types import Update
import logging

class LoggingMiddleware(BaseMiddleware):
    def init(self):
        self.logger = logging.getLogger('aiogram.middlware.logging')
        
    async def call(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any]
    ) -> Any:
        if event.message:
            self.logger.info(f'Recieved message from user_id={event.message.from_user.id} with text="{event.message.text}", message_id={event.message.message_id}')
        elif event.callback_query:
            self.logger.info(f'Recieved callback from user_id={event.callback_query.from_user.id} with callback_data="{event.callback_query.data}" on message_id={event.callback_query.message.message_id}')
        return await handler(event, data)
