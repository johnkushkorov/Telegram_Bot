#Ilhomjon(John) Kushkorov
#this code was used for to create a Telegram Bot that performs the commands that is given

import time, datetime #import the liB
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop
now = datetime.datetime.now()
red1 = 17#assign pins
red2 = 22
red3 = 27


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 


GPIO.setup(red1, GPIO.OUT)
GPIO.output(red1, 0) 
GPIO.setup(red2, GPIO.OUT)
GPIO.output(red2, 0) 
GPIO.setup(red3, GPIO.OUT)
GPIO.output(red3, 0) 
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Received: %s' % command)
    if 'hi' in command == '/hello':
            telegram_bot.sendMessage (chat_id, str("Hi To Whom It May Intrest In Class CET 4962"))
    elif command == '/time':
            telegram_bot.sendMessage(chat_id, str(now.hour)+str(":")+str(now.minute))
    elif command == '/logo':
            telegram_bot.sendPhoto (chat_id, photo = "https://res.cloudinary.com/campus-job/image/upload/t_student-public-page/v1/profile_pictures/iN9VtlfKh2_20170428.jpg")
    if 'on' in command:
        message = "Turned on "
        if 'red1' in command:
            message = message + "red1 "
            GPIO.output(red1, 1)
        if 'red2' in command:
            message = message + "red2 "
            GPIO.output(red2, 1)
        if 'red3' in command:
            message = message + "red3 "
            GPIO.output(red3, 1)
        if 'all' in command:
            message = message + "all "
            GPIO.output(red1, 1)
            GPIO.output(red2, 1)
            GPIO.output(red3, 1)
        message = message + "light(s)"
        telegram_bot.sendMessage (chat_id, message)
    if 'off' in command:
        message = "Turned off "
        if 'red1' in command:
            message = message + "red1 "
            GPIO.output(red1, 0)
        if 'red2' in command:
            message = message + "red2 "
            GPIO.output(red2, 0)
        if 'red3' in command:
            message = message + "red "
            GPIO.output(red3, 0)
        if 'all' in command:
            message = message + "all "
            GPIO.output(red1, 0)
            GPIO.output(red2, 0)
            GPIO.output(red3, 0)
        message = message + "light(s)"
        telegram_bot.sendMessage (chat_id, message)
 
telegram_bot = telepot.Bot('487727623:AAEQrQeny1oSzjLxoNUUEib7hHQeny41sEM')
print (telegram_bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()
print ('Waiting')
while 1:
    time.sleep(10)
