from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import location

import var
import db
mahsulot1="Mahsulot"
mahsulotlar=InlineKeyboardMarkup().row(mahsulot1,mahsulot1).row(mahsulot1,mahsulot1)
Langbut=InlineKeyboardMarkup()
Langbut.row(InlineKeyboardButton(text='Uzb',callback_data='uz'),InlineKeyboardButton(text='Рус',callback_data='ru'))
bot=Bot(token="5133080417:AAGOnTa0rzqlw0bHS31gDQA1QBTeapTFOWQ")
dp=Dispatcher(bot)
ddb=db.Database('users.db')

share_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
share_location = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
share_keyboard2 = types.ReplyKeyboardRemove()
share_button = types.KeyboardButton(text="☎ Telefon raqamni Ulashish", request_contact=True)
share_keyboard.add(share_button)
location = types.KeyboardButton(text="📍", request_location=True)
share_location.add(location)
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    if ddb.exists(message.from_user.id)==False:
        ddb.add_user(message.from_user.id)
        await message.reply('🇺🇿Salom hurmatli foydalanuvchi. Foydalanish uchun o\'zingizga qulay bo\'lgan tilni tanlang!\n🇷🇺Здравствуйте уважаемый пользователь. Выберите предпочтительный язык для использования!',reply_markup=Langbut)
        var.vaqtinchalik='changelang'

    if ddb.exists(message.from_user.id)==True:
        if ddb.get_lang(message.from_user.id)=='ru':
            await message.reply(var.titlesru[0],reply_markup=var.getproduct(var.productru))
            var.lang=int('uz'==ddb.get_lang(message.from_user.id))
        if ddb.get_lang(message.from_user.id)=='uz':
            await message.reply(var.titlesuz[0],reply_markup=var.getproduct(var.productuz))
            var.lang=int('uz'==ddb.get_lang(message.from_user.id))
        if ddb.get_lang(message.from_user.id)==None:
            var.vaqtinchalik='changelang'
            await message.reply('🇺🇿Foydalanish uchun o\'zingizga qulay bo\'lgan tilni tanlang!\n🇷🇺 Выберите предпочтительный язык для использования!',reply_markup=Langbut)
        #@fff
@dp.message_handler(content_types=['contact'])
async def handle_contact_east(message):
    telephone = message.contact.phone_number
    await message.reply('+'+telephone,reply_markup=share_keyboard2)
    await message.delete()
    await message.reply('Mahsulotlar',reply_markup=mahsulotlar)
@dp.callback_query_handler(text=['1','2','3','4','5','6','7','8','9','0','10','11','12','13','14','15','16','clear'])
async def calc_son(call: types.CallbackQuery):
    calldata=call.data
    if var.nowmahsulot=='Calc':
        if var.vaqtinchalik!='0':
            if call.data in ['1','2','3','4','5','6','7','8','9','0']:
                var.vaqtinchalik=var.vaqtinchalik+call.data
                if var.lang==0:
                    await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=var.titlesuz[2],reply_markup=var.getcalc())
                if var.lang==1:
                    await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=var.titlesru[2],reply_markup=var.getcalc())

            if call.data=='clear':
                print(len(var.vaqtinchalik))
                if len(var.vaqtinchalik)>1:
                    var.vaqtinchalik=var.vaqtinchalik[0:len(var.vaqtinchalik)-1]
                    if var.lang==0:
                        await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=var.titlesuz[2],reply_markup=var.getcalc())
                    if var.lang==1:
                        await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=var.titlesru[2],reply_markup=var.getcalc())

                if len(var.vaqtinchalik)==1:
                    var.vaqtinchalik='0'
                    await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=var.titlesru[2],reply_markup=var.getcalc())

            if var.vaqtinchalik=='0':
                if call.data in ['1','2','3','4','5','6','7','8','9']:
                    var.vaqtinchalik=call.data
                    await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=var.titlesru[1],reply_markup=var.getcalc())
                if call.data=='clear':
                    var.vaqtinchalik='0'
    if var.nowmahsulot=='start':
        var.savat.nomi  =var.products[int(i)]
        var.nowmahsulot=var.products[int(i)]
        if lang==0:
            cap=var.titlesuz[5]
        if lang==1:
            cap=var.titlesru[5]
        await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=cap,reply_markup=var.get_button())
    if (var.nowmahsulot==calldata[0:len(calldata)-1]) and (var.nowmahsulot in var.products  ):
        #sasas
        customb=db.mahsulotlar('product.db')
        await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=customb.get_name(calldata[len(calldata)-1:len(calldata)])+'\nNarxi '+customb.get_price(calldata[len(calldata)-1:len(calldata)]))

        #print('i')
        #await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='xullas tanlang',reply_markup=var.get_button(var.products[int(call.data)]))
#SET LANGUAGE
@dp.callback_query_handler(text=['uz','ru'])
async def change_lang(call: types.CallbackQuery):
    if var.vaqtinchalik=='changelang':
        if (call.data=='uz') or (call.data=='ru'):
            ddb.set_lang(call.message.chat.id,call.data)
            var.lang=int('ru'==call.data)
            if var.lang==0:
                bot.edit_message_text(text=var.titlesuz[0],chat_id=call.message.chat.id,  message_id=call.message.message_id,reply_markup=var.getproduct(var.productuz))
            if var.lang==1:
                bot.edit_message_text(text=var.titlesru[0],chat_id=call.message.chat.id,  message_id=call.message.message_id,reply_markup=var.getproduct(var.productru))

@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    print(message)
    reply = "latitude:  {}\nlongitude: {}".format(lat, lon)
    await message.answer(reply, reply_markup=types.ReplyKeyboardRemove())
    await bot.send_location(message.chat.id,latitude=lat,longitude=lon)
'''@dp.callback_query_handler(text=['1','2','3','4','5','6','7','8','9','0','10','11','12','13','14','15','16'])
async def choose_product(call: types.CallbackQuery):
    print('i')
    if var.nowmahsulot=='start':
        print('i')
        await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='xullas tanlang',reply_markup=var.get_button(var.products[int(call.data)]))
'''
executor.start_polling(dp)