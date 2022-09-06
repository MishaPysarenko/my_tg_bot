import telebot
from telebot import types
import pyodbc
import time

connection = pyodbc.connect("""DRIVER=SQL Server Native Client 11.0;DATABASE=test_database;Trusted_Connection=Yes;SERVER=.""")
cursor = connection.cursor()
global mySQLQuery

bot = telebot.TeleBot('5511019814:AAE6VhsF7g-tYmAuOJG7UWfTBCl-Rpll40o')
@bot.message_handler(commands = ["start"])
def start(message):
	#menu1 = telebot.types.InlineKeyboardMarkup()
	#menu1.add(telebot.types.InlineKeyboardButton(text = 'Створити жижку по своїму смаку', callback_data ='create'))
	#menu1.add(telebot.types.InlineKeyboardButton(text = 'Подивитись всі замовлення', callback_data ='show_amount'))
	#msg = bot.send_message(message.chat.id, "Привіт👋, цей бот призначен для замовлення жижок для вейпів по індивідуальному смаку😋\nАбо замовлення готових варіантів😉", reply_markup = menu1)
	#bot.register_next_step_handler(msg, mainmenu)
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("Головне меню")
	markup.add(btn1)
	msg = bot.send_message(message.chat.id,"Привіт👋", reply_markup = markup)

@bot.callback_query_handler(func=lambda callback: callback.data)
def mainmenu(message):
	if all.data == 'create':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("Начати с початку")
		markup.add(btn1)
		msg = bot.send_message(call.message.chat.id, "натисніть кнопку для продожвення".format(call.message.from_user), reply_markup=markup)
	elif call.data == 'show_amount':
		ID = call.from_user.id
		mySQLQuery = ("""SELECT [ID],[date],[amount],[taste],[nicotin],[ratio],[price],[city],[adress],[num],[name]
						 FROM [test_database].[dbo].[orders]
						 WHERE [ID] = """+str(ID)+"""""")
		cursor.execute(mySQLQuery)
		result = cursor.fetchall()
		for row in result:
			user_id = row[0]
			user_date = row[1]
			user_amount = row[2]
			user_taste = row[3]
			user_nicotin = row[4]
			user_ratio = row[5]
			user_price = row[6]
			user_city = row[7]
			user_departament = row[8]
			user_num = row[9]
			user_name = row[10]
			bot.send_message(call.from_user.id, "ID замовника:"+str(user_id)+"\nІНФОРМАЦІЯ ПО ЖИЖЦІ\nкількість в мл: "+str(user_amount)+"\nсмак: "+str(user_taste)+"\nкількість нікотину: "+str(user_nicotin)+"\nспіввідношення: "+str(user_ratio)+"\nорієнтовна ціна замовлення: "+str(user_price)+"\nІНФОРМАЦІЯ ПО ДОСТАВЦІ\nдата замовлення: "+str(user_date)+"\nмісто: "+str(user_city)+"\nномер відділення нової пошти: "+str(user_departament)+"\nномер тел. на який відправляється замовлення:\n"+str(user_num)+"\nПІБ замовника:\n"+str(user_name))
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("Головне меню")
		markup.add(btn1)
		bot.send_message(call.from_user.id, "Повернутись до головного меню", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def text(message):
	if(message.text == "Начати с початку"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("30")
		btn2 = types.KeyboardButton("55")
		markup.add(btn1, btn2)
		msg = bot.send_message(message.chat.id, "для початку введи кількість в мл 🍷".format(message.from_user), reply_markup=markup)
		bot.register_next_step_handler(msg , add1)
	elif(message.text == "Головне меню"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("додати замовлення")
		btn2 = types.KeyboardButton("подивитись свої замовлення")
		markup.add(btn1, btn2)
		msg = bot.send_message(message.chat.id, "Меню", reply_markup=markup)
	elif(message.text == "додати замовлення"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("30")
		btn2 = types.KeyboardButton("55")
		markup.add(btn1, btn2)
		msg = bot.send_message(message.chat.id, "для початку введи кількість в мл 🍷".format(message.from_user), reply_markup=markup)
		bot.register_next_step_handler(msg, add1)
	elif(message.text == "подивитись свої замовлення"):
		ID = message.chat.id
		mySQLQuery = ("""SELECT [ID],[date],[amount],[taste],[nicotin],[ratio],[price],[city],[adress],[num],[name]
						 FROM [test_database].[dbo].[orders]
						 WHERE [ID] = """+str(ID)+"""""")
		cursor.execute(mySQLQuery)
		result = cursor.fetchall()
		for row in result:
			user_id = row[0]
			user_date = row[1]
			user_amount = row[2]
			user_taste = row[3]
			user_nicotin = row[4]
			user_ratio = row[5]
			user_price = row[6]
			user_city = row[7]
			user_departament = row[8]
			user_num = row[9]
			user_name = row[10]
			bot.send_message(message.chat.id, "ID замовника:"+str(user_id)+"\nІНФОРМАЦІЯ ПО ЖИЖЦІ\nкількість в мл: "+str(user_amount)+"\nсмак: "+str(user_taste)+"\nкількість нікотину: "+str(user_nicotin)+"\nспіввідношення: "+str(user_ratio)+"\nорієнтовна ціна замовлення: "+str(user_price)+"\nІНФОРМАЦІЯ ПО ДОСТАВЦІ\nдата замовлення: "+str(user_date)+"\nмісто: "+str(user_city)+"\nномер відділення нової пошти: "+str(user_departament)+"\nномер тел. на який відправляється замовлення:\n"+str(user_num)+"\nПІБ замовника:\n"+str(user_name))
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("Головне меню")
		markup.add(btn1)
		bot.send_message(message.chat.id, "Повернутись до головного меню", reply_markup=markup)

@bot.message_handler(commands = ["add"])
def add(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("30")
	btn2 = types.KeyboardButton("55")
	markup.add(btn1, btn2)
	msg = bot.send_message(message.chat.id, "для початку введи кількість в мл 🍷".format(call.message.from_user), reply_markup=markup)
	bot.register_next_step_handler(msg, add1)
def add1(message):
	print(message.message_id)
	global mil
	mil = message.text
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("яблуко")
	btn2 = types.KeyboardButton("кокос")
	btn3 = types.KeyboardButton("кока-кола")
	btn4 = types.KeyboardButton("Мигдальний амаретто")
	btn5 = types.KeyboardButton("банан")
	btn6 = types.KeyboardButton("Банановий крем")
	markup.add(btn1, btn2, btn3,btn4,btn5,btn6)
	msg = bot.send_message(message.chat.id, "виберіть\nабо введіть свій смак 😋".format(message.from_user), reply_markup=markup)
	bot.register_next_step_handler(msg, add2)
def add2(message):
	global taste
	taste = message.text
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("0")
	markup.add(btn1)
	msg = bot.send_message(message.chat.id,"введіть кількість нікотину🤯\nякщо ви бажаєте без нікотину введіть \"0\"".format(message.from_user), reply_markup=markup)
	bot.register_next_step_handler(msg, add3)
def add3(message):
	global nicotin
	nicotin = message.text
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("20/80")
	btn2 = types.KeyboardButton("30/70")
	btn3 = types.KeyboardButton("40/60")
	btn4 = types.KeyboardButton("50/50")
	btn5 = types.KeyboardButton("60/40")
	btn6 = types.KeyboardButton("70/30")
	btn7 = types.KeyboardButton("80/20")
	markup.add(btn1, btn2, btn3,btn4,btn5,btn6,btn7)
	msg = bot.send_message(message.chat.id,"введіть співвівдношення PG/VG 🤷🏼‍♀️".format(message.from_user), reply_markup=markup)
	bot.register_next_step_handler(msg, add4)
def add4(message):
	global pg_vg
	pg_vg = message.text
	a = types.ReplyKeyboardRemove()
	msg = bot.send_message(message.chat.id,"введіть місто куди відправляти замовлення🌃", reply_markup = a)
	bot.register_next_step_handler(msg, add5)
def add5(message):
	global city
	city = message.text
	msg = bot.send_message(message.chat.id,"введіть номер відділення нової пошти🏨")
	bot.register_next_step_handler(msg, add6)
def add6(message):
	global adress
	adress = message.text
	msg = bot.send_message(message.chat.id,"введіть номер отримувача📞😎")
	bot.register_next_step_handler(msg, add7)
def add7(message):
	global num
	num = message.text
	msg = bot.send_message(message.chat.id,"введіть ПІБ на яке відправляти замовлення🎩")
	bot.register_next_step_handler(msg, add8)
def add8(message):
	amount = ((float(mil)*2)+(80)+(float(nicotin)*5))
	global data 
	data = time.asctime()
	global pib
	pib = message.text
	u_id = message.chat.id
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("Головне меню")
	markup.add(btn1)
	ordes = "🆔ID замовника:"+str(u_id)+"\n🌫ІНФОРМАЦІЯ ПО ЖИЖЦІ🌫\n🍷кількість в мл: "+str(mil)+"\n😋смак: "+str(taste)+"\n🤯кількість нікотину: "+str(nicotin)+"\n🤷🏼‍♀️співвідношення: "+str(pg_vg)+"\n💳орієнтовна ціна замовлення: "+str(int(amount))+"\n🚚ІНФОРМАЦІЯ ПО ДОСТАВЦІ🚛\n📅дата замовлення: "+str(data)+"\n🌃місто: "+str(city)+"\n🏨номер відділення нової пошти: "+str(adress)+"\n📞😎номер тел. на який відправляється замовлення:\n"+str(num)+"\n🎩ПІБ замовника:\n"+str(pib)
	msg = bot.send_message(message.chat.id,ordes, reply_markup=markup)
	global mySQLQuery
	mySQLQuery = "insert into orders (ID , date, amount, taste, nicotin, ratio, price, city, adress, num, name) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(str(u_id),str(data),str(mil),str(taste),str(nicotin),str(pg_vg),str(int(amount)),str(city),str(adress),str(num),str(pib))
	cursor.execute(mySQLQuery)
	connection.commit()
	#bot.send_message(546815948, "збереженно замовлення від\n"+str(message.first_name)+"\n"+str(message.last_name)+"\nчас та дата замовлення:\n"+str(data)+"\nсмак: "+str(taste)+"\nнікотін: "+str(nicotin)+"\nспіввідношення: "+str(pg_vg)+"\nадресса: місто "+str(city)+" нова пошта №"+str(adress)+"\nномер: "+str(num)+"ім'я на яке відправляти:\n"+str(pib))
	bot.register_next_step_handler(msg, add9)
def add9(message):
	if(message.text == "Головне меню"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("Головне меню")
		markup.add(btn1)
		msg = bot.send_message(message.chat.id,"Добре 😄", reply_markup = markup)
		
	elif(message.text == "Змінити замовлення"): 
		msg = bot.send_message(message.chat.id,"Добре дякуємо за замовлення😉")
		bot.register_next_step_handler(msg, add)

bot.polling(none_stop = True)
connection.close()

