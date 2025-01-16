from aiogram import types, Dispatcher,Bot,executor
from fo import m_menu
#from fo import second_menu

api = '7564045304:AAHyH3hjcm2-poWDsE8CuW2pSZDuE-0kNiE'  
bot = Bot(api)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_hi(sms:types.Message):
    await sms.answer(text='Assalawma aleykum',
                     reply_markup=m_menu)

# @dp.message_handler(text='1')
# async def open_2menu(sms:types.Message):
#     await sms.answer(text='mine taza menu',
#                      reply_markup=second_menu)

# @dp.message_handler(text='izge qaytiw')
# async def back_menu(sms:types.Message):
#     await sms.answer(text='izge qattiniz',
#                      reply_markup=m_menu)

# @dp.message_handler(text='foto jiberiw')
# async def foto(sms:types.Message):
#     suwret=open(file='lesson3/instagram.png',mode='rb') #rb-read binary
#     await sms.answer_photo(
#         photo=suwret,
#         caption='Bul instagram logosi'
#     )


# @dp.message_handler(text='2')
# async def emoji(sms:types.Message):
#     await sms.answer_dice(emoji='⚽')


# @dp.message_handler(text='3')
# async def stiker(sms:types.Message):
#     await sms.answer_sticker(sticker='CAACAgIAAxkBAAENZl1nb5a0EmpIRVR2IEFXLn_FPLE5pQACEgADwDZPEzO8ngEulQc3NgQ')


@dp.message_handler(text='First Name')
async def first(sms:types.Message):
    await sms.reply(f'Sizdin atiniz: {sms.from_user.first_name}')

@dp.message_handler(text='User Name')
async def user(sms:types.Message):
    await sms.reply(f'Sizdin jekeniz: @{sms.from_user.username}')

@dp.message_handler(text='Last Name')
async def last(sms:types.Message):
    #await sms.reply(f'Sizdin ekinshi atiniz: {sms.from_user.last_name}')
    if sms.from_user.last_name:
        await sms.reply(f'Sizdin ekinshi atiniz:{sms.from_user.last_name}')
    else:
        await sms.reply('Sizde Last Name joq!')

@dp.message_handler(text="ID")
async def ide(sms:types.Message):
    await sms.reply(sms.from_user.id)

@dp.message_handler(commands=['bye'])
async def send_hi(sms:types.Message):
    await sms.answer(text='Xosh saw bolin')

if __name__=='__main__':
    executor.start_polling(skip_updates=True,dispatcher=dp)
