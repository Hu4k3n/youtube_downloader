from __future__ import unicode_literals
from telegram.ext import Updater, CommandHandler
import logging
import youtube_dl
import os

updater=Updater(token='<api token>',use_context=True)
dispatcher=updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
def start(update,context) :
    context.bot.send_message(chat_id=update.effective_chat.id, text="This is a work of Huraken")
def dl(update, context):
    p=update.message.text
    p = p.strip('\n')
    if (not "https://youtu.be" in p) :
        context.bot.send_message(chat_id=update.effective_chat.id, text='Wrong Link')

    ydl_opts = {
            'outtmpl':'music/%(title)s.%(ext)s',
            'format': 'bestaudio/best', 
                   'format': 'bestaudio/best',
               'postprocessors': [{
               'key': 'FFmpegExtractAudio',
               'preferredcodec': 'mp3',
               'preferredquality': '320',
             }],
                }
    if ("https://youtu.be" in p) :
        context.bot.send_message(chat_id=update.effective_chat.id, text='Checking Link...')
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([str(p)])
    
        list=os.listdir('music')
        context.bot.send_message(chat_id=update.effective_chat.id, text='Uploading Song...')
        context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('music/'+list[0], 'rb'))
        os.system("rm -rf music")
    context.bot.send_message(chat_id=update.effective_chat.id, text='Session Timeout Try again')
    print ('Session Complete')
    
from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, dl)
dispatcher.add_handler(echo_handler)

start_handler=CommandHandler('start',start)
dispatcher.add_handler(start_handler)
updater.start_polling()