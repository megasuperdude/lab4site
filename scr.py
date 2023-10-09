from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from datetime import date
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "5782845642:AAFTH7nkRawy71naGWS2jUfQ6aVoJG9NkPc"

logging.basicConfig(level=logging.INFO)

#create bot
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

chrome_options = Options() #
chrome_options.add_argument('--headless')
chrome_options.add_argument("--window-size=1800x1080")
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options, service=s)




@dp.message_handler(commands=['start'])
async def start(message: types.Message):

	if message.from_user.id == 959040465:
		driver.get('https://edu2.aues.kz/index')

		driver.find_element("id", "login_input").send_keys('Нурбаев_А')

		driver.find_element("id", "pass_input").send_keys('E7#M3$')

		driver.find_element("id", "Submit1").click()

		sleep(1)
		driver.get('https://edu2.aues.kz/v7/#/schedule/studentView')
		sleep(1)

		driver.get_screenshot_as_file("capture.png")
		driver.quit()

		current_date = date.today()
		png=open("capture.png", "rb")
		await bot.send_photo(message.from_user.id, photo=png, caption=current_date)

if __name__ == "__main__":
	executor.start_polling(dp, skip_updates = True)




