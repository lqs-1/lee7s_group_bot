# CommandHandler:命令处理器
# MessageHandler:消息处理器
import logging

from telegram.ext import CommandHandler, MessageHandler, filters, CallbackQueryHandler
from telegram.ext._application import Application
from app.handler.commandHandler import start, help, forward_message, forward_message_re


def register_all_handler(application: Application):
    # 添加命令处理器

    logging.info("application register 'go' command handler")
    application.add_handler(CommandHandler("go", forward_message))
    logging.info("application register 'start' command handler")
    application.add_handler(CommandHandler('start', start))

    logging.info("application register ALL message handler")
    application.add_handler(MessageHandler(filters.ALL, forward_message_re))

