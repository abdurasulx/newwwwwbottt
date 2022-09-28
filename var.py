from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import db
nowmahsulot='ozod'
admin_id=1397715295

lang=-1
vaqtinchalik='0'
productuz=['Lavashlar','Setlar','Hot doglar','Xaggi','Shirinliklar','Pitsalar','Sendvichlar','Burger va donerlar','Sneklar','Salatlar','Ichimliklar ','Souslar']
productru=['Лавас','Сеты','Хот-доги','Хаггис','Десерты','Пицца','Сэндвичи','Бургеры и донеры','Закуски','Салаты','Напитки', 'Соусы']
products=['Lavashs','Setlar','Hotdogs','Xaggi','Shirinklar','Pitsalar','Sendvvischlar','Burgers','Sneklar','Salats','Ichimliklar','Souslar']
titlesuz=['Mahsulotlardan birini tanlang. Yetkazib berish endi o\'zimiz bilamiz','Tanlanmadi',' ta tanlandi','savatga o\'tish','Buyurtmalar tarixi','Tanlang','Savatga qo`shish','Geolokatsiyani jo `natish']
titlesru=['Выберите один из продуктов. Доставка теперь наша собственная','не выбран',' выбрано','перейти в корзину','История заказов','выбирать','Добавить в корзину','Отправить геолокацию']
setlar=["Setlar1","Setlar2","Setlar3","Setlar4","Setlar5","setlar6"]

back_button=InlineKeyboardButton(text='◀',callback_data='backtostart')
savat=InlineKeyboardButton(text='Savatchaga o\'tish',callback_data='savat')

locationbut=KeyboardButton(text='Give location',requist_location=True)
give_location=InlineKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).row(locationbut)
class savat():
    s=None
    nomi=None
    soni=None
class zakas():

    lat=None
    lon=None
    tulovturi=None
def getcalc():
    calc=InlineKeyboardMarkup()
    if lang==0:
        calc.row(InlineKeyboardButton(titleuz[0]+vaqtinchalik,callback_data='unknown'))
        savatga=InlineKeyboardButton(text=titlesuz[6],callback_data='savatga')
    if lang==1:
        calc.row(InlineKeyboardButton(titleru[0]+aqtinchalik,callback_data='unknown'))
        savatga=InlineKeyboardButton(text=titlesru[6],callback_data='savatga')
    calc.row(InlineKeyboardButton('1',callback_data='1'),InlineKeyboardButton('2',callback_data='2'),InlineKeyboardButton('3',callback_data='3'))
    calc.row(InlineKeyboardButton('4',callback_data='4'),InlineKeyboardButton('5',callback_data='5'),InlineKeyboardButton('6',callback_data='6'))
    calc.row(InlineKeyboardButton('7',callback_data='7'),InlineKeyboardButton('8',callback_data='8'),InlineKeyboardButton('9',callback_data='9'))
    calc.row(InlineKeyboardButton('0',callback_data='0'),InlineKeyboardButton('<---',callback_data='clear'))
    if lang==0:
        savatga=InlineKeyboardButton(text=titlesuz[3],callback_data='savat')

    if lang==1:
        savatga=InlineKeyboardButton(text=titlesru[3],callback_data='savat')

    calc.row(savatga)
    calc.row(historybut)
    calc.row(back_button)
    return calc

def getproduct(product):
    calc=InlineKeyboardMarkup()
    for i in range(0,len(product)):
        if (i)%2==1:
            #print(product[i-1],'\t',product[i])
            calc.row(InlineKeyboardButton(text=product[i-1],callback_data=str(i-1)),InlineKeyboardButton(text=product[i],callback_data=str(i)))
    calc.row(historybut)
    calc.row(savat)
    nowmahsulot='start'
    return calc
def get_button(dbname):
    c=InlineKeyboardMarkup()
    a=db.mahsulotlar('products.db')
    for i in range(0,a.get_count(dbname)):
        if i%2==1:
            c.row(InlineKeyboardButton(text=a.get_name(i,dbname),callback_data=dbname+str(i)),InlineKeyboardButton(text=a.get_name(i+1,dbname),callback_data=str(i+1)))
        #print(getproduct())
        if (i==(a.get_count(dbname))) and (i%2==0):
            c.row(InlineKeyboardButton(text=a.get_name(i,dbname)))
    nowmahsulot=dbname
    return c