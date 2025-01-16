from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

m_menu=ReplyKeyboardMarkup(resize_keyboard=True)
# one=KeyboardButton(text='1')
# two=KeyboardButton(text='2')
# three=KeyboardButton(text='3')
# four=KeyboardButton(text='4')
# five=KeyboardButton(text='5')
# six=KeyboardButton(text='6')
# seven=KeyboardButton(text='7')
# eight=KeyboardButton(text='8')
# nine=KeyboardButton(text='9')
# zero=KeyboardButton(text='0')


first_name=KeyboardButton(text='First Name')
last_name=KeyboardButton(text='Last Name')
username=KeyboardButton(text='User Name')
ID=KeyboardButton(text="ID")

m_menu.add(first_name,last_name)
m_menu.add(ID,username)

# second_menu=ReplyKeyboardMarkup(resize_keyboard=True)

# foto=KeyboardButton(text='foto jiberiw')
# video=KeyboardButton(text='video jiberiw')
# back=KeyboardButton(text='izge qaytiw')

# second_menu.add(foto,video)
# second_menu.add(back)
