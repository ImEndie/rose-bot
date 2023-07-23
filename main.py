import time
from bot import bot
from chat import gen_img, req
from filters import IsAdmin
from db import get_count,ins

@bot.message_handler(content_types=['new_chat_members'])
def new_chat_members(m):
    for i in m.new_chat_members:
        bot.send_message(m.chat.id,f"Salom {i.first_name}!\nGuruxga xush kelibsiz.")
    bot.delete_message(m.chat.id,m.id)

@bot.message_handler(content_types=['left_chat_member'])
def left_chat_member(m):
    bot.send_message(m.chat.id,f"Xayr {m.left_chat_member.first_name}!")
    bot.delete_message(m.chat.id,m.id)

@bot.message_handler(commands=['start'])
def start(m):
    ins(m.from_user.id)
    bot.reply_to(m,f"Salom {m.from_user.first_name}! Men sizning virtual yordamchingizman. Men bilan istalgan mavzuda guruxda yoki shaxsiy chatda suhbatlashishingiz mumkin. Shuningdek guruxlarda ba'zi qo'shimcha buyruqlar yordamida guruxni boshqarishingiz mumkin. Albatta adminlik huquqingiz bo'lsa😁\n\nBuruqlar ro'yxatini ko'rish uchun /help buyrug'idan foydalaning.")

@bot.message_handler(commands=['help'])
def help(m):
    bot.reply_to(m,"/ban — xabarga javob tariqasida ushbu xabarni yuboring va men uni guruxdan chetlataman.\n/mute sekund — xabarga javob tariqasida ushbu xabarni yuboring va men uni siz xoxlaganingizcha ovozini o'chirib turaman\n/rasm ta'rif — siz ta'riflaganingizdek rasm chizib beraman\n/stats — foydalanuvchilar soni")

@bot.message_handler(is_admin=True,commands=['ban'])
def ban(m):
    bot.ban_chat_member(m.chat.id,m.reply_to_message.from_user.id)
    bot.delete_message(m.chat.id,m.id)

@bot.message_handler(is_admin=True,content_types=['text'],func=lambda m: m.text.startswith('/mute'))
def mute(m):
    s=m.text.split()
    bot.restrict_chat_member(m.chat.id,m.reply_to_message.from_user.id,time.time()+(int(s[1])*60) if len(s)>0 else None)
    bot.delete_message(m.chat.id,m.id)

@bot.message_handler(is_admin=True,content_types=['text'],func=lambda m: m.text.startswith('/unmute'))
def unmute(m):
    bot.restrict_chat_member(m.chat.id,m.reply_to_message.from_user.id,time.time()+5)
    bot.delete_message(m.chat.id,m.id)

@bot.message_handler(commands=['stats'])
def stats(m):
    bot.reply_to(m,"Foydalanuvchilar soni: "+str(get_count()))


@bot.message_handler(content_types=['text'],func=lambda m: m.text.startswith('/rasm'))
def rasm(m):
    bot.send_photo(m.chat.id,photo=gen_img(m.text),reply_to_message_id=m.id)

@bot.message_handler(content_types=['text'],func=lambda m: m.text.startswith('@rosebyendie_bot'),chat_types=['group','supergroup'])
def rec_gr(m):
    bot.reply_to(m,req(m.text[16:]))

@bot.message_handler(content_types=['text'],chat_types=['private'])
def rec_pr(m):
    bot.reply_to(m,req(m.text))

bot.add_custom_filter(IsAdmin())

bot.infinity_polling()
