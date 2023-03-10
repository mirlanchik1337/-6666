import types
import requests
from aiogram.bot import bot
from aiogram.dispatcher import storage
from bs4 import BeautifulSoup
from aiogram import executor  # для запуска бота
from handlers import client, callback, admin, fsm_anketa, extra
from config import dp
import logging
from selenium import webdriver
from aiogram import types, executor, Dispatcher, Bot


client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsm_anketa.register_handlers_anketa(dp)
extra.register_handlers_extra(dp)




if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

